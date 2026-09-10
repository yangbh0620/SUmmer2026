# Formulating Markov Decision Processes - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 4, Lesson 1
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

A Markov decision process models repeated decisions in a stochastic environment where present actions influence a long trajectory of rewards. This lesson treats the topic as both a formal method and an engineering component. We will state the model, trace the algorithm on concrete data, and identify the implementation contracts that preserve its guarantees. The goal is not to memorize isolated notation. The goal is to recognize which assumptions make the method valid, what evidence can expose a defect, and how the method connects to the rest of CMPSC 480. By the end, you should be able to explain the central result, reproduce the critical calculation or trace, and design a defensive implementation that behaves predictably on normal, boundary, and invalid inputs. Keep one question active throughout: what would a skeptical reviewer need to observe before trusting the result?

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order.

These objectives define the evidence expected after the lesson. 1) Define the MDP tuple <S,A,P,R,gamma>. 2) Test whether a state representation satisfies the Markov property. 3) Distinguish trajectory, reward, return, and discount. 4) Define policy pi, V^pi, and Q^pi. 5) Derive the Bellman expectation equation. 6) Compute a fixed-policy value in a small MDP. The sequence moves from vocabulary and assumptions to derivation, tracing, implementation, and judgment. As you work through the slides, attach every equation to the meaning of its variables and every algorithmic step to a data-structure operation. When a guarantee is stated, ask which precondition supports it. When an implementation choice is shown, ask which test would reveal a violation. That discipline turns the objectives into reusable engineering practice rather than a list of terms. You should finish able to explain both the successful case and the nearest counterexample.

## Slide 3 - An MDP is a persistent stochastic decision model

**Suggested pacing:** 3 minutes
**Visual cue:** State the claim, then connect each detail to observable behavior.

The agent commits to a policy that maps states to action distributions across an extended trajectory. The supporting details make the claim operational. 1) Transitions are probabilistic, not adversarial. 2) Rewards arrive along a trajectory. 3) Value aggregates present and discounted future reward. The highlighted idea, Policy, is the part to retain when the surrounding notation changes. A policy specifies behavior at every reachable decision state. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 4 - The MDP tuple defines dynamics and preference

**Suggested pacing:** 3 minutes
**Visual cue:** Define every symbol before applying the relation.

Read the displayed relation as a compact specification rather than decorative notation: MDP = <S, A, P(s'|s,a), R(s,a,s'), gamma>. The symbols mean the following. 1) S is the state set. 2) A is the action set. 3) P gives successor probabilities. 4) R gives transition reward; 0 <= gamma < 1 discounts delay. The engineering implication is Every transition distribution must be nonnegative and sum to 1. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 5 - The Markov property is a sufficiency claim

**Suggested pacing:** 3 minutes
**Visual cue:** Compare the two columns using the same input or decision criterion.

The two columns separate related responsibilities. On the left, Markov state: Predicts next outcome from current state and action. No extra history is required. Supports recursive value equations. Can include memory summaries. On the right, Incomplete state: Hidden history changes transitions. Same stored state has different futures. Bellman backup mixes incompatible cases. Add the missing variable or belief. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 6 - A trajectory generates discounted return

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the sequence from left to right and pause at the highlighted stage.

This process gives a disciplined execution order. 1) Observe: Receive state S_t. 2) Act: Sample A_t from policy. 3) Transition: Sample S_(t+1) from P. 4) Reward: Receive R_(t+1). 5) Accumulate: Discount and sum future rewards. The emphasized stage deserves extra attention because defects introduced there propagate to every later result. Return evaluates a sequence, while reward labels one transition. When implementing the process, record the invariant that should hold after each stage and decide how failure will be represented. When analyzing it, trace a small instance all the way through before relying on an aggregate output. A useful review asks what state enters each stage, what state leaves it, and which later stage would expose corruption.

## Slide 7 - A simulator exposes the MDP interface

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one iteration and identify the invariant.

The pseudocode shows the control structure while leaving language-specific details open. Read it from initialization through termination and identify the state that changes on each iteration. The rail lists the stable questions: State is Markov. Policy sees state only. Step samples P. Terminal stops future reward. A faithful implementation should make those decisions explicit rather than depend on incidental container behavior. Trace the code on a minimal legal input, a boundary case, and a case that triggers its failure path. That three-part trace usually reveals incorrect initialization, update ordering, or termination earlier than a large demonstration does. Also estimate the dominant operation and choose a data structure whose cost matches the stated complexity.

## Slide 8 - Worked return calculation

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the result before revealing it.

The scenario is A trajectory yields rewards 2, -1, and 5 with gamma=0.9. Work through it in the displayed order. 1) Weight the first reward by 1. 2) Weight the second by 0.9. 3) Weight the third by 0.9^2. 4) Add 2-0.9+4.05. The resulting conclusion is The discounted return is 5.15. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 9 - Value functions answer related conditional questions

**Suggested pacing:** 3 minutes
**Visual cue:** Compare information, ordering, and guarantees.

This comparison organizes the alternatives by the information they use and the guarantee they can support. V^pi(s): Expected return from s. Follow pi immediately. Averages over policy actions. One value per state. In contrast, Q^pi(s,a): Expected return after action a. Then follow pi. Supports action comparison. One value per state-action. In contrast, Policy pi(a|s): Action distribution. Can be deterministic. Defines on-policy values. Must normalize by state. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 10 - Checkpoint: repair a non-Markov state

**Suggested pacing:** 2 minutes
**Visual cue:** Pause for individual work before discussing the guidance.

Pause before reading the guidance and answer the checkpoint: A machine's failure probability depends on how many consecutive hours it has run, but state stores only current temperature. Is the state Markov? Use the prompts to structure the response. 1) Identify hidden history that affects P. 2) Name a sufficient additional variable. 3) Explain the Bellman consequence. The expected reasoning is No. Consecutive runtime affects the next failure distribution. Add runtime, wear level, or a sufficient health statistic to state; otherwise one Bellman value mixes states with different dynamics. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 11 - Expectimax and MDPs share expectation but differ in scope

**Suggested pacing:** 3 minutes
**Visual cue:** Use the interface boundary to separate responsibilities.

The two columns separate related responsibilities. On the left, One game-tree decision: Choose a root move. Chance may appear at nodes. Finite lookahead is common. No stationary behavior required. On the right, MDP policy problem: Choose behavior for all states. Environment persists. Long or infinite horizon. Recursive values seek consistency. The distinction matters because combining these concerns prematurely often hides an assumption or duplicates logic. A strong implementation exposes the boundary through clear types or functions, then tests each side independently before testing the combined behavior. The key takeaway is to compare the columns by information used, result produced, and failure modes, not merely by their names. If a design mixes both roles, label where the handoff occurs and what invariant crosses it.

## Slide 12 - Bellman expectation decomposes one step

**Suggested pacing:** 3 minutes
**Visual cue:** Work the relation one term at a time.

Read the displayed relation as a compact specification rather than decorative notation: V^pi(s) = sum_a pi(a|s) sum_s' P(s'|s,a)[R(s,a,s') + gamma V^pi(s')]. The symbols mean the following. 1) Outer sum averages policy actions. 2) Inner sum averages successor states. 3) R is immediate reward. 4) gamma V is discounted continuation value. The engineering implication is A value function is a fixed point consistent with its policy and model. Work one term at a time, verify dimensions or domains before calculating, and separate the mathematical result from its numerical representation. A useful test case should make each term observable and should include a boundary condition that would fail if a sign, index, normalization, or termination rule were implemented incorrectly. Before substituting numbers, predict the sign, scale, and limiting behavior of the result. Then translate the relation into a function signature and identify which inputs must be validated before the arithmetic begins.

## Slide 13 - Fixed-policy value in a two-state MDP

**Suggested pacing:** 3 minutes
**Visual cue:** Trace the second example and contrast it with the first.

The scenario is In state A, a fixed action gives reward 1 and stays in A with probability 0.5 or terminates with probability 0.5; gamma=0.8. Work through it in the displayed order. 1) Write V(A)=1+0.8[0.5 V(A)+0.5*0]. 2) Collect 0.4 V(A) on the left. 3) Obtain 0.6 V(A)=1. 4) Divide by 0.6. The resulting conclusion is V(A)=5/3, approximately 1.667. This example is intentionally small enough to verify by hand. That makes it useful as an oracle for unit tests and for diagnosing discrepancies in a larger implementation. After reproducing the result, change one assumption or input and predict which intermediate quantity should change. If the output changes without the corresponding intermediate evidence, the implementation is not preserving the model. Record the trace in a table so that every update has a visible cause. Finally, state which theorem, invariant, or modeling assumption makes the result generalizable beyond this one instance.

## Slide 14 - Discounting has mathematical and modeling roles

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which column fits a stated scenario and why.

This comparison organizes the alternatives by the information they use and the guarantee they can support. gamma=0: Future is ignored. Myopic behavior. Simple backup. Useful boundary test. In contrast, 0<gamma<1: Delayed reward matters. Bounded infinite return. Contraction later applies. Scale is interpretable. In contrast, gamma near 1: Future decays slowly. Values can be large. Convergence can slow. Numerical tolerance matters. Do not choose a column by familiarity alone. Match the choice to the problem assumptions, available resources, and required evidence. In an exam answer or design review, state one reason the selected method fits and one reason another method does not. In an implementation, keep the shared interface stable so that the alternatives can be tested on the same inputs and compared with the same metrics. A fair experiment changes one method choice while holding data, seed, budget, and evaluation criterion constant. Report not only the winner but also the condition under which the ranking could reverse.

## Slide 15 - Checkpoint: apply the Bellman equation

**Suggested pacing:** 2 minutes
**Visual cue:** Pause, then require the assumption and the result.

Pause before reading the guidance and answer the checkpoint: A deterministic policy receives reward 3, moves to state B, and V^pi(B)=4 with gamma=0.5. What is V^pi(A)? Use the prompts to structure the response. 1) Use the one available action. 2) Use successor probability 1. 3) Add reward and discounted continuation. The expected reasoning is V^pi(A)=3+0.5*4=5. A complete answer should show the governing definition or equation, apply it to the supplied facts, and state any assumption needed to remove ambiguity. If your answer differs, identify the first inference where the reasoning diverges rather than changing only the final value. The point is diagnostic: a justified wrong step is easier to repair than an unexplained correct guess. After resolving it, invent one nearby variant that would change the answer and explain exactly why.

## Slide 16 - Validate an MDP before solving it

**Suggested pacing:** 3 minutes
**Visual cue:** Connect the highlighted engineering principle to a concrete test.

Transition normalization, terminal semantics, reward timing, and state sufficiency are executable preconditions. The supporting details make the claim operational. 1) Assert each transition row sums to 1 within tolerance. 2) Define terminal actions and continuation value explicitly. 3) Use small hand-computed policies as numerical oracles. The highlighted idea, Model, is the part to retain when the surrounding notation changes. A solver cannot recover a guarantee from an inconsistent environment definition. A correct explanation should name the assumptions, describe the observable behavior, and distinguish the method from a superficially similar alternative. In code, this claim becomes a contract that can be exercised with a small counterexample as well as a representative case. Try to state the claim in one sentence, then identify the smallest input that would falsify an incorrect version.

## Slide 17 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Review the four takeaways and preview the next lesson.

The lesson reduces to four reusable ideas. 1) An MDP combines Markov state, actions, transition probabilities, rewards, and discount. 2) A policy defines behavior over all states. 3) V and Q are expected discounted returns. 4) Bellman expectation is a recursive fixed-point condition for a policy. These are connected: the formal model supplies the algorithm, the algorithm's invariant supports its guarantee, and the implementation contract makes that guarantee testable. The next topic is Value iteration and policy iteration replace evaluation of a fixed policy with optimal control. Before moving on, make sure you can reproduce one worked trace without notes and can name one edge case that would distinguish a correct implementation from a plausible but defective one. Keep the summary as a checklist for the corresponding code lab and review questions.

## Slide 18 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group.

Use these questions as an exit check. 1) Classify a state as Markov or incomplete. 2) Compute a three-reward discounted return. 3) Distinguish V^pi from Q^pi. 4) Derive a two-state Bellman equation. 5) List MDP validation checks. Answer with definitions, calculations, traces, or design evidence rather than one-word labels. When a question asks for a comparison, hold the input and evaluation criterion constant. When it asks for a derivation, show the intermediate quantities. When it asks for an engineering decision, name the contract and the test that supports it. Any answer that depends on an unstated convention should make that convention explicit. A strong answer should be concise enough to audit yet complete enough to reproduce.

## Reference Notes

- Repository prompt: week_04/Week_4_Lesson_1_MDP_Formulation.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition.
- Richard Sutton and Andrew Barto, Reinforcement Learning: An Introduction, 2nd edition.

**Approximate narration word count:** 2471
