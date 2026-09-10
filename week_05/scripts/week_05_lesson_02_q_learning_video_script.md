# Q-Learning: Off-Policy Temporal-Difference Control - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 5, Lesson 2
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

Q-learning learns a greedy target policy from transitions gathered by a possibly exploratory behavior policy, without querying transition probabilities. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Derive Q-learning from the Bellman optimality target. 2) Compute numeric Q updates including terminal cases. 3) Implement epsilon-greedy selection with deterministic tie handling. 4) Explain behavior versus target policy. 5) State sufficient exploration and learning-rate convergence conditions. 6) Design a defensible episodic training and evaluation loop. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - Q-learning targets greedy control while behaving exploratorily

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

The update bootstraps from the maximum next-state action value, regardless of which next action the behavior policy takes. The supporting details make the claim operational. 1) The table stores one estimate per state-action pair. 2) The target uses max over next actions. 3) Terminal transitions do not bootstrap. The highlighted idea, Off-policy, is the part to retain when the surrounding notation changes. Behavior gathers coverage; the target defines the greedy policy being learned. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - The Q-learning update samples Bellman optimality

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: Q(s,a) <- Q(s,a) + alpha [r + gamma max_a' Q(s',a') - Q(s,a)]. The symbols mean the following. 1) alpha is the learning rate. 2) gamma discounts continuation. 3) r,s' are sampled from interaction. 4) The maximum defines the greedy target. The engineering implication is If s' is terminal, replace the maximum continuation term with zero. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Behavior and target policies have separate jobs

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Behavior policy: Usually epsilon-greedy. Generates transitions. Must cover relevant actions. Changes as Q changes. On the right, Target policy: Greedy with respect to Q. Defines bootstrap target. Represents learned control. Used without exploration at evaluation. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - A Q-learning episode alternates action and update

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Reset: Receive an initial state. 2) Choose: Sample epsilon-greedy action. 3) Step: Observe reward, successor, done. 4) Update: Apply terminal-aware target. 5) Decay: Adjust epsilon on schedule. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. Update exactly once per observed transition and never bootstrap past terminal. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - The training loop keeps environment and agent separate

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Validate state indexes. Seed tie randomness. Cap episode length. Log epsilon and return. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked Q update

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is Q(s,a)=2, reward=1, max Q(s',.)=4, gamma=0.9, and alpha=0.5. Work through it in the displayed order. 1) Target=1+0.9*4=4.6. 2) TD error=4.6-2=2.6. 3) Increment=0.5*2.6=1.3. 4) Set Q(s,a)=3.3. The resulting conclusion is Only the experienced state-action entry changes on this tabular update. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Q-learning and SARSA use different next-action targets

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Q-learning: Target uses max_a' Q. Learns greedy target. Behavior can explore. Can be optimistic near risk. In contrast, SARSA: Target uses chosen next action. Learns epsilon-greedy behavior value. Includes exploration consequences. Policy and data align. In contrast, Shared: One-step bootstrap. Need learning rate. Need repeated coverage. Terminal target is reward. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: compute a terminal update

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: Q(s,a)=5, terminal reward=1, alpha=0.2, gamma=0.99. What is the new Q value? Use the prompts to structure the response. 1) Remove future bootstrap. 2) Compute error 1-5. 3) Apply alpha. The expected reasoning is The new value is 5+0.2*(-4)=4.2. Gamma does not appear because the successor is terminal. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Epsilon-greedy must define exploration and ties

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Exploration branch: Occurs with probability epsilon. Sample uniformly or by documented rule. Can choose the current greedy action too. Improves state-action coverage. On the right, Greedy branch: Occurs with probability 1-epsilon. Choose an argmax action. Tie handling changes behavior. Evaluation normally uses epsilon=0. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Convergence requires continued evidence and controlled steps

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: visit every (s,a) infinitely often; sum_t alpha_t=infinity; sum_t alpha_t^2<infinity. The symbols mean the following. 1) Coverage prevents permanently unknown actions. 2) Nonzero total step size permits correction. 3) Finite squared step size controls noise. 4) Finite MDP and bounded rewards are standard assumptions. The engineering implication is A practical finite run can only provide empirical evidence, not the asymptotic guarantee itself. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Epsilon decay changes discovery probability

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is A sparse-reward action is initially undervalued and requires repeated trials before its benefit appears. Work through it in the displayed order. 1) High initial epsilon explores the action. 2) Updates raise its Q estimate after success. 3) Gradual decay shifts behavior toward exploitation. 4) A too-fast decay may freeze the wrong policy. The resulting conclusion is Compare schedules across seeds and evaluate the final greedy policy separately. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Hyperparameters control distinct failure modes

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Learning rate: Too high oscillates. Too low learns slowly. Decay can stabilize. Log TD magnitude. In contrast, Discount: Low is myopic. High values delayed reward. Near one raises variance. Must match task. In contrast, Epsilon: High sacrifices reward. Low misses alternatives. Decay timing matters. Report schedule. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: diagnose no learning

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: A Q-table stays zero in a sparse-reward maze; epsilon decays to zero after ten episodes. What is the likely problem and first experiment? Use the prompts to structure the response. 1) Separate update logic from data coverage. 2) Inspect visited actions and rewards. 3) Change one schedule variable. The expected reasoning is Exploration likely ended before reward was discovered. Log coverage and reward events, then use a slower decay or larger epsilon floor while keeping the update equation unchanged. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - Validate Q-learning against a known-model oracle

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

On small environments, compare the learned greedy policy with value iteration while preserving agent-model separation. The supporting details make the claim operational. 1) Unit-test one-step updates with hand values. 2) Run multiple seeds and report mean plus variability. 3) Evaluate without exploration or learning and check terminal behavior. The highlighted idea, Ablation, is the part to retain when the surrounding notation changes. Controlled comparisons reveal whether exploration, update logic, or evaluation causes failure. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) Q-learning is off-policy TD control. 2) The target is reward plus discounted maximum next Q. 3) Terminal transitions never bootstrap. 4) Exploration, learning rate, and evaluation protocol determine credible results. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Week 6 replaces the Q-table with function approximation to generalize across large state spaces. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Compute two Q-learning updates. 2) Contrast Q-learning with SARSA. 3) Explain epsilon-greedy tie handling. 4) State convergence conditions. 5) Design a sparse-reward diagnostic experiment. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_05/Week_5_Lesson_2_Q_Learning.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.
- Richard Sutton and Andrew Barto, Reinforcement Learning: An Introduction, 2nd edition.

**Approximate narration word count:** 2468
