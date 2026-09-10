# Solving MDPs: Value Iteration and Policy Iteration - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 4, Lesson 2
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

Dynamic programming solves a known finite MDP by repeatedly applying Bellman structure until values and action choices become self-consistent. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Distinguish Bellman expectation from Bellman optimality. 2) Perform a value-iteration backup. 3) Explain the gamma-contraction convergence intuition. 4) Extract a greedy policy from values. 5) Trace policy evaluation and policy improvement. 6) Compare value iteration with policy iteration. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - Optimal control replaces policy averaging with maximization

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

The Bellman optimality operator chooses the action with the greatest expected one-step reward plus continuation value. The supporting details make the claim operational. 1) Expectation evaluates a specified policy. 2) Optimality maximizes over actions. 3) A greedy policy with respect to V* is optimal. The highlighted idea, Fixed point, is the part to retain when the surrounding notation changes. V* is unchanged by another optimality backup. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - Expectation and optimality use different backups

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: T^pi V: sum_a pi(a|s) q_V(s,a)        T*V: max_a q_V(s,a). The symbols mean the following. 1) q_V includes P, R, and gamma V. 2) T^pi keeps policy fixed. 3) T* selects the best action at each state. 4) V*=T*V*. The engineering implication is Do not average actions when computing an optimality backup. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Value iteration mixes evaluation and improvement

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Value backup: Initialize V arbitrarily. Apply T* to every nonterminal state. Use a synchronous copy for clear semantics. Stop by max-norm residual. On the right, Policy extraction: Compute q_V(s,a). Choose an argmax action. Break ties deterministically. Terminal states have no action. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Value iteration converges through repeated contraction

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Initialize: Set terminal and nonterminal values. 2) Backup: Compute every new state value. 3) Measure: Find max absolute change. 4) Stop: Compare with tolerance. 5) Extract: Build the greedy policy. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. A stopping rule should measure a documented residual, not an arbitrary iteration count alone. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - Value iteration uses a synchronous Bellman sweep

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Terminal value is fixed. Read old V in one sweep. Normalize transitions. Guard max iterations. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - One value-iteration backup

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is State A has actions Exit for reward 2, or Wait for reward 0 then return to A; gamma=0.9 and current V(A)=5. Work through it in the displayed order. 1) Q(A,Exit)=2. 2) Q(A,Wait)=0+0.9*5=4.5. 3) Take the maximum. 4) Set new V(A)=4.5. The resulting conclusion is The greedy action under the current values is Wait, even though later sweeps may change it. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Contraction turns approximation into a convergence guarantee

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Operator: Maps one value vector to another. Uses max over actions. Preserves bounded values. Has fixed point V*. In contrast, Contraction: Distance shrinks by at most gamma. Requires gamma<1. Repeated backups converge. Residual bounds error. In contrast, Tolerance: Tracks max change. Balances time and precision. Depends on gamma. Report iterations. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: compute an optimality backup

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: Action a has expected backup 4.2 and action b has expected backup 3.7. What value and greedy action result? Use the prompts to structure the response. 1) Identify the optimality operator. 2) Take the maximum. 3) State the tie rule if values were equal. The expected reasoning is The new value is 4.2 and the greedy action is a. If equal, use a documented deterministic tie rule. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Policy iteration separates evaluation and improvement

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Policy evaluation: Hold pi fixed. Solve or iterate T^pi V=V. Estimate V^pi. Stop at evaluation tolerance. On the right, Policy improvement: Hold V fixed. Choose argmax q_V(s,a). Replace inferior actions. Stop when policy is stable. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Greedy improvement cannot reduce policy value

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: pi'(s) in argmax_a q^(pi)(s,a)  implies  V^(pi')(s) >= V^pi(s). The symbols mean the following. 1) q^pi evaluates one deviation then follows pi. 2) pi' chooses a maximizing deviation. 3) Policy improvement holds statewise. 4) A stable greedy policy satisfies optimality. The engineering implication is Finite deterministic policies prevent endless strict improvement. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - One policy-improvement step

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is Under current V^pi, state A's action values are Left=1.2, Right=2.8, and Stay=2.1. Work through it in the displayed order. 1) Evaluate all legal actions with the same V^pi. 2) Find the maximum value 2.8. 3) Set pi'(A)=Right. 4) Record whether the action changed. The resulting conclusion is Right replaces the old action unless it was already selected; stability is checked across all states. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Value and policy iteration trade sweep cost for count

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Value iteration: One optimality sweep per iteration. Many simple iterations. Easy vectorization. Policy extracted at end. In contrast, Policy iteration: Fewer outer iterations. Evaluation can be expensive. Policy is explicit throughout. Exact or approximate evaluation. In contrast, Modified PI: Partial evaluation. Regular improvement. Balances costs. Needs clear stopping rules. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: diagnose a terminal-state bug

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: A solver applies gamma V(terminal) after entering a terminal state and repeatedly collects its reward. What is wrong? Use the prompts to structure the response. 1) State the intended terminal semantics. 2) Identify double counting. 3) Describe the code-level fix. The expected reasoning is The terminal transition reward should be collected once, with no bootstrapped continuation. Fix the transition or backup so terminal successor value contributes zero and terminal states are not repeatedly rewarded. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - Numerical convergence needs observable evidence

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Report residual, iteration count, policy stability, and validation against hand-solvable MDPs. The supporting details make the claim operational. 1) Use max-norm residual and a maximum-iteration guard. 2) Compare VI and PI policies on the same model. 3) Test gamma=0, gamma near 1, terminal-only, and unreachable states. The highlighted idea, Convergence, is the part to retain when the surrounding notation changes. A loop ending is not evidence that the intended fixed point was reached. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) Bellman optimality maximizes rather than averages policy actions. 2) Value iteration converges because T* is a gamma-contraction. 3) Policy iteration alternates evaluation and greedy improvement. 4) Terminal semantics and tolerance determine reliable implementations. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Week 5 removes the known transition model and learns values from sampled interaction. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Compute one value-iteration sweep. 2) Explain the contraction intuition. 3) Extract a greedy policy. 4) Trace one policy-improvement step. 5) Compare VI and PI on per-iteration cost. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_04/Week_4_Lesson_2_Value_and_Policy_Iteration.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.
- Richard Sutton and Andrew Barto, Reinforcement Learning: An Introduction, 2nd edition.

**Approximate narration word count:** 2484
