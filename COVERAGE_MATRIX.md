# CMPSC 480 Coverage Matrix

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

## Weekly Instruction and Assessment Alignment

| Week | Lecture coverage | Weekly assessed artifact | Quiz | Midterm | Final | Outcomes |
|---:|---|---|---|:---:|:---:|---|
| 1 | AI engineering mindset; pseudocode-to-Python contracts; defensive programming; rational agents; PEAS; state-space formulation | Environment, immutable state, problem interface, agent contract, and tests | Quiz 1 | Yes | Yes | LO1, LO2 |
| 2 | Tree versus graph search; BFS; DFS; UCS; Greedy Best-First Search; A-star; admissibility; consistency | Unified search implementation, traces, and heuristic defenses | Quiz 1 | Yes | Yes | LO1, LO2 |
| 3 | Game trees; minimax; alpha-beta pruning; expectimax; evaluation functions | Module Project A: search-based game agent | Quiz 2 | Yes | Yes | LO1, LO2, LO6 |
| 4 | MDP components; transition and reward models; Bellman equations; value iteration; policy iteration | Validated gridworld planning implementation | Quiz 2 | Yes | Yes | LO1, LO2, LO3 |
| 5 | Model-free learning; exploration-exploitation; temporal-difference learning; tabular Q-learning | Q-learning update, policy, terminal handling, and training evidence | Quiz 2 | Yes | Yes | LO2, LO3 |
| 6 | Linear value-function approximation; feature design; neural Q approximators; replay; target networks | Approximate Q-learning and feature-ablation evidence | Quiz 3 | Yes | Yes | LO2, LO3 |
| 7 | Joint and conditional probability; Bayes' rule; Bayesian-network structure; variable elimination; sampling | Module Project B: stochastic control and Bayesian belief updates | Quiz 3 | Yes | Yes | LO3, LO6 |
| 8 | Linear regression; mean squared error; normal equation; batch gradient descent; vectorization | Raw-NumPy regression pipeline and convergence study | Quiz 3 | No | Yes | LO4 |
| 9 | Perceptrons; activations; feedforward dimensions; chain rule; backpropagation; gradient checking | Neural network and backpropagation from scratch | Quiz 3 | No | Yes | LO4 |
| 10 | Logistic regression; sigmoid and softmax; cross-entropy; bias-variance; L1/L2 regularization; data splits | Classifier, regularization experiment, and protected test set | Quiz 4 | No | Yes | LO4, LO5 |
| 11 | Confusion matrix; precision; recall; F1; ROC-AUC; cross-validation; grid/random search; learning curves | Evaluation tooling, tuning ledger, and single final-test evaluation | Quiz 4 | No | Yes | LO5 |
| 12 | Sources of bias; group metrics; fairness criteria; model cards; audits; deployment controls | Module Project C: classifier fairness audit and mitigation | Quiz 5 | No | Yes | LO4, LO5 |
| 13 | Cross-module method selection; interface contracts; cumulative derivation review; debugging | Minimal repairs across Modules A, B, and C with regression tests | Quiz 5 | No | Yes | LO2, LO4, LO6 |
| 14 | Final-project scope; architecture; baseline; evaluation plan; risks; walking skeleton | Proposal and feasibility checkpoint | No | No | Yes | LO5, LO6 |
| 15 | Reproducible showcase; evidence chain; limitations; responsibility; course synthesis | Final integrated project, report, tests, evidence, and showcase | No | No | Yes | LO1-LO6 |

## Required Topic Coverage

| Required topic | Taught in | Practiced in | Summative assessment |
|---|---|---|---|
| Rational agents, PEAS, and search formulation | Week 1 | Weeks 1-2 assignments | Midterm Task 1; Final Task 1 |
| BFS, DFS, UCS, and A-star | Week 2 | Week 2 assignment; Module Project A | Midterm Task 2; Final Task 1 |
| Minimax, alpha-beta, and expectimax | Week 3 | Module Project A; Quiz 2 | Midterm Task 3; Final Task 2 |
| MDP formulation and Bellman reasoning | Week 4 | Week 4 assignment; Quiz 2 | Midterm Task 4; Final Task 3 |
| Reinforcement learning and Q-learning | Weeks 5-6 | Weeks 5-6 assignments; Module Project B | Midterm Task 5; Final Task 3 |
| Bayesian networks and inference | Week 7 | Module Project B; Quiz 3 | Midterm Task 6; Final Task 4 |
| Linear regression and gradient descent | Week 8 | Week 8 assignment; Quiz 3 | Final Task 5 |
| Neural networks and backpropagation | Week 9 | Week 9 assignment; Quiz 3 | Final Task 6 |
| Classification and regularization | Week 10 | Week 10 assignment; Quiz 4 | Final Task 7 |
| Evaluation metrics and tuning | Week 11 | Week 11 assignment; Quiz 4 | Final Task 8 |
| Bias and fairness | Week 12 | Module Project C; Quiz 5 | Final Task 9 |
| Responsible deployment | Week 12 | Module Project C; final project | Final Tasks 9-10 |
| Cross-module integration and debugging | Weeks 13-15 | Weeks 13-15 assignments | Midterm Task 7; Final Task 10 |

## Objective-to-Assessment Trace

| Outcome | Direct instructional evidence | Direct assessment evidence |
|---|---|---|
| LO1 | Agent, search, MDP, and project-formulation lectures | Weeks 1-4 assignments; Midterm Tasks 1 and 4; Final Tasks 1 and 10 |
| LO2 | Search, games, planning, RL, and debugging lectures | Weeks 2-6 and 13 assignments; Quizzes 1-2; Midterm Tasks 2-5; Final Tasks 1-3 |
| LO3 | RL, approximation, probability, and Bayesian-network lectures | Weeks 5-7 assignments; Quiz 3; Midterm Tasks 5-6; Final Tasks 3-4 |
| LO4 | Regression, neural-network, classification, and debugging lectures | Weeks 8-10 and 13 assignments; Quizzes 3-4; Final Tasks 5-7 |
| LO5 | Evaluation, tuning, fairness, and deployment lectures | Weeks 10-12 and 14 assignments; Quizzes 4-5; Final Tasks 8-9 |
| LO6 | Module projects, integration review, and final-project lectures | Module Projects A-C; Weeks 13-15 assignments; Midterm Task 7; Final Task 10 |

## Sequencing Checks

- No assessment requires a topic before its first instructional week.
- The midterm is limited to Weeks 1-7.
- The comprehensive final samples every required technical topic and includes a
  dedicated cross-module integration task.
- Module C receives six dedicated final-exam tasks when regression, neural
  networks, classification, evaluation, fairness, and integration are counted.
- The final project requires methods from at least two modules and an explicit
  interface, baseline, evaluation plan, limitations statement, and operational
  owner.
