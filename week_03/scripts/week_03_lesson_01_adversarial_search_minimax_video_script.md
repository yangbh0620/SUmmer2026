# Adversarial Search: Game Trees and Minimax - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 3, Lesson 1
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

Adversarial search retains states, actions, successors, and a tree, but the objective changes because another decision maker selects harmful replies. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Define game state, player function, terminal test, utility, and game tree. 2) Compute minimax values by backward induction. 3) Trace mutually recursive MAX and MIN procedures. 4) Sketch minimax correctness under optimal play. 5) Derive O(b^m) time and O(bm) depth-first space. 6) Design and test depth-limited evaluation functions. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - An opponent changes the backup, not the state-space idea

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

Minimax values a state by assuming MAX optimizes utility and MIN optimizes the opposing objective. The supporting details make the claim operational. 1) MAX chooses the largest child value. 2) MIN chooses the smallest child value. 3) Terminal utility anchors the recursion. The highlighted idea, Contingency, is the part to retain when the surrounding notation changes. A plan must specify a response to every opponent action, not one fixed path. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - Minimax is a recursive value definition

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: V(s)=UTILITY(s) if terminal; max_a V(RESULT(s,a)) for MAX; min_a V(RESULT(s,a)) for MIN. The symbols mean the following. 1) PLAYER(s) identifies who moves. 2) ACTIONS(s) lists legal moves. 3) RESULT(s,a) gives the successor. 4) UTILITY(s) is defined at terminal states. The engineering implication is The root action is selected by child value, not by a single predicted opponent move. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - Single-agent paths become adversarial strategies

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Pathfinding search: Environment does not choose against the agent. Solution is one action sequence. Goal and path cost evaluate a path. Frontier ordering guides expansion. On the right, Game-tree search: Players alternate control. Solution is a contingent strategy. Terminal utility evaluates outcomes. Backups propagate values. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - Backward induction computes rational play

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Expand: Generate legal continuations. 2) Anchor: Assign utility at terminals. 3) Minimize: Back up MIN choices. 4) Maximize: Back up MAX choices. 5) Choose: Select the root action with highest value. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. Every backup represents control by the player named at that state. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - Minimax alternates MAX and MIN recursion

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: Terminal test must stop. Utility uses MAX's perspective. Turns alternate correctly. Ties are deterministic. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked minimax backup

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is MAX has Left and Right. Their MIN children lead to leaves [3,5] and [2,9]. Work through it in the displayed order. 1) Left MIN chooses min(3,5)=3. 2) Right MIN chooses min(2,9)=2. 3) MAX compares 3 and 2. 4) MAX chooses Left. The resulting conclusion is The root minimax value is 3 even though the tree contains a leaf worth 9. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Game assumptions determine what minimax means

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Zero-sum: One scalar utility. MIN lowers MAX value. Standard minimax model. Tie policy still matters. In contrast, Perfect information: No hidden cards or state. Legal actions are known. Deterministic successor. Chance is absent. In contrast, Optimal play: Opponent selects best reply. Value is conservative. Weak opponents may do better. Guarantee is model-relative. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: back up a small tree

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: A MIN node has three MAX children valued 4, -1, and 6. What value is returned, and which branch can MIN select? Use the prompts to structure the response. 1) Identify the player controlling the node. 2) Apply the correct extremum. 3) Interpret the result from MAX's perspective. The expected reasoning is MIN returns -1 and may select the second branch because utility is measured from MAX's perspective. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Depth limits replace terminal utility with evaluation

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, Terminal utility: Exact for completed games. Aligned with win, loss, or score. Too deep in large games. No approximation at leaves. On the right, Evaluation function: Estimates nonterminal strength. Combines informative features. Must use one consistent perspective. Creates approximation error. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Game trees grow exponentially

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: nodes through depth m = 1+b+...+b^m = O(b^m). The symbols mean the following. 1) b is average legal-move count. 2) m is search depth in plies. 3) Each ply adds another branching layer. 4) Depth-first recursion stores O(bm) pending siblings and path state. The engineering implication is A modest depth increase can multiply work by b, making cutoffs operationally necessary. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Evaluation features encode strategic judgment

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is A Pacman-style state is cut off before a terminal win or loss. Work through it in the displayed order. 1) Reward current score and nearby food. 2) Penalize collision risk and nearby active ghosts. 3) Treat scared ghosts with a different sign. 4) Normalize feature scales before weighting. The resulting conclusion is The evaluator ranks frontier states but does not change the legal game model. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Evaluation defects can dominate deeper search

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. Perspective error: MIN and MAX disagree. Wins can look bad. Backups remain consistent but wrong. Use one utility convention. In contrast, Horizon effect: Threat is delayed. Shallow value looks safe. Quiescence can help. Test tactical positions. In contrast, Scale error: One term overwhelms others. Weights become uninterpretable. Scores become unstable. Inspect component values. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: choose a cutoff result

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: At a depth-limited MIN node, evaluation values are 7, 3, and 5 from MAX's perspective. What value backs up? Use the prompts to structure the response. 1) Keep the perspective fixed. 2) Apply MIN at the cutoff's parent. 3) State whether the value is exact. The expected reasoning is The backed-up value is 3. It is an estimate because the children were evaluated before terminal outcomes. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - A minimax implementation needs structural tests

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Test turn alternation, terminal handling, value perspective, and tie order independently. The supporting details make the claim operational. 1) Compare recursive output with a hand-computed tree. 2) Assert the input state is not mutated. 3) Instrument depth, generated nodes, and chosen root action. The highlighted idea, Oracle, is the part to retain when the surrounding notation changes. Tiny hand-valued trees provide exact expected outputs. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) Minimax backs values through alternating MAX and MIN control. 2) Its result is a contingent strategy under optimal play. 3) Time is O(b^m), so practical search uses depth limits. 4) Evaluation quality and perspective are part of correctness. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Alpha-beta pruning preserves the minimax value while avoiding irrelevant branches; expectimax adds chance. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Back up a two-ply minimax tree. 2) Explain why a strategy is not one path. 3) Derive O(b^m). 4) Design an evaluation function for a small game. 5) Name tests for turn and utility defects. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_03/Week_3_Lesson_1_Adversarial_Search_Minimax.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.

**Approximate narration word count:** 2527
