# Informed Search: Greedy, A-star, and Heuristic Design - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 2, Lesson 2
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

A heuristic estimates remaining cost and changes which frontier node is examined next. The quality and mathematical properties of that estimate determine efficiency and optimality. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Define heuristic, admissibility, consistency, and dominance. 2) Trace Greedy Best-First Search and A-star using g, h, and f. 3) Sketch A-star's optimality argument under admissible or consistent h. 4) Derive heuristics from relaxed problems. 5) Verify Manhattan-distance consistency on four-neighbor grids. 6) Implement deterministic A-star with correct cost updates. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - A heuristic injects domain knowledge into ordering

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

A heuristic h(n) estimates the cheapest remaining cost from node n to a goal. The supporting details make the claim operational. 1) h uses state information unavailable to uninformed ordering. 2) h is not the cost already paid. 3) A heuristic can be informative, weak, or unsafe. The highlighted idea, Estimate, is the part to retain when the surrounding notation changes. Useful estimates reduce irrelevant expansion while respecting the model's cost units. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - Greedy and A-star use different priority functions

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: Greedy: f(n) = h(n)        A-star: f(n) = g(n) + h(n). The symbols mean the following. 1) g(n) is exact accumulated cost. 2) h(n) estimates remaining optimal cost h*(n). 3) Greedy ignores paid cost. 4) A-star balances paid and estimated cost. The engineering implication is Priority and duplicate-update logic must use the same numeric cost model. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Greedy pursues promise; A-star preserves evidence

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Greedy Best-First: Priority is h only. Can reach a goal quickly. Can follow a deceptive heuristic. Not generally optimal. On the right, A-star: Priority is g+h. Reduces to UCS when h=0. Optimal under stated h conditions. Needs cheaper-path updates. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Design a heuristic through a relaxed problem

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Model: State the original constraints and cost. 2) Relax: Remove constraints, never add them. 3) Solve: Compute the relaxed optimal cost. 4) Verify: Check goal value and edge inequalities. 5) Measure: Compare expansion and runtime empirically. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. A relaxed optimum is a principled lower bound on the original optimum. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - A-star extends the UCS priority queue

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Store best g by state. Skip stale queue entries. Use h(goal)=0. Break ties deterministically. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked A-star trace

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is S reaches A with g=2,h=3 and B with g=1,h=5; A reaches G with cost 3. Work through it in the displayed order. 1) Insert A with f=5 and B with f=6. 2) Remove A because f is smaller. 3) Generate G with g=5,h=0,f=5. 4) Remove G before B and return S-A-G. The resulting conclusion is A-star returns cost 5; the frontier still contains B with f=6. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Heuristic properties answer different questions

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Admissible: 0 <= h(n) <= h*(n). Never overestimates. Supports A-star tree-search proof. h(goal)=0 follows. In contrast, Consistent: h(n) <= c(n,n')+h(n'). Triangle inequality. Implies admissibility. f does not decrease along paths. In contrast, Dominant: h2(n) >= h1(n). Both remain admissible. h2 is at least as informed. May reduce expansion. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: test consistency

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: For an edge A to B with cost 2, h(A)=5 and h(B)=2. Is the heuristic consistent on this edge? Use the prompts to structure the response. 1) Write the consistency inequality. 2) Substitute the three values. 3) State whether admissibility alone can be inferred. The expected reasoning is No, because 5 <= 2+2 is false. One violated edge proves inconsistency. This local result alone does not establish whether the heuristic is globally admissible. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Manhattan and Euclidean distance encode relaxations

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Manhattan distance: |dx|+|dy|. Exact without obstacles on four-neighbor unit grids. Consistent for unit orthogonal moves. Can overestimate if diagonal moves cost 1. On the right, Euclidean distance: sqrt(dx^2+dy^2). Straight-line relaxed path. Fits continuous or geometric motion. Often weaker on four-neighbor grids. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - A-star's lower-bound argument protects the optimum

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: For optimal path node n: f(n)=g(n)+h(n) <= g(n)+h*(n)=C*. The symbols mean the following. 1) C* is optimal solution cost. 2) Admissibility supplies h(n) <= h*(n). 3) A suboptimal goal G has f(G)=g(G)>C*. 4) Minimum-f removal selects an optimal-path node first. The engineering implication is A suboptimal goal cannot be removed while an optimal-path frontier node remains. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Manhattan consistency follows from one move

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is A legal grid move changes exactly one coordinate by one and costs 1. Work through it in the displayed order. 1) Let h be Manhattan distance to the goal. 2) One move changes h by at most 1. 3) Therefore h(s) <= 1+h(s'). 4) The edge consistency inequality holds. The resulting conclusion is Manhattan distance is consistent and therefore admissible for this movement model. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Heuristic failure modes are model mismatches

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Overestimate: Can lose optimality. Often caused by wrong move costs. Goal value may be nonzero. Counterexample needed. In contrast, Too weak: Behaves like UCS. Optimal but expands more. Relaxation removed too much. Measure expansion. In contrast, Inconsistent: Graph search may reopen states. Stale entries appear. Local edge test detects it. Correctness policy must match. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: choose a grid heuristic

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: A grid permits eight directions; orthogonal moves cost 1 and diagonal moves cost sqrt(2). Is Manhattan distance admissible? Use the prompts to structure the response. 1) Compare one diagonal displacement. 2) Compute Manhattan and true relaxed cost. 3) Name a better geometric heuristic. The expected reasoning is No. For a one-by-one diagonal displacement, Manhattan returns 2 while the legal diagonal costs sqrt(2). Octile distance or Euclidean distance respects the movement model. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - Heuristics require both proof and measurement

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Validate mathematical safety separately from empirical usefulness. The supporting details make the claim operational. 1) Unit-test h(goal)=0 and sampled edge consistency. 2) Compare solution cost against UCS on small instances. 3) Report expansions, maximum frontier, and wall-clock time. The highlighted idea, Evidence, is the part to retain when the surrounding notation changes. A proof supports optimality; benchmarks support efficiency claims. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) Greedy orders by h; A-star orders by g+h. 2) Admissibility is a global lower bound; consistency is an edge inequality. 3) Relaxed problems provide principled heuristics. 4) Correct A-star needs best-g updates and deterministic queue behavior. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Week 3 replaces a passive environment with an optimizing opponent and introduces minimax. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Trace A-star on a five-node weighted graph. 2) Give an admissible but inconsistent heuristic. 3) Prove Manhattan consistency for one grid edge. 4) Explain heuristic dominance. 5) Design tests for an A-star implementation. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_02/Week_2_Lesson_2_Informed_Search_and_Heuristics.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.

**Approximate narration word count:** 2534
