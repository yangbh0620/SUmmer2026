# CMPSC 480 Notation Guide

This guide standardizes mathematical and implementation notation across all
lectures and assessments. A local definition on a slide may specialize a symbol,
but it must not silently reverse the meaning established here.

## General Conventions

- Scalars use italic lowercase letters: \(x\), \(y\), \(\alpha\), and
  \(\gamma\).
- Vectors use bold lowercase letters: \(\mathbf{x}\), \(\mathbf{w}\), and
  \(\mathbf{b}\).
- Matrices use bold uppercase letters: \(\mathbf{X}\) and \(\mathbf{W}\).
- Sets and spaces use calligraphic uppercase letters: \(\mathcal{S}\),
  \(\mathcal{A}\), and \(\mathcal{D}\).
- Random variables use uppercase letters; realized values use lowercase
  letters: \(X=x\).
- A hat denotes an estimate or prediction: \(\hat{y}\), \(\hat{Q}\).
- A superscript in parentheses denotes an example index:
  \(\mathbf{x}^{(i)}\). It is not an exponent.
- Subscripts denote components, time, layers, or conditioning context, as
  defined locally.
- \(\arg\min\) and \(\arg\max\) return an argument; \(\min\) and \(\max\)
  return a value.
- Logarithms are natural logarithms unless a different base is stated.
- Equality means exact mathematical equality. Approximate numerical equality is
  written with \(\approx\) and accompanied by a tolerance when implemented.

## Agents and Search

- \(s \in \mathcal{S}\): a state.
- \(s_0\): the initial state.
- \(G \subseteq \mathcal{S}\): the set of goal states.
- \(a \in \mathcal{A}(s)\): an action legal in state \(s\).
- \(T(s,a)\): the successor state or transition function in a deterministic
  problem.
- \(c(s,a,s')\): the step cost from \(s\) to \(s'\).
- \(g(n)\): accumulated path cost to search node \(n\).
- \(h(n)\): estimated remaining cost from node \(n\).
- \(f(n)=g(n)+h(n)\): the A-star priority.
- \(b\): branching factor; \(d\): shallowest solution depth; \(m\): maximum
  search depth.
- Frontier tie-breaking must be stated and deterministic in graded code.
- A search **state** describes the modeled world; a search **node** additionally
  stores path-dependent information such as parent, action, cost, and depth.

## Adversarial Search

- \(V(s)\): backed-up utility or evaluation of game state \(s\).
- \(U(s)\): exact terminal utility.
- \(\operatorname{Eval}(s)\): bounded heuristic evaluation for a cutoff state.
- MAX and MIN name the alternating decision makers in a zero-sum game.
- \(\alpha\): the best lower bound currently available to MAX.
- \(\beta\): the best upper bound currently available to MIN.
- In expectimax, \(P(s' \mid s,a)\) denotes the chance-node transition
  probability.

## Markov Decision Processes and Reinforcement Learning

An MDP is written as
\[
(\mathcal{S},\mathcal{A},P,R,\gamma).
\]

- \(P(s' \mid s,a)\): transition probability.
- \(R(s,a,s')\): immediate reward.
- \(\gamma \in [0,1)\): discount factor unless a finite-horizon exception is
  stated.
- \(\pi(a\mid s)\): stochastic policy; \(\pi(s)\) may denote a deterministic
  action.
- \(V^\pi(s)\): value of state \(s\) under policy \(\pi\).
- \(Q^\pi(s,a)\): value of taking \(a\) in \(s\), then following \(\pi\).
- The Bellman optimality relation is
  \[
  V^*(s)=\max_a \sum_{s'}P(s'\mid s,a)
  \left[R(s,a,s')+\gamma V^*(s')\right].
  \]
- A tabular Q-learning update is
  \[
  Q(s,a)\leftarrow Q(s,a)+\alpha
  \left[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\right].
  \]
- \(\alpha\) is a learning rate; \(\epsilon\) is the exploration probability in
  an epsilon-greedy policy.
- For a terminal transition, the bootstrap contribution is zero.
- A linear approximation uses
  \(Q(s,a;\mathbf{w})=\mathbf{w}^{\mathsf T}\boldsymbol{\phi}(s,a)\).

## Probability and Bayesian Networks

- \(P(X=x)\): marginal probability.
- \(P(X=x\mid Y=y)\): conditional probability.
- \(\mathbf{e}\): observed evidence assignment.
- \(\mathbf{H}\): hidden variables to marginalize.
- A Bayesian network factorizes a joint distribution as
  \[
  P(X_1,\ldots,X_n)=\prod_{i=1}^{n}P(X_i\mid
  \operatorname{Pa}(X_i)).
  \]
- A factor is written \(\phi(\mathbf{X})\); factor multiplication aligns shared
  variable assignments.
- Variable elimination order affects computational cost but not the exact
  normalized result.
- A zero normalization constant is an impossible-evidence condition and must be
  reported rather than divided through.

## Regression and Optimization

- \(\mathbf{X}\in\mathbb{R}^{m\times d}\): design matrix with examples in rows.
- \(\mathbf{y}\in\mathbb{R}^{m}\): target vector.
- \(\mathbf{w}\in\mathbb{R}^{d}\): parameter vector.
- \(\hat{\mathbf{y}}=\mathbf{Xw}\): linear predictions.
- The course commonly uses
  \[
  J(\mathbf{w})=\frac{1}{2m}
  \lVert\mathbf{Xw}-\mathbf{y}\rVert_2^2,
  \qquad
  \nabla J=\frac{1}{m}\mathbf{X}^{\mathsf T}
  (\mathbf{Xw}-\mathbf{y}).
  \]
- If mean squared error without the factor \(1/2\) is used, the changed gradient
  scale must be stated explicitly.
- A gradient-descent step is
  \(\mathbf{w}\leftarrow\mathbf{w}-\eta\nabla J(\mathbf{w})\).
- \(\eta>0\) denotes the optimization learning rate.
- Feature normalization statistics are fitted on training data and reused
  unchanged on validation and test data.

## Neural Networks and Classification

- Layer \(l\) uses
  \[
  \mathbf{z}^{[l]}=\mathbf{W}^{[l]}\mathbf{a}^{[l-1]}
  +\mathbf{b}^{[l]},
  \qquad
  \mathbf{a}^{[l]}=g^{[l]}(\mathbf{z}^{[l]}).
  \]
- \(\mathbf{a}^{[0]}=\mathbf{x}\).
- \(\delta^{[l]}\) denotes the backpropagated preactivation derivative at layer
  \(l\).
- The logistic sigmoid is
  \(\sigma(z)=1/(1+\exp(-z))\).
- Binary cross-entropy for probability \(p\) and label \(y\in\{0,1\}\) is
  \[
  -y\log p-(1-y)\log(1-p).
  \]
- Softmax converts class logits \(\mathbf{z}\) into normalized probabilities.
  A numerically stable implementation subtracts \(\max_j z_j\) before
  exponentiation.
- \(\lambda\ge 0\) denotes regularization strength. Unless stated otherwise,
  intercept parameters are not regularized.

## Evaluation and Fairness

For binary classification:

- TP: true positives; FP: false positives.
- TN: true negatives; FN: false negatives.
- Precision \(=\mathrm{TP}/(\mathrm{TP}+\mathrm{FP})\).
- Recall or true-positive rate
  \(=\mathrm{TP}/(\mathrm{TP}+\mathrm{FN})\).
- False-positive rate
  \(=\mathrm{FP}/(\mathrm{FP}+\mathrm{TN})\).
- \(F_1=2PR/(P+R)\), where \(P\) is precision and \(R\) is recall.
- A zero denominator follows the explicitly declared convention in the
  question, code contract, or reporting standard; it must never fail silently.

For a protected or operational group \(g\):

- Group-conditioned rates carry a subscript, such as
  \(\mathrm{TPR}_g\) and \(\mathrm{FPR}_g\).
- A disparity gap is reported with its direction and convention, for example
  \(\mathrm{TPR}_{g_1}-\mathrm{TPR}_{g_2}\).
- Demographic parity, equal opportunity, and equalized odds are distinct
  criteria. A report must name the selected criterion and justify why it fits
  the deployment context.

## Implementation Conventions

- Arrays use examples in rows unless a document states otherwise.
- Shapes are part of the contract and should be asserted at public boundaries.
- Floating-point comparisons use a documented absolute or relative tolerance.
- Randomized procedures expose and record seeds.
- Invalid inputs raise a documented exception; impossible probabilistic events
  use an explicit failure convention.
- Ties use a stated deterministic rule.
- Every reported metric names its split, aggregation rule, and denominator.
