# Alpha-Beta Pruning and Expectimax - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 3, Lesson 2
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

Alpha-beta pruning makes minimax faster without approximation, while expectimax changes the model by replacing an optimizing opponent with chance. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Define alpha and beta as backed-up bounds. 2) Trace exact alpha-beta prune conditions. 3) Explain why pruning preserves the minimax root value. 4) Relate move ordering to effective branching factor. 5) Compute expectimax chance-node values. 6) Choose between minimax and expectimax from environment assumptions. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - Alpha-beta pruning is exact

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

A branch may be skipped only after bounds prove that it cannot change an ancestor's decision. The supporting details make the claim operational. 1) MAX prunes when v >= beta. 2) MIN prunes when v <= alpha. 3) Unpruned minimax and alpha-beta return the same value. The highlighted idea, Bound, is the part to retain when the surrounding notation changes. Alpha is MAX's best guaranteed value; beta is MIN's best guaranteed value. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - Alpha and beta summarize ancestor alternatives

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: alpha = best MAX value on path; beta = best MIN value on path; prune when alpha >= beta. The symbols mean the following. 1) Alpha is a lower bound for MAX. 2) Beta is an upper bound for MAX under MIN control. 3) Bounds tighten monotonically down a path. 4) A cutoff occurs only when an ancestor already has a better choice. The engineering implication is Initialize alpha=-infinity and beta=+infinity at the root. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Pruning changes work, not semantics

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Plain minimax: Visits every node to depth m. Returns exact minimax value. Order does not affect value. Time O(b^m). On the right, Alpha-beta: Skips provably irrelevant nodes. Returns the same exact value. Order strongly affects work. Best case approaches O(b^(m/2)). The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - A cutoff follows a local proof

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Enter: Receive alpha and beta. 2) Evaluate: Search one child. 3) Update: Tighten the current bound. 4) Compare: Test alpha against beta. 5) Prune: Skip dominated siblings. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. The comparison is valid because an ancestor already owns a dominating alternative. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - Alpha-beta threads bounds through recursion

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Start v=+infinity. Cut when v<=alpha. Update beta=min(beta,v). Keep one utility perspective. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked alpha-beta cutoff

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is MAX's first MIN child returns 5, so alpha becomes 5. A second MIN child first reveals value 3. Work through it in the displayed order. 1) The second child is controlled by MIN. 2) Its current value is at most 3. 3) MAX already has an alternative worth 5. 4) Remaining siblings under that MIN node cannot improve MAX's choice. The resulting conclusion is Prune the remaining siblings; the root value remains 5. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Move ordering controls pruning efficiency

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Best first: MAX sees high values early. MIN sees low values early. Many cutoffs. Depth roughly doubles for same work. In contrast, Random: Some useful early bounds. Variable node counts. Value remains exact. Seed for reproducibility. In contrast, Worst first: Cutoffs arrive late. Approaches plain minimax. Value remains exact. Ordering heuristic matters. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: identify the cutoff

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: At a MIN node with alpha=4, the first child returns 2. Can the remaining children be pruned? Use the prompts to structure the response. 1) Update the MIN node's current value. 2) Compare v with alpha. 3) Explain the ancestor's existing alternative. The expected reasoning is Yes. The MIN node's value is at most 2, which is already no better for MAX than the ancestor alternative worth 4, so v<=alpha triggers a cutoff. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Expectimax models chance rather than hostility

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, MIN node: Another agent chooses an action. Backup is minimum utility. Represents worst rational reply. Needs adversarial assumption. On the right, Chance node: Outcome is sampled from a distribution. Backup is probability-weighted mean. Represents stochastic dynamics. Needs calibrated probabilities. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Chance nodes back up expected value

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: V(s) = sum_o P(o | s) V(RESULT(s,o)). The symbols mean the following. 1) Outcomes o are mutually exclusive. 2) Probabilities are nonnegative. 3) Probabilities sum to 1. 4) Child values use the same utility scale. The engineering implication is Expectimax can prefer risk when a high payoff raises expected utility. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Minimax and expectimax can choose differently

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is Safe action returns 4. Risky action returns 0 or 10 with probability 0.5 each. Work through it in the displayed order. 1) Minimax values Risky at min(0,10)=0. 2) Expectimax values Risky at 0.5*0+0.5*10=5. 3) Safe remains value 4. 4) The preferred action depends on the model. The resulting conclusion is Minimax selects Safe; expectimax selects Risky under the stated probabilities. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Evaluation design remains a practical bottleneck

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Features: Progress toward objective. Threat and opportunity. Mobility or control. Terminal conditions dominate. In contrast, Weights: Normalize magnitudes. Document sign and units. Avoid double counting. Validate on tactical cases. In contrast, Ordering: Reuse evaluation cheaply. Try promising moves first. Cache repeated states. Do not change backed-up rule. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: compute a chance backup

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: A chance node reaches values -2, 4, and 10 with probabilities 0.2, 0.5, and 0.3. What value backs up? Use the prompts to structure the response. 1) Check that probabilities sum to 1. 2) Multiply each value by its probability. 3) Add the three contributions. The expected reasoning is The expected value is -0.4+2+3=4.6. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - Cross-check exact optimization against the baseline

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Every alpha-beta implementation should match plain minimax on small trees while expanding no more nodes. The supporting details make the claim operational. 1) Generate small deterministic trees with known leaves. 2) Compare values across multiple action orders. 3) Test expectimax separately with normalized probability tables. The highlighted idea, Equivalence, is the part to retain when the surrounding notation changes. Value and root action are correctness evidence; node count is optimization evidence. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) Alpha-beta is an exact minimax optimization. 2) Alpha and beta are path-relative decision bounds. 3) Move ordering changes work but not value. 4) Expectimax replaces adversarial minimum with a probability-weighted mean. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Week 4 generalizes sequential decision making under uncertainty with Markov decision processes. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Trace alpha-beta on a two-ply tree. 2) Explain why a cutoff preserves value. 3) Derive the best-case square-root branching effect. 4) Compute a chance-node expectation. 5) Choose minimax or expectimax for a stated domain. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_03/Week_3_Lesson_2_Alpha_Beta_Pruning_and_Expectimax.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.

**Approximate narration word count:** 2512
