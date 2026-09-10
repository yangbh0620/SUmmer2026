# Reinforcement Learning Fundamentals - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 5, Lesson 1
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

Reinforcement learning replaces exact model backups with data gathered from interaction, creating simultaneous estimation and exploration problems. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Distinguish planning from reinforcement learning. 2) Compare model-based and model-free learning. 3) Define episode, bootstrapping, behavior policy, and target policy. 4) Derive and compute a TD(0) update. 5) Explain exploration versus exploitation. 6) Distinguish on-policy from off-policy learning. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - Learning uses samples where planning uses a model

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

An RL agent must improve estimates and behavior from transitions it actually experiences. The supporting details make the claim operational. 1) The transition model may be unknown. 2) Rewards can be delayed and noisy. 3) Exploration changes which state-action pairs are observed. The highlighted idea, Experience, is the part to retain when the surrounding notation changes. Data collection depends on current behavior, so the agent influences its own evidence. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - The TD error compares a sample with a bootstrap target

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: delta_t = R_(t+1) + gamma V(S_(t+1)) - V(S_t). The symbols mean the following. 1) R_(t+1) is sampled immediate reward. 2) V(S_(t+1)) estimates continuation. 3) V(S_t) is the current prediction. 4) delta is a signed prediction error. The engineering implication is For a terminal successor, the continuation term is zero. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Model-based and model-free RL learn different objects

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Model-based RL: Learns or knows P and R. Plans inside the learned model. Can reuse simulated experience. Model bias can mislead. On the right, Model-free RL: Learns V, Q, or policy directly. No explicit transition table required. Often simpler control loop. May need more interaction. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Interaction creates an online learning loop

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Reset: Start an episode. 2) Select: Choose an exploratory action. 3) Observe: Receive next state and reward. 4) Update: Move estimate toward target. 5) Repeat: Continue until terminal or limit. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. Behavior determines data coverage, so exploration is part of the learning algorithm. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - TD(0) updates one transition at a time

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: alpha sets step size. gamma discounts future. Terminal stops bootstrap. Samples are correlated. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked TD update

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is V(A)=4, transition A to B gives reward 2, V(B)=5, gamma=0.9, and alpha=0.1. Work through it in the displayed order. 1) Target=2+0.9*5=6.5. 2) TD error=6.5-4=2.5. 3) Increment=0.1*2.5=0.25. 4) Set V(A)=4.25. The resulting conclusion is The estimate moves partway toward the one-step bootstrap target. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Planning and learning use different backup evidence

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Bellman model backup: Uses every successor probability. No sampled transition required. Deterministic given V. Requires known P and R. In contrast, Monte Carlo: Waits until episode end. No bootstrap. Unbiased return sample. Can have high variance. In contrast, TD(0): Updates before episode end. Bootstraps from V. Lower variance, some bias. No model required. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: compute TD error

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: V(s)=3, reward=-1, V(s')=4, gamma=0.5. What is the TD error and the new value for alpha=0.2? Use the prompts to structure the response. 1) Compute the target. 2) Subtract the old prediction. 3) Apply the learning-rate step. The expected reasoning is The target is -1+0.5*4=1. The error is 1-3=-2, and the new value is 3+0.2*(-2)=2.6. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Exploration and exploitation serve different evidence needs

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Exploitation: Choose the current best action. Improves immediate performance. Concentrates on known behavior. Can lock into a poor estimate. On the right, Exploration: Try uncertain alternatives. Improves coverage. Can sacrifice immediate reward. Needs scheduling and limits. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Incremental updates average evidence over time

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: V(S_t) <- V(S_t) + alpha_t [target_t - V(S_t)]. The symbols mean the following. 1) alpha_t controls adaptation. 2) Constant alpha tracks nonstationarity. 3) Decaying alpha can support convergence. 4) The bracketed term is prediction error. The engineering implication is Large alpha learns quickly but can make estimates noisy or unstable. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Sparse reward exposes inadequate exploration

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is A long corridor gives zero reward until a distant goal gives +10; an early side action gives +1. Work through it in the displayed order. 1) Greedy behavior discovers the side reward first. 2) It repeatedly exploits +1. 3) The distant goal remains unobserved. 4) Exploration occasionally samples the corridor and reveals +10. The resulting conclusion is Observed performance depends on data coverage, not only the update equation. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - On-policy and off-policy name the learning target

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. On-policy: Target includes exploratory policy. Evaluation matches data policy. SARSA is a control example. Safer behavior may be learned. In contrast, Off-policy: Behavior gathers data. Target may be greedy. Q-learning is an example. Coverage conditions matter. In contrast, Engineering: Log epsilon schedule. Seed action sampling. Separate evaluation runs. Do not learn during testing. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: identify the policy relation

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: An epsilon-greedy behavior policy generates data while updates target a purely greedy action. Is learning on-policy or off-policy? Use the prompts to structure the response. 1) Name the behavior policy. 2) Name the target policy. 3) Compare whether they are identical. The expected reasoning is It is off-policy because the behavior is epsilon-greedy while the target is greedy. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - RL experiments need separation and repeatability

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Separate training from evaluation, control randomness, and report variation across seeds. The supporting details make the claim operational. 1) Evaluate with learning disabled and a fixed policy. 2) Cap episode length to prevent hangs. 3) Log return, length, exploration, and update magnitude. The highlighted idea, Protocol, is the part to retain when the surrounding notation changes. A rising training return is not an unbiased estimate of final policy quality. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) RL learns from sampled interaction when the model is unavailable. 2) TD combines one sampled reward with a bootstrapped continuation estimate. 3) Exploration determines data coverage. 4) On-policy and off-policy distinguish behavior from target. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Q-learning applies off-policy TD updates directly to action values for control. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Compute a TD(0) update. 2) Contrast model-based and model-free RL. 3) Explain bootstrapping. 4) Design an exploration schedule. 5) Distinguish behavior and target policies. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_05/Week_5_Lesson_1_Reinforcement_Learning_Fundamentals.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.
- Richard Sutton and Andrew Barto, Reinforcement Learning: An Introduction, 2nd edition.

**Approximate narration word count:** 2442
