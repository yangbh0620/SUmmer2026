# Course Introduction and the AI Engineering Mindset - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 1, Lesson 1
**Target duration:** Approximately 50 minutes
**Format:** Narration script only; no video or audio is produced.

## Production Notes

- Use the matching PowerPoint slide number shown in each section.
- Read equations deliberately and define every symbol on first use.
- Pause after checkpoint questions before discussing the instructor guidance.
- On-screen emphasis cues are optional and must not change the slide content.

## Slide 1 - Opening

**Suggested pacing:** 2 minutes
**Visual cue:** Hold on the title, then emphasize the phrase production-quality systems.

Welcome to CMPSC 480, AI Curriculum Engineering. This course begins from a premise that is easy to state but demanding to practice: knowing an algorithm is not the same as being able to engineer a reliable system from it. You already have the mathematical and programming prerequisites to read search procedures, probability models, and learning rules. Our work this semester is to close the gap between those formal descriptions and software that remains correct under unfamiliar inputs, hidden tests, performance constraints, and changing requirements. The central object of evaluation will therefore not be a clever demonstration that works once. It will be an implementation whose assumptions are explicit, whose invariants are preserved, whose failure behavior is deliberate, and whose evidence of correctness can survive independent testing. That shift in mindset connects every module in the course, from classical search through reinforcement learning and responsible machine-learning deployment.

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the six objectives in order and connect each one to professional practice.

These objectives define the working contract for today's lesson. First, you should be able to separate a mathematical or conceptual claim from the additional evidence required of an engineered artifact. Second, you should be able to look at pseudocode and identify concrete representations, invariants, and tests rather than immediately typing a literal translation. Third, you should understand why an autograder's hidden cases and time limits are not arbitrary obstacles; they approximate independent production verification. Fourth, you should be able to reason about failure semantics, especially the difference between rejecting invalid input immediately and returning a safe degraded result. Fifth, you should be able to classify acceptable and unacceptable uses of generative AI under this course's learning policy. Finally, you should understand the progression of the semester well enough to allocate practice time before integration projects and exams. These are application objectives. Merely repeating definitions will not demonstrate them.

## Slide 3 - The unit of success changes in an engineering course

**Suggested pacing:** 3 minutes
**Visual cue:** Contrast the large claim with the evidence panel before discussing the bullets.

In a theory-centered setting, success may be a proof that A-star is optimal under an admissible or consistent heuristic, or a derivation showing that a learning update is unbiased under specified assumptions. Those claims matter here, but they do not finish the engineering task. Code introduces representation choices, interfaces, mutation, numerical limits, exceptions, and resource constraints. A state that is mathematically well defined may be represented by a mutable list that cannot safely enter an explored set. An update equation may be correct on paper while a NumPy broadcast silently computes the wrong tensor. Engineering success therefore requires evidence at several levels: a clear behavioral contract, an implementation that preserves the relevant invariants, tests that would expose plausible faults, and performance measurements that show the design remains usable at the intended scale. The key shift is from believing an example to constructing independent evidence.

## Slide 4 - Theory, implementation, and verification form one pipeline

**Suggested pacing:** 3 minutes
**Visual cue:** Move left to right: claim, construction, evidence.

Treat these columns as one pipeline rather than competing philosophies. Theory specifies the assumptions and the property we want. Implementation chooses concrete structures and operations that either preserve or violate those assumptions. Verification asks what observations would distinguish a faithful implementation from a plausible-looking defect. Consider breadth-first search. Theory tells us when it is complete and optimal. Implementation must decide how states are hashed, when they enter the explored set, and how parent pointers reconstruct a path. Verification must include cycles, duplicate frontier entries, an unreachable goal, and a start state that is already a goal. If any one column is missing, the result is weak. Theory without implementation is not a working system. Implementation without theory has no justified guarantee. Testing without a contract can only show that selected executions happened, not that they were the right executions.

## Slide 5 - Translate pseudocode through invariants, not line by line

**Suggested pacing:** 4 minutes
**Visual cue:** Trace the five stages and pause on Extract.

A literal line-by-line translation of pseudocode is tempting because pseudocode looks like code. The danger is that pseudocode deliberately omits representation and operational details. Begin by reading for the contract: what are the valid inputs, what must the output mean, and which assumptions support the guarantee? Then extract the invariants. In graph search, one invariant might state that every frontier node represents a discovered path and carries the correct accumulated cost for that path. Another might constrain when a state becomes closed. Representation follows from those invariants: a priority queue for cost order, immutable state keys for membership, and explicit parent references for reconstruction. Only then should implementation begin. The final stage challenges the translation with cases that target the invariant: duplicate discovery at a cheaper cost, an empty frontier, a malformed state, or a graph whose size exposes an inefficient membership test. This workflow scales beyond search to dynamic programming, Bayesian inference, gradient descent, and deployment monitoring.

## Slide 6 - Pseudocode leaves engineering decisions unresolved

**Suggested pacing:** 4 minutes
**Visual cue:** Point to REMOVE, membership, duplicate handling, and failure in that order.

This pseudocode communicates the common control structure of graph search, but it intentionally leaves several decisions open. REMOVE could mean FIFO order, LIFO order, or minimum priority; that single choice changes the algorithm and its guarantees. Membership in an explored set assumes states have stable equality and hashing semantics. The phrase not in the frontier hides an efficiency question: will the implementation scan a list, maintain an auxiliary set, or support a decrease-key operation? Uniform-cost search and A-star also need a policy for a state rediscovered through a cheaper path. Finally, failure must have an unambiguous representation that cannot be confused with a valid empty path. A production translation should make these decisions explicit in interfaces and tests. The lesson is not that pseudocode is deficient. Its abstraction is useful. Engineering begins precisely where the abstraction stops specifying operational behavior.

## Slide 7 - Correctness is a conjunction, not a screenshot

**Suggested pacing:** 3 minutes
**Visual cue:** Read the conjunction aloud and define each term.

This expression is not a formal theorem, but it is a useful engineering checklist. The contract states what callers may provide and what they may observe. An invariant explains why intermediate operations remain meaningful. A termination argument explains why the computation reaches an allowed outcome rather than looping, exhausting memory, or waiting indefinitely. A screenshot of a path or a high accuracy number may be evidence that one execution finished, but it does not establish the contract on other inputs, invariant preservation during execution, or bounded behavior under stress. In later modules, the same conjunction will take different forms. For value iteration, we will connect updates to a Bellman operator and a convergence threshold. For gradient descent, we will monitor shapes, numerical values, and stopping criteria. For deployed models, the contract includes data schemas, metric definitions, and monitoring responses. The discipline remains stable even as the algorithms change.

## Slide 8 - An autograder is an independent executable specification

**Suggested pacing:** 3 minutes
**Visual cue:** Emphasize that hidden does not mean arbitrary.

Students sometimes experience hidden tests as a negotiation with an unknown opponent. A better model is independent verification. Public tests reveal examples of the contract and help you establish a working feedback loop. Hidden tests then vary the input structure, edge conditions, and scale so that special-cased demonstrations do not masquerade as general solutions. Timeouts similarly make complexity visible. A breadth-first search that uses repeated linear membership scans may be logically correct on a tiny graph but fail the intended engineering requirement at scale. Deterministic tie-breaking and seeded randomness make these failures reproducible. A strong workflow does not guess the hidden inputs. It derives test partitions from the contract: minimum size, maximum practical size, empty or unreachable cases, duplicates, ties, invalid values, and performance boundaries. If your local tests represent those partitions, the hidden suite should feel like confirmation rather than surprise.

## Slide 9 - Public examples start the test design; they do not finish it

**Suggested pacing:** 3 minutes
**Visual cue:** Ask students which right-column case they would write first.

The left column is necessary because it establishes a shared interface and a known starting point. The right column is where engineering confidence grows. Boundary tests examine the smallest legal structures and deliberately malformed input. Structural tests introduce cycles, duplicate states, equal priorities, or disconnected components. Scale tests reveal whether a theoretically reasonable algorithm was paired with an unsuitable data structure. Repeated executions expose dependence on unordered iteration, ambient random state, or hidden mutation. Notice that these are not random tests. Each corresponds to a specific risk derived from the contract or implementation. Before submitting an assignment, you should be able to name the risk addressed by every test. Conversely, for every important invariant or failure mode, you should be able to point to at least one test designed to challenge it. That traceability is a professional habit we will practice throughout the semester.

## Slide 10 - A zero-length solution exposes a search-agent defect

**Suggested pacing:** 3 minutes
**Visual cue:** Let students predict the failure before revealing the regression test.

This case is intentionally small because small counterexamples are powerful. The theoretical search problem allows the initial state to be a goal. The correct solution is then the empty action sequence with total cost zero. An implementation that expands first may take an unnecessary action, return failure when no actions exist, or produce a nonminimal path. The fix is not only to move a condition in the code. We should state the behavior in the contract and add a regression test so later refactoring cannot silently reintroduce the defect. This example also shows why edge cases are not cosmetic. They often sit exactly at the boundary where an invariant is initialized. Similar patterns recur in dynamic programming with terminal states, in learning loops with zero examples, and in evaluation code with a class absent from a fold. Boundary behavior deserves explicit design.

## Slide 11 - Defensive programming makes assumptions executable

**Suggested pacing:** 3 minutes
**Visual cue:** Differentiate boundary validation from cluttering every internal line.

Defensive programming is not the indiscriminate addition of checks everywhere. Its purpose is to turn assumptions into observable behavior at the correct boundary. A public function that expects a rectangular numeric matrix should verify dimensionality, finiteness, and compatible labels before training begins. A search problem should reject an action not returned by its legal-action function rather than mutating into an impossible state. Once those preconditions are established, the trusted core can operate under a smaller, clearer set of assumptions. Failure messages should name the violated condition and relevant value. A vague index error ten stack frames later is not an adequate contract. Defensive design also includes postconditions when practical: output shapes, probability normalization within tolerance, or a reconstructed path whose transitions are legal. The goal is not to prevent every imaginable problem. It is to make the most consequential assumptions explicit, local, testable, and diagnosable.

## Slide 12 - Choose failure semantics from the system contract

**Suggested pacing:** 3 minutes
**Visual cue:** Stress that fail safely is not fail silently.

Fail fast and fail safely are both deliberate strategies; neither means ignoring a problem. Fail fast is appropriate when invalid developer input, inconsistent state, or a broken invariant makes continued computation misleading. A precise exception close to the boundary shortens diagnosis and protects the rest of the system. Fail safely is appropriate when the contract explicitly defines a degraded result, such as declining to recommend when confidence is insufficient or using a conservative default policy while emitting an alert. The dangerous pattern is fail silently: swallowing an exception, returning an undocumented value, or continuing with corrupted data. In this course, you should state the chosen failure behavior in the interface documentation and test it directly. When you design a fallback, also define how operators or callers learn that it occurred. Reliability requires both behavior and observability.

## Slide 13 - The AI-use policy protects the learning objective

**Suggested pacing:** 4 minutes
**Visual cue:** Use concrete examples; do not reduce the distinction to tool names.

The policy distinguishes the learning objective, not merely the tool. If the objective is to implement A-star, asking a model to generate that implementation replaces the practice being assessed. Asking for an explanation of a priority-queue exception can support debugging without supplying the algorithmic design. Syntax clarification and abstract conceptual discussion are similarly permitted, provided the resulting submission remains your own work and you follow any assignment-specific disclosure rule. Borderline cases should be judged by asking what cognitive work the assignment intends to measure. If the tool is making the representation, algorithm, invariant, or evaluation decision that you are supposed to demonstrate, stop and ask the instructor. Regardless of permission, you remain accountable for correctness. Generated explanations can be wrong, outdated, or mismatched to the contract. You must be able to explain, reproduce, and defend every submitted decision without relying on the tool's authority.

## Slide 14 - Policy checkpoint

**Suggested pacing:** 3 minutes
**Visual cue:** Pause for responses, then guide students to a conditional permitted answer.

A defensible answer is that the request can be permitted if the student has already authored the core BFS logic and uses the tool to understand a runtime symptom and improve testing. The student should not ask the system to rewrite the search loop or provide a submission-ready explored-set implementation. The learning objective is the student's ability to construct graph search correctly. Diagnosis of a timeout and discussion of test categories can support that objective rather than replace it. The student must still determine whether the explanation fits the actual code, add tests based on the course contract, and be able to explain the final fix. If an assignment imposes a stricter rule, that local rule controls. The general method is to identify what is being assessed, identify which reasoning the tool would perform, and preserve the assessed reasoning as the student's own work.

## Slide 15 - Three modules expand one engineering discipline

**Suggested pacing:** 3 minutes
**Visual cue:** Connect each module to the shared engineering habits.

Module A begins with explicit state spaces and rational agents. You will implement uninformed and informed search, then extend the reasoning to adversarial game trees. Module B adds sequential uncertainty through Markov decision processes, reinforcement learning, function approximation, and Bayesian belief. Module C shifts to predictive learning, where you will build regression and neural models from first principles, evaluate them rigorously, and confront bias and deployment responsibility. The integration weeks ask you to choose among these paradigms rather than treating them as isolated chapters. Across all modules, the recurring engineering questions remain stable: What is the contract? Which assumptions support the method? What invariant or diagnostic should hold? Which test would expose a violation? What evidence justifies deployment? Recognizing that continuity will make the course feel like one discipline rather than a list of algorithms.

## Slide 16 - Assessment rewards both repeated practice and integration

**Suggested pacing:** 3 minutes
**Visual cue:** Call out the documented 95% total without inventing the remaining allocation.

The published source prompt assigns 15 percent to weekly code labs and quizzes, 30 percent to the three module projects, 30 percent to the midterm category, and 20 percent to the comprehensive final. Those listed categories total 95 percent. This course package does not invent the missing allocation; the official syllabus must state the remaining 5 percent before grades are calculated. The important planning signal is still clear. Weekly practice provides fast feedback, projects require integration, and examinations ask you to reason without relying on a working codebase. Do not interpret the smaller weekly percentage as permission to skip practice. The projects and exams depend directly on the habits built there. Conversely, passing an autograder is not sufficient exam preparation. You must also trace algorithms, derive updates, compare guarantees, and explain failure modes in words and mathematics.

## Slide 17 - Passive familiarity will not survive an unfamiliar test

**Suggested pacing:** 2 minutes
**Visual cue:** End the main lesson with a concrete study routine.

A technical page can feel obvious after several readings because recognition is easy. The exam, project, and hidden test require retrieval and transfer. A more effective routine is active. First, trace the algorithm on a deliberately small case and record each state change. Second, implement from the contract rather than copying the trace. Third, design a case that should break a naive implementation. Fourth, explain the relevant guarantee and its assumptions without notes. Finally, compare your result with tests and revise the model of the problem, not only the code. This routine turns mistakes into information. It also distributes effort: short, frequent practice reduces the risk of discovering a conceptual gap during a module project. The course will be demanding, but the difficulty is structured. Each week supplies a smaller system, vocabulary, and evidence pattern that feeds the next integration task.

## Slide 18 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Summarize without introducing new terminology.

Four ideas should remain after this lesson. First, AI engineering is not theory with extra syntax. It is the discipline of carrying theoretical assumptions into executable contracts and observable evidence. Second, invariants are the bridge that helps us choose representations and tests rather than translating pseudocode mechanically. Third, an autograder is a form of independent verification that makes generality, complexity, determinism, and boundary behavior visible. Fourth, generative AI must support learning without performing the core reasoning that an assignment is designed to measure. These ideas will recur immediately in the next lesson, where we formalize rational agents, describe task environments with PEAS, and represent problem solving as search. As we introduce those abstractions, keep asking how each abstract component will become a data structure, interface, invariant, and test.

## Slide 19 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Use the questions as exit prompts or a short paired discussion.

Use these questions to test whether you can apply the lesson rather than repeat its vocabulary. For the first, identify a concrete implementation choice that can violate a theoretical assumption. For the second, make the invariant precise enough that a test can challenge it. For the timeout question, connect runtime behavior to data structures and scale. For failure semantics, state both the user-visible behavior and the monitoring evidence. For the policy question, explain which reasoning belongs to the student. A strong answer names the contract, the risk, and the evidence. If an answer remains at the level of a slogan such as test more or use AI responsibly, make it operational: what exactly should the code do, which case should be run, and what observation would distinguish correct behavior from a defect?

## Reference Notes

- Repository prompt: week_01/Week_1_Lesson_1_Course_Intro_and_AI_Engineering_Mindset.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition, Chapters 1-3.
- Python Software Foundation, Python 3 documentation: Errors and Exceptions; Data Model.
- Paul Ammann and Jeff Offutt, Introduction to Software Testing, 2nd edition.

**Approximate narration word count:** 2693
