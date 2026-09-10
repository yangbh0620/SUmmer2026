# From Linear Approximation to Deep Q-Networks - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 6, Lesson 2
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

A deep Q-network learns its own representation, but naive online bootstrapping combines correlated data with a rapidly moving target. Replay and target networks reshape that learning problem. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Map a discrete-action state to one Q value per action. 2) Explain temporal correlation and moving targets. 3) Describe replay-buffer sampling and data reuse. 4) Distinguish online and target network roles. 5) Compute a terminal-aware mini-batch target. 6) Trace the complete DQN training loop. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - DQN is Q-learning with engineered stabilization

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

A neural network supplies the action-value function while replay and a target network reduce two major sources of instability. The supporting details make the claim operational. 1) One forward pass outputs all discrete-action values. 2) Replay breaks short-range temporal correlation. 3) A frozen target network supplies short-window consistency. The highlighted idea, Stabilization, is the part to retain when the surrounding notation changes. The mechanisms improve the training distribution and slow movement of the bootstrap target. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - The DQN target and loss

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: y = r + gamma(1-done) max_a Q(s_next,a;theta_minus); L = mean[(y-Q(s,a;theta))^2]. The symbols mean the following. 1) theta are online-network parameters. 2) theta_minus are target-network parameters. 3) done masks every terminal bootstrap. 4) Only theta receives the gradient step. The engineering implication is The two networks have distinct responsibilities even when their architectures match. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Online and target networks form a controlled handoff

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Online network: Selects epsilon-greedy actions. Predicts Q(s,a;theta). Updated every training step. Receives gradients from loss. On the right, Target network: Computes next-state target values. Frozen for a short interval. Copied or softly updated. Never optimized directly. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Data flows through six explicit stages

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Act: Choose from the online network. 2) Store: Append a complete transition. 3) Sample: Draw a random mini-batch. 4) Target: Evaluate next states with theta_minus. 5) Update: Optimize theta and periodically synchronize. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. Keeping action selection, target construction, and optimization separate prevents accidental gradient paths. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - High-level DQN training loop

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Warm up the buffer. Sample without sequence bias. Detach targets. Sync on a fixed schedule. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked target: terminal masks matter

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is A batch item has reward 2, gamma 0.9, target-network next values [1,4,3], and done=0. Work through it in the displayed order. 1) The maximum next value is 4. 2) The bootstrap contribution is 0.9(4)=3.6. 3) The target is 5.6. 4) If done becomes 1, the multiplicative mask removes 3.6. The resulting conclusion is The nonterminal target is 5.6; the terminal target is exactly 2. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Three training regimes expose the design

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Naive online: Strong correlation. No data reuse. Same moving network. Often oscillatory. In contrast, Replay only: Better sample mixture. Reuses experience. Target still moves fast. Needs buffer policy. In contrast, Full DQN: Decorrelated batches. Short-window targets. More state to manage. Still no guarantee. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: find the forbidden gradient

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: A student computes y with the online network and allows automatic differentiation through y. What is wrong? Use the prompts to structure the response. 1) Identify both target defects. 2) Name the parameter set that should update. 3) Describe the required stop-gradient. The expected reasoning is The target moves with the same network and the optimizer can chase changes on both sides of the loss. Compute y with theta_minus and detach it; optimize theta only. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Replay changes the training distribution

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Sequential stream: Adjacent states are similar. Recent policy dominates. One transition used once. Ordering can bias gradients. On the right, Random mini-batch: Samples mix times and episodes. Older policies remain represented. Transitions are reused. Distribution still reflects buffer contents. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Hard and soft target updates

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: hard: theta_minus <- theta every C steps; soft: theta_minus <- tau theta + (1-tau) theta_minus. The symbols mean the following. 1) C is the hard-copy interval. 2) tau is a small interpolation rate. 3) Hard updates create piecewise-constant targets. 4) Soft updates move every step but more slowly. The engineering implication is The synchronization rule is a hyperparameter and must be logged with results. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Replay sampling breaks a correlated run

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is The last eight transitions all come from the same corridor, while a 10,000-item buffer spans many states. Work through it in the displayed order. 1) Online-only training sees eight nearly identical inputs. 2) A uniform batch draws across older episodes. 3) Gradient directions reflect several regions. 4) Repeated data use improves sample efficiency. The resulting conclusion is Replay reduces immediate correlation but cannot repair a buffer that never contains rare successful transitions. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Buffer choices create different evidence

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Capacity: Small adapts quickly. Large increases diversity. Large can retain stale data. Memory cost is explicit. In contrast, Sampling: Uniform is simple. Prioritized focuses error. Weights may be needed. Seed controls reproducibility. In contrast, Warm-up: Avoid tiny biased batches. Delay early gradients. Costs interaction steps. Log threshold. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: remove one stabilizer

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: What symptom would you expect without replay, and what different symptom would you expect without a target network? Use the prompts to structure the response. 1) Separate data correlation from target motion. 2) Name an observable metric. 3) Avoid claiming a theoretical cure. The expected reasoning is Without replay, successive gradients can be highly aligned and brittle to trajectory order. Without a target network, TD targets can oscillate rapidly with online parameters. Track loss, TD errors, Q magnitudes, and return across seeds. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - DQN adds state that must be checkpointed

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

A reproducible DQN run includes more than neural-network weights. The supporting details make the claim operational. 1) Serialize online and target networks separately. 2) Record buffer capacity, sampling seed, and sync cadence. 3) Evaluate with frozen parameters and epsilon zero. The highlighted idea, State, is the part to retain when the surrounding notation changes. Replay contents, target parameters, optimizer moments, counters, epsilon, and random states affect continuation. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) DQN maps one state to all discrete-action values. 2) Replay reduces temporal correlation and reuses data. 3) Target networks slow bootstrap-target movement. 4) Both mechanisms mitigate, but do not eliminate, deadly-triad risk. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Bayesian networks introduce a different way to represent uncertainty: explicit probabilistic structure. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Compute a masked DQN target. 2) Explain why y must be detached. 3) Compare hard and soft synchronization. 4) Describe replay warm-up. 5) Name all checkpoint state. 6) Predict failure without either stabilizer. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_06/Week_6_Lesson_2_Intro_to_Deep_Q_Networks.md
- Richard Sutton and Andrew Barto, Reinforcement Learning: An Introduction, 2nd edition.
- Volodymyr Mnih et al., Human-level control through deep reinforcement learning, Nature 518, 2015.

**Approximate narration word count:** 2541
