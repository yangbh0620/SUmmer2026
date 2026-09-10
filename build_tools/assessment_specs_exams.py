"""Midterm and comprehensive final specifications for CMPSC 480."""


def p(label, points, question, answer):
    return {"label": label, "points": points, "question": question, "answer": answer}


def q(pid, title, points, prompt, deliverable, grading, parts):
    return {
        "id": pid, "title": title, "points": points, "prompt": prompt,
        "deliverable": deliverable, "grading": grading, "parts": parts,
    }


EXAM_RULES = [
    "Work independently and show intermediate algebra, frontier state, or factor state.",
    "One double-sided handwritten letter-size reference sheet is permitted.",
    "A nonprogrammable calculator is permitted; networked devices and communication are prohibited.",
    "State every tie-breaking, terminal, reward, and zero-division convention you use.",
    "Answers receive credit for justified reasoning; an unsupported final number may receive little credit.",
    "Academic integrity rules of the course and institution apply throughout the examination.",
]


def exam(title, subtitle, short, coverage, duration, points, objectives, problems,
         edge_cases, edge_solutions, reflection, reflection_answer):
    return {
        "title": title, "subtitle": subtitle, "short_title": short,
        "overview": "Solve applied, mathematical, algorithmic, and engineering problems under explicit assumptions.",
        "coverage": coverage, "duration": duration,
        "submission": "Individual examination PDF", "total_points": points,
        "objectives": objectives, "requirements": EXAM_RULES,
        "problems": problems,
        "edge_cases": edge_cases, "edge_solutions": edge_solutions,
        "submission_steps": [
            "Write your name and identify every requested problem and subpart.",
            "Show enough intermediate work that another reader can audit the result.",
            "Submit the complete question-response document when time is called.",
        ],
        "reflection_length": "one or two sentences",
        "reflection": reflection,
        "reflection_answer": reflection_answer,
        "style_path": "../../shared/cmpsc480_beamer.tex",
    }


SPECS = {}

SPECS["midterm"] = exam(
    "CMPSC 480 Midterm Examination",
    "Cumulative assessment of Weeks 1-7",
    "Midterm",
    "Modules A and B: agents, search, adversarial reasoning, MDPs, RL, approximation, and Bayesian inference",
    "110 minutes", 100,
    [
        "Formulate agent and search problems precisely.",
        "Trace cost-sensitive and adversarial algorithms.",
        "Apply Bellman and temporal-difference updates.",
        "Reason about function approximation stability.",
        "Compute Bayesian posteriors and factor operations.",
        "Integrate methods while preserving assumptions.",
    ],
    [
        q(1, "Agent and search formulation", 10,
          "A delivery robot operates in a partially mapped building with battery limits and moving people.",
          "PEAS analysis, search model, and engineering contract.",
          "Components are precise and connected to observable behavior.",
          [
              p("a", 3, "Give one concrete element for each PEAS component.", "Performance includes timely collision-free delivery and battery use; environment includes corridors, doors, people, and stations; actuators include motion and lift commands; sensors include localization, range sensing, battery, and task messages."),
              p("b", 3, "Define states, actions, transition model, goal test, and path cost for deterministic route planning.", "A state contains position and other path-relevant discrete facts such as carried item or battery bucket; actions are legal moves or task operations; transition applies one action; goal checks delivery completion; cost can combine time and energy with nonnegative units."),
              p("c", 4, "Explain why rational behavior does not imply omniscience and name two defensive interface checks.", "Rationality maximizes expected performance using the available percept history and knowledge, so uncertainty can still produce failure. Checks include immutable state keys, legal successor validation, positive costs for UCS/A-star, deterministic ties, and explicit failure."),
          ]),
        q(2, "UCS and A-star", 15,
          "Graph edges are S-A:4, S-B:1, B-A:1, A-G:3, and B-G:8. Heuristic values are h(S)=5, h(A)=3, h(B)=4, h(G)=0.",
          "Priority trace, optimal path, and heuristic argument.",
          "Costs, updates, and guarantee conditions are correct.",
          [
              p("a", 5, "Trace UCS until a goal is removed, including cheaper rediscovery.", "Remove S(0), insert A(4),B(1); remove B(1), improve A to 2 and insert G(9); remove A(2), improve G to 5; remove G(5). Return S-B-A-G with cost 5."),
              p("b", 5, "Trace A-star priorities and return the selected path.", "After S, A has f=7 and B f=5; remove B, improved A has g=2,f=5 and G has f=9; remove A, improve G to g=f=5; remove G and return cost 5."),
              p("c", 5, "Is the heuristic admissible and consistent? Justify from the graph.", "True remaining costs are h-star(G)=0, h-star(A)=3, h-star(B)=4 via A, and h-star(S)=5 via B-A. The listed h equals these values, so it is admissible. Each edge satisfies h(n)<=c+h(n-prime), including S-B:5<=1+4 and B-A:4<=1+3, so it is consistent."),
          ]),
        q(3, "Minimax and alpha-beta", 15,
          "A MAX root has MIN children A, B, and C. Their leaves in search order are A:[6,4], B:[3,8], C:[5,2].",
          "Minimax backups, pruning trace, and evaluation design.",
          "Values, bounds, pruning, and perspective are correct.",
          [
              p("a", 5, "Compute every minimax value and the selected action.", "MIN(A)=4, MIN(B)=3, and MIN(C)=2. MAX chooses A with root value 4."),
              p("b", 5, "Trace alpha-beta left to right and identify pruned leaves.", "After A, root alpha=4. At B, first leaf gives beta=3, so alpha>=beta and leaf 8 is pruned. At C, first leaf 5 does not prune because beta=5; second leaf gives 2. The root still chooses A."),
              p("c", 5, "Design a depth-cutoff evaluation with three features and state two tests.", "A valid MAX-perspective weighted sum might use score difference, mobility difference, and threat or distance advantage with normalized scales. Test terminal states bypass the heuristic and alpha-beta returns the same value as plain minimax on generated small trees."),
          ]),
        q(4, "MDP planning", 15,
          "At state s, action a reaches terminal reward 5 with probability 0.8 and state t with reward 0 and probability 0.2. Let gamma=0.9 and V(t)=2. Action b deterministically yields reward 3 and terminates.",
          "Bellman values, policy choice, and convergence reasoning.",
          "Expectations, terminal convention, and contraction logic are sound.",
          [
              p("a", 5, "Compute Q(s,a) under reward-on-transition semantics.", "Q(s,a)=0.8[5+0]+0.2[0+0.9(2)]=4+0.36=4.36."),
              p("b", 5, "Compute Q(s,b) and the greedy action.", "Q(s,b)=3 because the transition terminates and has no bootstrap. Since 4.36>3, choose a."),
              p("c", 5, "Explain why value iteration converges for a finite discounted MDP.", "The Bellman optimality operator changes values by at most gamma times the previous max-norm difference: expectation and maximum do not enlarge the bound beyond gamma. Since gamma<1, it is a contraction with a unique fixed point."),
          ]),
        q(5, "Q-learning and approximation", 15,
          "A linear agent has w=[0.5,-0.5], f(s,a)=[1,2], reward 2, gamma=0.5, max next Q=3, and alpha=0.2.",
          "Semi-gradient update, terminal change, and stability analysis.",
          "Arithmetic and deadly-triad reasoning are precise.",
          [
              p("a", 5, "Compute current Q, target, TD error, and new weights.", "Current Q=0.5-1=-0.5. Target=2+0.5(3)=3.5; delta=4. Increment=0.2(4)[1,2]=[0.8,1.6], so new w=[1.3,1.1]."),
              p("b", 5, "Recompute the update if the transition is terminal.", "Target=2, delta=2-(-0.5)=2.5, increment=0.2(2.5)[1,2]=[0.5,1], and new w=[1,0.5]."),
              p("c", 5, "Name the deadly triad and two observable instability signals.", "The triad is function approximation, bootstrapping, and off-policy learning. Signals include exploding weight or Q norms, increasing absolute TD-error quantiles, nonfinite values, oscillatory loss or return, and large cross-seed variance."),
          ]),
        q(6, "Bayesian networks and inference", 15,
          "R is a binary root with P(R)=0.2. S depends on R with P(S|R)=0.1 and P(S|not R)=0.5. W depends on both with P(W|R,S)=0.99 and P(W|R,not S)=0.8.",
          "Joint probability, posterior structure, and factor operation.",
          "CPT selection, normalization plan, and factor scope are correct.",
          [
              p("a", 5, "Compute P(R,S,W) for all three true.", "Use the factorization P(R)P(S|R)P(W|R,S)=0.2(0.1)(0.99)=0.0198."),
              p("b", 5, "Write an exact expression for P(R|W) without evaluating missing CPT rows.", "P(R|W) is proportional to P(R) sum_s P(s|R)P(W|R,s); compute that mass for R=true and false using their CPT rows, then normalize the two masses."),
              p("c", 5, "If factors f(R,S) and g(S,W) are multiplied and S is summed out, what is the result scope and why can order matter?", "The product scope is {R,S,W}; summing S yields a factor over {R,W}. Different elimination orders can create intermediate factors over more variables and therefore require exponentially more space and arithmetic."),
          ]),
        q(7, "Integrated engineering scenario", 15,
          "A robot uses a Bayesian belief over hazards as features for a linear Q-learning policy.",
          "Interface, ablation, and safety verification plan.",
          "The answer connects inference, learning, evaluation, and defensive controls.",
          [
              p("a", 5, "Specify the belief-to-policy interface and three invariants.", "Pass a fixed-order normalized finite belief vector, optionally with observable state features, never the hidden truth. Invariants include correct dimension, nonnegative entries summing to one, and legal-action-only output."),
              p("b", 5, "Design a controlled ablation showing whether belief tracking helps.", "Compare the full agent with a fixed-prior or observation-only agent using identical training steps, seeds, environment cases, and epsilon-zero evaluation; report return, success, hazard rate, and variability."),
              p("c", 5, "State a response to impossible evidence and a posttraining safety gate.", "Raise or apply a declared fallback posterior when normalization is zero. Before acceptance, require belief oracle tests, terminal-update tests, finite Q/weight limits, and hazard-rate performance across noise levels."),
          ]),
    ],
    ["A start state is already a goal.", "All minimax root actions tie.", "A terminal RL transition has a large next Q.", "Bayesian evidence has zero probability.", "A factor order creates an unexpectedly large table."],
    ["Return an empty path.", "Use stable action order.", "Ignore the bootstrap.", "Raise or use the declared fallback.", "Choose a lower-growth elimination order and report maximum factor scope."],
    "Identify one assumption that changed the answer to a problem.",
    "A full-credit response names the problem, states the assumption, and explains the exact trace, equation, or guarantee affected.",
)

SPECS["final_exam"] = exam(
    "CMPSC 480 Comprehensive Final Examination",
    "Weeks 1-15: methods, evidence, integration, and responsibility",
    "Final Examination",
    "All modules with emphasis on machine learning, evaluation, fairness, deployment, and cross-module integration",
    "180 minutes", 150,
    [
        "Compare and apply classical and adversarial search.",
        "Reason about stochastic planning and reinforcement learning.",
        "Perform Bayesian exact-inference operations.",
        "Derive regression, classification, and backpropagation updates.",
        "Design valid evaluation and hyperparameter protocols.",
        "Analyze fairness and responsible deployment decisions.",
        "Integrate methods through testable engineering contracts.",
    ],
    [
        q(1, "Search and heuristic guarantees", 15,
          "A* runs on a positive-cost graph with a heuristic that is admissible but not consistent.",
          "Guarantee analysis, implementation rule, and counterexample reasoning.",
          "The answer distinguishes tree search, graph search, reopening, and evidence.",
          [
              p("a", 5, "State admissibility and consistency formally.", "Admissibility requires h(n)<=h-star(n). Consistency requires h(n)<=c(n,n-prime)+h(n-prime) for every edge and h(goal)=0."),
              p("b", 5, "Can graph-search A* remain optimal with this heuristic? State the needed implementation behavior.", "Yes with admissibility if nodes can be reopened when a cheaper g is found and the algorithm uses a correct termination condition. A closed-set implementation that never reopens can return suboptimal paths under inconsistency."),
              p("c", 5, "Design a test that exposes missing reopening.", "Create a graph where a state is first expanded through a worse route due to low f, then reached more cheaply later; verify A* with reopening matches UCS optimal cost while the defective closed implementation does not."),
          ]),
        q(2, "Adversarial reasoning", 15,
          "A stochastic game node chooses action A with outcomes 8 and 0 at probabilities 0.25 and 0.75, or action B with guaranteed value 3.",
          "Expectimax calculation, minimax contrast, and engineering test.",
          "Utilities, probability semantics, and method choice are correct.",
          [
              p("a", 5, "Compute expectimax values and choose an action.", "A has expected value 0.25(8)+0.75(0)=2; B has value 3, so expectimax chooses B."),
              p("b", 5, "What would a worst-case MIN interpretation choose for A, and why is that a different model?", "MIN assigns A the value min(8,0)=0. It models an adversary selecting the outcome, not an exogenous random event with known probabilities."),
              p("c", 5, "Give two tests for a combined minimax-expectimax implementation.", "Use probabilities summing to one with a hand-computed chance node, and use a deterministic probability-one outcome that must equal the corresponding child. Also verify terminal utility and stable action ties."),
          ]),
        q(3, "MDPs and reinforcement learning", 15,
          "For Q(s,a)=2, reward=-1, gamma=0.9, max-next-Q=5, and alpha=0.1, compare one Q-learning update with a Bellman optimality backup.",
          "Numeric update and planning-learning comparison.",
          "Target, update, model requirements, and exploration are correct.",
          [
              p("a", 5, "Compute the Q-learning target, TD error, and updated Q.", "Target=-1+0.9(5)=3.5; delta=1.5; new Q=2+0.1(1.5)=2.15."),
              p("b", 5, "How would the terminal case differ?", "The target is immediate reward -1, delta=-3, and new Q=2-0.3=1.7."),
              p("c", 5, "Compare information required by value iteration and Q-learning.", "Value iteration needs explicit transition probabilities and rewards and performs expected backups over successors. Q-learning uses sampled transitions without the model but needs exploration and sufficient experience; it learns off-policy toward a greedy target."),
          ]),
        q(4, "Bayesian inference", 15,
          "A disease prior is 0.02, test sensitivity is 0.9, and false-positive rate is 0.1.",
          "Posterior, factor reasoning, and approximate-inference choice.",
          "Base rate, normalization, and evidence rarity are handled correctly.",
          [
              p("a", 5, "Compute P(disease|positive).", "True-positive mass is 0.02(0.9)=0.018; false-positive mass is 0.98(0.1)=0.098; posterior is 0.018/0.116, approximately 0.1552."),
              p("b", 5, "Explain how variable elimination avoids repeated enumeration.", "It restricts evidence, multiplies all factors containing one hidden variable, sums that variable out once, and reuses the resulting smaller factor for remaining query values."),
              p("c", 5, "Compare rejection sampling with likelihood weighting for rare evidence.", "Rejection sampling discards almost all inconsistent samples and is inefficient. Likelihood weighting clamps evidence and weights samples by its likelihood, retaining samples but potentially suffering high weight variance."),
          ]),
        q(5, "Regression and gradient descent", 15,
          "X=[[1,0],[1,1],[1,2]], y=[1,3,5], and w=[0,0] for one-half mean squared error.",
          "Gradient calculation, update, and conditioning analysis.",
          "Vectorized arithmetic, scaling, and numerical reasoning are correct.",
          [
              p("a", 5, "Compute the initial residual and gradient.", "Residual is [-1,-3,-5]. X^T residual=[-9,-13]; divide by m=3 to obtain gradient [-3,-13/3]."),
              p("b", 5, "With alpha=0.1, compute the new weights.", "w_new=[0.3,13/30], approximately [0.3,0.4333]."),
              p("c", 5, "Explain how feature scaling and collinearity affect optimization or solving.", "Scaling reduces elongated loss contours and supports a common learning rate. Collinearity makes X^T X singular or ill-conditioned, producing unstable coefficients; use a stable least-squares solver, pseudoinverse, or regularization."),
          ]),
        q(6, "Neural networks and backpropagation", 15,
          "A layer has A_prev shape (4,20), W shape (3,4), b shape (3,1), and delta shape (3,20).",
          "Shape derivation, gradient formulas, and checking.",
          "Matrix orientation, averaging, and verification are correct.",
          [
              p("a", 5, "Give Z, A, dW, and db shapes.", "Z and A are 3 by 20; dW=delta A_prev^T/m is 3 by 4; db=sum delta across examples with keepdims is 3 by 1."),
              p("b", 5, "Write the previous-layer delta formula and shape.", "delta_prev=(W^T delta) elementwise f_prime(Z_prev); W^T delta is 4 by 20, matching the previous layer."),
              p("c", 5, "Describe a two-sided gradient check and one limitation.", "Perturb each parameter by plus and minus epsilon, compute the centered finite difference, and compare with backprop by relative error. It is expensive and can be unreliable at nondifferentiable points such as ReLU zero."),
          ]),
        q(7, "Classification and regularization", 15,
          "A binary classifier has logit z=log(4), label y=1, w=[3,4], lambda=0.5, and m=5.",
          "Probability, loss, L2 penalty, and threshold interpretation.",
          "Logistic and regularization calculations are correct.",
          [
              p("a", 5, "Compute sigmoid(z) and cross-entropy loss.", "Since exp(z)=4, sigmoid(z)=4/(1+4)=0.8. For y=1, loss=-log(0.8), approximately 0.2231."),
              p("b", 5, "Compute the L2 penalty and gradient addition.", "Squared norm is 25; penalty=lambda*25/(2m)=1.25. Gradient addition is lambda w/m=[0.3,0.4], excluding the intercept."),
              p("c", 5, "Explain why threshold 0.5 is not universally optimal.", "Threshold choice trades false positives and false negatives and should reflect costs, capacity, and validation evidence; the probability midpoint ignores asymmetric consequences and prevalence."),
          ]),
        q(8, "Evaluation and tuning", 15,
          "A rare-event classifier yields TP=12, FP=8, FN=3, and TN=977.",
          "Metrics, curve diagnosis, and selection protocol.",
          "Counts, diagnostic logic, and data isolation are correct.",
          [
              p("a", 5, "Compute accuracy, precision, recall, and F1.", "Accuracy=(12+977)/1000=0.989; precision=12/20=0.6; recall=12/15=0.8; F1=2(0.6)(0.8)/1.4, approximately 0.6857."),
              p("b", 5, "Training and validation error are both high and close. Diagnose and name one experiment.", "This suggests underfitting or high bias. Test more capacity, improved features, weaker regularization, or corrected optimization while preserving the split."),
              p("c", 5, "Give a valid hyperparameter workflow with k-fold CV.", "Define ranges and metric, fit preprocessing and a fresh model inside each fold, compare means and spreads on fixed folds, lock one configuration, optionally refit under a predeclared rule, then evaluate the untouched test set once."),
          ]),
        q(9, "Fairness and responsible deployment", 15,
          "Group A0 has TPR=0.85 and FPR=0.10; group A1 has TPR=0.65 and FPR=0.25. A production feature distribution then shifts.",
          "Disparity, criterion reasoning, and monitoring control.",
          "Formal metrics and lifecycle response are complete.",
          [
              p("a", 5, "Compute the equalized-odds gaps and interpret them.", "Absolute TPR gap is 0.20 and FPR gap is 0.15; equalized odds is not satisfied, and A1 bears both more missed positives and more false positives under these rates."),
              p("b", 5, "Explain why removing the protected attribute alone does not establish fairness.", "Proxy variables, historical labels, sampling, measurement, and deployment feedback can reproduce group disparities. Audit disaggregated counts, data provenance, and consequences."),
              p("c", 5, "Specify a complete shift monitor and response.", "Define a feature-distance or population-stability metric against the release baseline, window and minimum count, alert threshold, model-risk owner, and actions such as investigation, human fallback, scope restriction, or rollback; confirm with delayed labeled performance."),
          ]),
        q(10, "Cross-module integration", 15,
          "Design a system that combines a learned heuristic, Bayesian belief state, and a search or control policy for navigation under uncertain hazards.",
          "Architecture, verification, and responsible evidence plan.",
          "The design integrates methods and preserves or explicitly relinquishes guarantees.",
          [
              p("a", 5, "Define the component handoffs.", "Sensor observations update a normalized hazard posterior; the posterior and observable state form fixed-size features; a learned model predicts remaining risk or cost; the planner or policy consumes that estimate while outputting only legal actions."),
              p("b", 5, "State three component or end-to-end tests.", "Compare posterior updates with enumeration, compare learned heuristic search with UCS on small maps, verify terminal and legal-action behavior, and run a fixed-seed end-to-end hazard scenario with expected path and safety invariants."),
              p("c", 5, "Design a baseline, metrics, and limitation statement.", "Use a fixed-prior plus hand-designed heuristic baseline under identical maps and seeds. Report path cost, expansions, hazard rate, success, posterior calibration or error, and variability. State that learned overestimation or shifted sensors can break optimality or safety and define a fallback."),
          ]),
    ],
    ["A logistic probability is numerically zero.", "A subgroup metric denominator is zero.", "A ReLU check lands at zero.", "A learned heuristic overestimates.", "A production dependency fails during evaluation."],
    ["Use stable logits loss.", "Report the declared undefined or zero convention with counts.", "Move the check point or state a subgradient.", "Reopen safely or relinquish optimality and compare with UCS.", "Use a transparent local fallback and do not fabricate results."],
    "Name one connection among modules that changed how you would design or evaluate an AI system.",
    "A full-credit response names a concrete handoff or shared invariant and explains how it changes implementation evidence, guarantees, or responsible-use decisions.",
)
