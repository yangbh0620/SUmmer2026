# Scaling Up: Function Approximation in Reinforcement Learning - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 6, Lesson 1
**Target duration:** Approximately 50 minutes
**Format:** Narration script only; no video or audio is produced.

## Production Notes

- Use the matching PowerPoint slide number shown in each section.
- Read equations deliberately and define every symbol on first use.
- Pause after checkpoint questions before discussing the instructor guidance.
- On-screen emphasis cues are optional and must not change the slide content.

## Slide 1 - Opening

**Suggested pacing:** 2 minutes
**Visual cue:** Introduce the engineering question and connect it to the previous lesson.

A Q-table treats every state-action pair as unrelated. Function approximation replaces that table with shared parameters so evidence from one experience can influence similar situations. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Quantify why tabular Q-learning fails in large or continuous spaces. 2) Represent action values as a linear function of state-action features. 3) Design normalized features that encode useful similarity. 4) Derive the semi-gradient Q-learning weight update. 5) Compute a complete numerical TD update by hand. 6) Explain the deadly triad and identify stability evidence. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - Approximation trades exact storage for generalization

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

A parameterized Q function shares statistical strength across state-action pairs but couples their errors. The supporting details make the claim operational. 1) Memory depends on parameter count, not the number of states. 2) Features define which situations share value information. 3) Approximation introduces bias and possible instability. The highlighted idea, Generalization, is the part to retain when the surrounding notation changes. Updating one experience changes every prediction that uses overlapping features. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - Linear action-value approximation

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: Q_hat(s,a;w) = w^T f(s,a) = sum_i w_i f_i(s,a). The symbols mean the following. 1) f(s,a) is a d-dimensional feature vector. 2) w contains d learned weights. 3) One-hot features recover a tabular Q function. 4) Dense shared features create generalization. The engineering implication is Feature scale and semantics become part of the agent contract. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - A table memorizes; a feature model shares

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Tabular Q: One value per state-action pair. No transfer to unseen pairs. Exact representation in finite tables. Memory grows as |S||A|. On the right, Linear approximation: One dot product per action. Transfer through shared features. Possible approximation bias. Memory grows with d. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Feature design is a modeling workflow

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Define: Name the behavioral signal each feature represents. 2) Normalize: Put magnitudes on comparable scales. 3) Probe: Evaluate features on boundary states. 4) Train: Log TD errors and weight norms. 5) Ablate: Remove one feature family at a time. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. A feature is justified by predictive evidence, not by an intuitive name. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - Semi-gradient Q-learning with linear features

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Treat target as fixed. Mask terminal bootstrap. Cache the feature vector. Monitor finite weights. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked update: one transition changes three weights

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is w=[0.4,-0.2,0.1], f(s,a)=[1,0.5,2], reward=1, gamma=0.9, max next Q=1.5, alpha=0.1. Work through it in the displayed order. 1) Current Q is 0.4-0.1+0.2=0.5. 2) Target is 1+0.9(1.5)=2.35. 3) TD error is 2.35-0.5=1.85. 4) Add 0.185 times the feature vector to w. The resulting conclusion is The new weights are [0.585,-0.1075,0.47], and every overlapping prediction changes. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Useful grid features encode distinct signals

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Geometry: Normalized row and column. Distance to goal. Distance to hazards. Wall adjacency indicators. In contrast, Action relation: Alignment with goal direction. Collision indicator. Progress delta. Action one-hot encoding. In contrast, Quality checks: Finite and bounded values. Stable scale across maps. Cheap computation. Ablation evidence. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: identify shared updates

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: Two state-action pairs have feature vectors [1,1,0] and [1,0,1]. Which prediction changes after updating the first pair? Use the prompts to structure the response. 1) Write the weight increment. 2) Take its dot product with the second vector. 3) State which shared coordinate causes transfer. The expected reasoning is The increment affects coordinates one and two. The second prediction changes through the shared bias coordinate, even though the other active feature differs. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - A semi-gradient freezes the bootstrap target

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Prediction side: Differentiate Q_hat(s,a;w). Gradient is f(s,a) for a linear model. Update parameters each step. Directly controls current prediction. On the right, Target side: Contains a next-state prediction. Treated as a constant for this step. Not differentiated through. Moves again after parameters change. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Deriving the weight update

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: L=0.5(y-Q_hat)^2; delta=y-Q_hat; w <- w + alpha delta grad_w Q_hat. The symbols mean the following. 1) y=r+gamma max Q_hat(s_next,a) for nonterminal steps. 2) The negative loss gradient is delta grad Q_hat. 3) For a linear model, grad Q_hat=f(s,a). 4) Terminal y equals reward only. The engineering implication is The semi-gradient update resembles supervised regression onto a moving TD target. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - One-hot features recover the tabular rule

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is A feature vector has one active coordinate for exactly one pair (s,a). Work through it in the displayed order. 1) The dot product selects one weight. 2) Its gradient is one at that coordinate and zero elsewhere. 3) The update changes only that selected weight. 4) The result matches Q(s,a) <- Q(s,a)+alpha delta. The resulting conclusion is Tabular Q-learning is a linear approximator with a very large one-hot feature basis. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - The deadly triad marks a risk boundary

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Approximation: Couples predictions. Creates representation error. May amplify updates. Enables scale. In contrast, Bootstrapping: Uses a moving target. Propagates value quickly. Can propagate error. Reduces full-return delay. In contrast, Off-policy: Behavior and target differ. Supports exploration reuse. Changes sampling distribution. Completes the triad. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: diagnose divergence

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: Training return rises while weight norm and absolute TD error explode. Is high return alone enough to accept the agent? Use the prompts to structure the response. 1) Name two stability metrics. 2) Check multiple seeds. 3) Separate evaluation from exploratory return. The expected reasoning is No. Exploding weights and TD errors are direct instability evidence. Freeze learning, evaluate greedily across seeds, and reduce step size or redesign features before accepting the result. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - Instrument approximation before tuning

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

A scalable agent needs observability for representation error and numerical stability. The supporting details make the claim operational. 1) Log returns, TD-error quantiles, feature ranges, and weight norms. 2) Test terminal masking and feature dimensions directly. 3) Compare against a tabular oracle on a small discretized environment. The highlighted idea, Evidence, is the part to retain when the surrounding notation changes. Learning curves alone cannot distinguish lucky behavior from a stable value function. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) Linear Q functions generalize through shared features. 2) The semi-gradient update freezes the TD target. 3) One-hot features reveal the table as a special case. 4) The deadly triad motivates explicit stability monitoring. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Deep Q-networks replace hand-designed linear features with learned representations. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Compute a linear Q value from w and f. 2) Derive the semi-gradient sign. 3) Explain why feature normalization matters. 4) Show the one-hot tabular correspondence. 5) Design a divergence-detection test. 6) Name the three parts of the deadly triad. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_06/Week_6_Lesson_1_Function_Approximation.md
- Richard Sutton and Andrew Barto, Reinforcement Learning: An Introduction, 2nd edition.

**Approximate narration word count:** 2540
