# CMPSC 480 Assessment Blueprint

## Purpose

The assessment system measures whether students can translate AI models and
pseudocode into correct, defensively programmed implementations; analyze formal
properties; evaluate evidence; and make responsible engineering decisions.
Recall-only questions are subordinate to tracing, derivation, debugging,
experimental design, and synthesis.

## Course Learning Outcomes

- **LO1 - Formalization:** Represent an AI task using states, actions,
  objectives, uncertainty, assumptions, and failure semantics.
- **LO2 - Algorithms:** Trace, implement, and compare search, planning, and
  learning algorithms.
- **LO3 - Uncertainty:** Compute and interpret probabilistic, Bayesian, and
  reinforcement-learning updates.
- **LO4 - Machine learning:** Implement regression, neural networks, and
  classification from first principles.
- **LO5 - Evaluation and responsibility:** Select metrics, prevent leakage,
  diagnose bias, and design monitoring and mitigation.
- **LO6 - Integration:** Connect methods across modules through explicit
  interfaces, tests, and evidence.

## Assessment Design Rules

- Every scored task and subtask has an explicit point value.
- Student and instructor decks are independent documents.
- Every student subtask has a matched solution entry with the same identifier
  and points.
- Programming work requires reproducibility, validation, edge cases, tests, and
  a short evidence-based reflection.
- Model selection occurs without test-set access; the final test set is used
  once after decisions are locked.
- Fairness questions require a declared metric convention and deployment
  context rather than a universal claim.
- Rubrics award reasoning and evidence, not only final numeric output.

## Weekly Assignment Blueprint

| Week | Points | Principal evidence | Primary outcomes |
|---:|---:|---|---|
| 1 | 10 | Environment verification, immutable state and agent contracts, tests | LO1, LO2 |
| 2 | 10 | Unified BFS, DFS, UCS, and A-star implementation with traces | LO1, LO2 |
| 3 | 20 | Module Project A: search-based game agent and comparative evidence | LO1, LO2, LO6 |
| 4 | 10 | Value and policy iteration on a validated gridworld MDP | LO1, LO2, LO3 |
| 5 | 10 | Tabular Q-learning with terminal and exploration defenses | LO2, LO3 |
| 6 | 10 | Approximate Q-learning with explicit features and update tests | LO2, LO3 |
| 7 | 20 | Module Project B: stochastic control with Bayesian belief updates | LO3, LO6 |
| 8 | 10 | Vectorized linear regression and gradient-descent convergence | LO4 |
| 9 | 10 | Feedforward network, backpropagation, and numerical gradient checks | LO4 |
| 10 | 10 | Logistic regression, regularization, and protected evaluation split | LO4, LO5 |
| 11 | 10 | Metrics, cross-validation, tuning ledger, and final-test discipline | LO5 |
| 12 | 20 | Module Project C: classifier fairness audit and mitigation experiment | LO4, LO5 |
| 13 | 10 | Cross-module debugging with minimal repairs and regression tests | LO2, LO4, LO6 |
| 14 | 10 | Final-project proposal, risk plan, baseline, and walking skeleton | LO5, LO6 |
| 15 | 100 | Final integrated system, report, tests, evidence, and showcase | LO1-LO6 |

Weeks 3, 7, and 12 use the indexed module projects as their weekly
assignments. Week 15 is the summative final-project submission.

## Quiz Blueprint

Each quiz is a 20-point, short-form assessment. Questions mix hand computation,
algorithm tracing, shape reasoning, and concise engineering judgment.

| Quiz | Administered | Coverage | Primary outcomes |
|---:|---:|---|---|
| 1 | Week 2 | Agents, problem formulation, BFS, DFS, UCS, A-star | LO1, LO2 |
| 2 | Week 5 | Minimax, alpha-beta, MDP planning, Q-learning | LO2, LO3 |
| 3 | Week 9 | Approximation, Bayesian updates, regression, neural-network shapes | LO3, LO4 |
| 4 | Week 11 | Cross-entropy, regularization, learning curves, confusion metrics | LO4, LO5 |
| 5 | Week 13 | Fairness metrics, criterion choice, monitoring, integration | LO5, LO6 |

## Midterm Blueprint

- **Coverage:** Weeks 1-7
- **Duration:** 110 minutes
- **Total:** 100 points
- **Permitted materials:** As stated in the student question deck
- **Balance:** Module A foundations and Module B probabilistic reasoning, with
  an integrative engineering problem

| Task | Topic | Points | Cognitive demand |
|---:|---|---:|---|
| 1 | Agent and search formulation | 10 | Formalize and justify |
| 2 | UCS and A-star | 15 | Trace and analyze guarantees |
| 3 | Minimax and alpha-beta | 15 | Back up values and prune safely |
| 4 | MDP planning | 15 | Apply Bellman reasoning |
| 5 | Q-learning and approximation | 15 | Compute updates and diagnose design |
| 6 | Bayesian networks and inference | 15 | Factorize and infer |
| 7 | Integrated engineering scenario | 15 | Compare and combine methods |

The midterm uses 21 scored subquestions. The instructor deck provides a matched
worked solution and grading guidance for every subquestion.

## Comprehensive Final Blueprint

- **Coverage:** Weeks 1-15
- **Duration:** 180 minutes
- **Total:** 150 points
- **Permitted materials:** As stated in the student question deck
- **Balance:** Representative coverage of all three modules, with meaningful
  emphasis on Module C and cross-module integration

| Task | Topic | Points | Cognitive demand |
|---:|---|---:|---|
| 1 | Search and heuristic guarantees | 15 | Analyze correctness and counterexamples |
| 2 | Adversarial reasoning | 15 | Trace values and compare assumptions |
| 3 | MDPs and reinforcement learning | 15 | Derive and compute |
| 4 | Bayesian inference | 15 | Factorize, eliminate, and interpret |
| 5 | Regression and gradient descent | 15 | Derive, vectorize, and diagnose |
| 6 | Neural networks and backpropagation | 15 | Track shapes and gradients |
| 7 | Classification and regularization | 15 | Compute and justify controls |
| 8 | Evaluation and tuning | 15 | Select evidence without leakage |
| 9 | Fairness and responsible deployment | 15 | Measure, qualify, and govern |
| 10 | Cross-module integration | 15 | Design a defensible system handoff |

The final uses 30 scored subquestions. The instructor deck provides a matched
worked solution and grading guidance for every subquestion.

## Evidence and Grading

Full-credit evidence may include:

- a correct derivation with declared assumptions;
- an algorithm trace whose intermediate state is visible;
- pseudocode or code with stated shape, type, and failure contracts;
- a counterexample that distinguishes two methods;
- a controlled experiment with a baseline and held-out evaluation;
- a fairness or risk conclusion bounded by the chosen metric and data; and
- reproducible commands, tests, configurations, and seeds.

Common deductions target incorrect assumptions, hidden state mutation, test-set
leakage, unmatched dimensions, unstable arithmetic, ambiguous tie-breaking,
unsupported deployment claims, and missing failure handling.
