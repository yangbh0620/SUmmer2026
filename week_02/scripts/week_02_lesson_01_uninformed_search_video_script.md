# Uninformed Search: BFS, DFS, and Uniform-Cost Search - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 2, Lesson 1
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

Uninformed search explores with no estimate of distance to the goal. Its behavior is governed by frontier ordering, duplicate handling, and step-cost assumptions. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Trace BFS, DFS, and UCS with a frontier and explored set. 2) Define branching factor b, solution depth d, maximum depth m, and path cost g. 3) Compare completeness, optimality, time, and space guarantees. 4) Explain why graph search requires immutable state keys. 5) Sketch why BFS is optimal for uniform costs and UCS for positive costs. 6) Implement all three strategies behind one frontier interface. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - Frontier ordering defines the search strategy

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

BFS, DFS, and UCS share the same expansion loop; only the removal priority changes. The supporting details make the claim operational. 1) BFS removes the shallowest node. 2) DFS removes the most recently added node. 3) UCS removes the node with minimum accumulated path cost. The highlighted idea, Policy, is the part to retain when the surrounding notation changes. Queue, stack, and minimum-g priority produce different search behavior. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - Search analysis uses four recurring quantities

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: b = branching factor; d = shallowest solution depth; m = maximum depth; g(n) = path cost. The symbols mean the following. 1) b bounds the number of successors generated per expansion. 2) d counts edges to a shallowest goal. 3) m bounds search depth when the space is finite. 4) g(n) sums step costs along node n's path. The engineering implication is A guarantee is meaningful only when its cost and graph assumptions are stated. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Breadth and depth trade memory for commitment

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Breadth-first search: FIFO frontier; expand nondecreasing depth. Complete for finite branching factor. Optimal when every step has equal cost. Time and space grow as O(b^d). On the right, Depth-first search: LIFO frontier; follow one path deeply. Can fail in infinite-depth spaces. Not generally optimal. Space is O(bm); time can be O(b^m). The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Generic graph search exposes the shared control loop

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Initialize: Create the root node and frontier. 2) Remove: Apply the strategy's priority. 3) Test: Return if the node state is a goal. 4) Expand: Generate legal child nodes. 5) Deduplicate: Control repeated states and cost updates. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. Correct duplicate handling is part of the algorithm, not a performance afterthought. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - One search loop accepts a frontier policy

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: BFS: FIFO by depth. DFS: LIFO. UCS: minimum g. Stable ties aid reproducibility. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked trace: BFS finds the shallow goal

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is S connects to A and B; A connects to C; B connects to goal G; every edge costs 1. Work through it in the displayed order. 1) Start frontier: [S]. Remove S; add A, B. 2) Remove A; explored is {S, A}; add C. 3) Remove B; add G behind C. 4) Remove C, then G; reconstruct S-B-G. The resulting conclusion is BFS returns depth 2 and cost 2; no depth-1 goal existed. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Completeness and optimality depend on assumptions

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. BFS: Complete if b is finite. Optimal for equal step cost. High memory. Ignores cheaper deep paths. In contrast, DFS: Low memory. May follow infinite path. Not optimal. Order strongly affects result. In contrast, UCS: Complete if costs >= epsilon. Optimal for positive costs. May expand many cheap paths. Needs cost updates. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: trace two frontier policies

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: If S adds A then B, A adds G at depth 2, and B adds C then G at depth 3, which goal does BFS return and which path can DFS return? Use the prompts to structure the response. 1) Write the frontier after expanding S. 2) Apply FIFO and LIFO separately. 3) State the assumption about successor order. The expected reasoning is BFS returns S-A-G because it reaches the depth-2 goal first. With A then B pushed onto a LIFO stack, DFS may expand B first and return S-B-C-G; reversing push order changes that trace. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Tree nodes and graph states are different objects

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Node record: Stores parent, action, depth, and g. Represents one path. Two nodes may share a state. Used for reconstruction. On the right, State key: Represents a world configuration. Needs stable equality and hashing. Drives explored membership. May map to a best known cost. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Why BFS and UCS can certify optimality

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: BFS: depth order + constant c; UCS: remove n only when g(n) is globally minimum. The symbols mean the following. 1) With constant c, lower depth means lower path cost. 2) BFS reaches no deeper goal before every shallower node. 3) UCS frontier priorities are accumulated path costs. 4) Positive costs prevent an unseen path from becoming cheaper after removal. The engineering implication is The first goal removed is optimal under the stated ordering and cost conditions. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Cheaper rediscovery must update UCS

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is S-A costs 5, S-B costs 1, and B-A costs 1; A leads to G with cost 1. Work through it in the displayed order. 1) S first discovers A with g=5 and B with g=1. 2) UCS removes B before A. 3) B rediscovers A with g=2, replacing the worse entry. 4) A then reaches G with total cost 3. The resulting conclusion is Rejecting every duplicate at generation time would incorrectly preserve the cost-6 route. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Common implementation defects have distinct symptoms

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Wrong ordering: BFS acts like DFS. UCS ignores g. Ties vary across runs. Guarantees no longer apply. In contrast, Wrong duplicate rule: Cycles repeat. Cheaper paths are lost. Frontier grows unnecessarily. Parents become inconsistent. In contrast, Wrong contract: Illegal actions expand. Costs can be nonpositive. Goal test accepts bad state. Failure is ambiguous. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: evaluate a guarantee

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: An implementation uses BFS on edges with costs 1 and 10 and returns the first goal at minimum depth. Is the result guaranteed to have minimum cost? Use the prompts to structure the response. 1) Separate depth from path cost. 2) Construct a two-path counterexample. 3) Name the suitable replacement algorithm. The expected reasoning is No. A depth-2 path can cost 20 while a depth-3 path costs 3. Uniform-cost search, with positive costs and correct updates, is the suitable minimum-cost strategy. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - A shared interface makes guarantees testable

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Keep domain expansion fixed and vary only the frontier policy when comparing search strategies. The supporting details make the claim operational. 1) Instrument nodes generated, expanded, maximum frontier, and solution cost. 2) Use deterministic successor and tie order. 3) Test trivial, cyclic, unreachable, cheaper-rediscovery, and scale cases. The highlighted idea, Control, is the part to retain when the surrounding notation changes. A fair comparison holds states, successors, costs, and goal behavior constant. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) BFS, DFS, and UCS are one graph-search loop with different removal priorities. 2) Completeness and optimality always depend on explicit assumptions. 3) Graph search needs immutable states and a correct duplicate-cost policy. 4) Small traces reveal ordering and update defects before scale tests do. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Informed search adds heuristics and develops Greedy Best-First Search and A-star. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Trace BFS and DFS on the same four-node graph. 2) Give a graph where BFS is not minimum cost. 3) Explain why UCS requires a positive lower bound on step cost. 4) Derive the O(b^d) BFS space term. 5) Design a test that exposes a missing UCS cost update. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_02/Week_2_Lesson_1_Uninformed_Search.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.

**Approximate narration word count:** 2691
