"""Assessment specifications for CMPSC 480 Weeks 6-15 and Quizzes 3-5."""


def part(label, points, question, answer):
    return {"label": label, "points": points, "question": question, "answer": answer}


def task(pid, title, points, prompt, deliverable, grading, parts):
    return {
        "id": pid, "title": title, "points": points, "prompt": prompt,
        "deliverable": deliverable, "grading": grading, "parts": parts,
    }


BASE_REQUIREMENTS = [
    "Use Python 3.11 and NumPy; do not use a library that implements the assessed algorithm.",
    "Keep data, model, optimization, and evaluation responsibilities behind explicit interfaces.",
    "Validate shapes, ranges, finite values, empty inputs, and terminal or degenerate cases.",
    "Use deterministic seeds and record every configuration used for reported evidence.",
    "Include focused tests and a README with exact reproduction commands.",
]


def spec(title, subtitle, short, overview, coverage, duration, submission, points,
         objectives, problems, edge_cases, edge_solutions, reflection, reflection_answer,
         requirements=None, submission_steps=None):
    return {
        "title": title, "subtitle": subtitle, "short_title": short,
        "overview": overview, "coverage": coverage, "duration": duration,
        "submission": submission, "total_points": points,
        "objectives": objectives,
        "requirements": requirements or BASE_REQUIREMENTS,
        "problems": problems,
        "edge_cases": edge_cases,
        "edge_solutions": edge_solutions,
        "submission_steps": submission_steps or [
            "Submit source, tests, README, configuration, and the requested report.",
            "Provide one command that reproduces the primary result from a clean environment.",
            "Exclude credentials, generated caches, and unlicensed data.",
        ],
        "reflection_length": "150-250 words",
        "reflection": reflection,
        "reflection_answer": reflection_answer,
    }


SPECS = {}

SPECS["week_06_assignment"] = spec(
    "Week 6 Assignment: Linear Q-Function Approximation",
    "Feature design, semi-gradient updates, and stability evidence",
    "Week 6 Assignment",
    "Replace a Q-table with a fixed-size linear approximator and verify every update.",
    "Week 6: function approximation, semi-gradients, and the deadly triad",
    "6-8 hours", "Repository plus experiment memo", 10,
    [
        "Implement a fixed-length state-action feature map.",
        "Compute Q values as vectorized dot products.",
        "Apply terminal-aware semi-gradient Q-learning.",
        "Demonstrate the one-hot tabular correspondence.",
        "Monitor numerical stability across controlled runs.",
    ],
    [
        task(1, "Features and dimensions", 2,
             "Design a feature map whose length is independent of the number of raw states.",
             "Feature implementation, dimensionality assertion, and feature table.",
             "Features are fixed length, normalized, documented, and safely validated.",
             [
                 part("a", 1, "Define at least four state-action features and justify their scales.", "A full-credit design names each signal, such as normalized coordinates, goal distance, wall risk, and action alignment; all are finite and on comparable documented scales."),
                 part("b", 1, "Prove by an executable assertion that parameter size does not grow when the environment map grows.", "Instantiate two map sizes with the same feature schema and assert equal feature and weight shapes. Reject any feature vector with a mismatched dimension."),
             ]),
        task(2, "Linear values and policy", 2,
             "Implement Q-hat and epsilon-greedy action selection over legal actions.",
             "Vectorized q_value and deterministic evaluation tests.",
             "Dot product, legal-action filtering, probabilities, and ties are correct.",
             [
                 part("a", 1, "Compute Q-hat(s,a;w) and test a known vector by hand.", "Return float(w dot f). For w=[1,-2,0.5] and f=[2,1,4], Q-hat=2-2+2=2."),
                 part("b", 1, "Specify training and evaluation tie behavior.", "Training explores uniformly with probability epsilon and otherwise uses a stable argmax over legal actions. Evaluation sets epsilon to zero and uses the same documented stable tie order."),
             ]),
        task(3, "Semi-gradient update", 4,
             "Implement the squared-TD-error semi-gradient rule with correct terminal masking.",
             "Update method, derivation, and hand-computed tests.",
             "Target, TD error, gradient, terminal rule, and signs are correct.",
             [
                 part("a", 2, "Derive the update from one-half times squared TD error.", "With y treated as fixed, negative loss gradient is (y-Q-hat) grad Q-hat. For a linear function grad Q-hat=f, so w receives alpha times delta times f."),
                 part("b", 1, "Compute an update for w=[0,0], f=[1,2], reward=1, gamma=0.5, max-next-Q=4, and alpha=0.1.", "The target is 3, current Q is 0, delta is 3, and the new weights are [0.3,0.6]."),
                 part("c", 1, "State and test the terminal target.", "When done is true, y equals reward with no next-state maximum. A test uses an enormous next Q and confirms the terminal update is unchanged."),
             ]),
        task(4, "Experiment and stability", 2,
             "Compare feature sets and report evidence beyond episodic return.",
             "Ablation table, stability plots or summaries, and defensive tests.",
             "Controlled comparison includes return, TD error, parameter norm, and multiple seeds.",
             [
                 part("a", 1, "Run one feature ablation and compare with a tabular small-state oracle.", "Hold seed, budget, and hyperparameters fixed; report return and action agreement. Explain whether the removed feature changes generalization or bias."),
                 part("b", 1, "Define an instability gate using at least three logged quantities.", "A suitable gate watches nonfinite values, weight norm, TD-error quantiles, and evaluation return across seeds, and stops or flags the run when declared thresholds are exceeded."),
             ]),
    ],
    ["Zero feature vector.", "Terminal next state.", "Feature dimension mismatch.", "All legal actions tie.", "Weight or TD error becomes nonfinite."],
    ["The prediction is zero and no coordinate changes.", "Target equals reward only.", "Raise a clear error before the dot product.", "Use stable evaluation order.", "Stop, record the transition and configuration, and mark the run invalid."],
    "Identify one feature that generalized useful information and one feature that created coupling risk. Cite an ablation or trace.",
    "A strong response links feature overlap to which predictions changed, cites controlled evidence, and distinguishes improved return from stable value estimates.",
)

SPECS["week_07_assignment"] = spec(
    "Week 7 Module Project B: Q-Learning with Bayesian Belief Tracking",
    "Acting under partial observability with normalized posterior state",
    "Module Project B",
    "Integrate a from-scratch Bayesian hazard belief with a Q-learning policy.",
    "Weeks 4-7: MDPs, Q-learning, approximation, Bayes nets, and inference",
    "10-14 hours", "Repository, evaluation report, and belief traces", 20,
    [
        "Update a categorical belief using Bayes rule.",
        "Handle impossible or numerically tiny evidence defensively.",
        "Expose belief summaries to a Q-learning state representation.",
        "Train and evaluate under several sensor-noise regimes.",
        "Ablate belief tracking against a nonbelief baseline.",
    ],
    [
        task(1, "Belief model", 5,
             "Implement a categorical prior, sensor likelihood, and normalized posterior over candidate hazard locations.",
             "BeliefTracker, fixed-sequence oracle tests, and trace table.",
             "Bayes numerator, normalization, repeated evidence, and validation are correct.",
             [
                 part("a", 2, "Write the vectorized posterior update.", "For each hypothesis h, compute unnormalized[h]=likelihood(observation|h,agent_state)*prior[h], then divide by the sum. Validate a nonnegative finite prior that sums to one."),
                 part("b", 2, "Hand compute prior [0.5,0.5] with likelihoods [0.8,0.2] for one observation.", "Unnormalized masses are [0.4,0.1], normalization is 0.5, and posterior is [0.8,0.2]."),
                 part("c", 1, "Define behavior when the normalization constant is zero or nonfinite.", "Raise a domain-specific impossible-evidence error or apply a documented fallback such as restoring the prior; never silently divide by zero or invent a posterior."),
             ]),
        task(2, "RL agent", 4,
             "Implement terminal-aware Q-learning using only information available to the agent.",
             "Agent interface, update tests, and reproducible training loop.",
             "No hidden-state leakage; exploration, targets, and termination are correct.",
             [
                 part("a", 2, "Define the observable agent state and prove it excludes the true hidden hazard.", "The state may include position, local observation, and belief vector or its summary. A test inspects inputs and confirms the true hazard identifier is never passed to policy or update code."),
                 part("b", 2, "Specify epsilon-greedy selection and the terminal Q update.", "Choose uniformly among legal actions with probability epsilon, otherwise stable argmax. For terminal steps target equals immediate reward; for others add gamma times max next Q."),
             ]),
        task(3, "Integration contract", 4,
             "Connect observations to posterior updates and posterior state to action selection.",
             "End-to-end sequence diagram, integration tests, and checkpoint serialization.",
             "Update order, state encoding, reset, and episode isolation are correct.",
             [
                 part("a", 2, "State the within-step order from observation to action to learning.", "Condition the prior on the new observation, build the policy state from the updated belief, choose a legal action, execute it, then apply the reward transition update under the documented convention."),
                 part("b", 1, "Test that reset restores the declared prior and clears episode-local state.", "Two episodes after reset begin with identical beliefs and agent state under the same seed, with no posterior or history leaked from the previous episode."),
                 part("c", 1, "List every component needed to resume training exactly.", "Save Q parameters or table, belief configuration, online belief if mid-episode, epsilon, counters, environment state if supported, and all random-generator states."),
             ]),
        task(4, "Noise study and ablation", 4,
             "Evaluate policy safety and reward at low, medium, and high sensor noise.",
             "Controlled result table with belief and no-belief baselines.",
             "Noise, seeds, budgets, baselines, metrics, and uncertainty are reported.",
             [
                 part("a", 2, "Define safety and performance metrics and run multiple seeds.", "Report mean return, success, hazard rate, and belief accuracy or entropy with variability for identical evaluation episodes and epsilon zero."),
                 part("b", 2, "Ablate the posterior input and interpret the difference.", "Replace the belief with a fixed prior or observation-only state while holding all else fixed. Attribute only the controlled performance change to belief integration."),
             ]),
        task(5, "Defensive evidence", 3,
             "Test belief and policy behavior on adversarial boundary cases.",
             "Focused tests and a short failure analysis.",
             "Tests cover impossible evidence, high noise, ties, and normalization drift.",
             [
                 part("a", 2, "Provide four tests and name the defect each exposes.", "Use repeated identical evidence, impossible evidence, uninformative sensor likelihoods, and a terminal transition; each test states expected belief or target and its associated bug."),
                 part("b", 1, "Explain why a high-noise posterior should remain closer to the prior.", "When likelihoods are similar across hypotheses, multiplying by them changes relative prior masses little; normalized posterior information gain is therefore small."),
             ]),
    ],
    ["Prior has a negative entry.", "Evidence has zero likelihood under every hypothesis.", "Sensor is completely uninformative.", "Episode begins terminal.", "True hidden state accidentally enters features."],
    ["Reject the prior.", "Raise or use the documented impossible-evidence fallback.", "Posterior equals prior.", "Return without bootstrapping.", "Fail the leakage test and remove the hidden value."],
    "Describe one case where the belief was mathematically correct but the policy still behaved poorly. Separate inference error from control or learning error.",
    "A strong response verifies the posterior against an oracle, then uses visitation, reward design, policy state, or Q-learning evidence to locate the remaining control defect.",
)

SPECS["week_08_assignment"] = spec(
    "Week 8 Assignment: Linear Regression with Batch Gradient Descent",
    "Raw NumPy, normalization, convergence, and numerical defenses",
    "Week 8 Assignment",
    "Build a vectorized regression pipeline and compare it with a stable closed-form oracle.",
    "Week 8: linear regression, MSE, gradient descent, and scaling",
    "6-8 hours", "Repository plus convergence report", 10,
    [
        "Fit and reuse training-only normalization statistics.",
        "Implement a vectorized MSE gradient.",
        "Handle an intercept consistently.",
        "Stop on bounded, reproducible convergence criteria.",
        "Compare predictions with a pseudoinverse reference.",
    ],
    [
        task(1, "Data and normalization", 2, "Validate X and y and fit z-score scaling on training features.", "Stored means/scales and preprocessing tests.", "Shapes, constant columns, bias, and leakage prevention are correct.", [
            part("a", 1, "Specify fit and predict shape rules and bias handling.", "X is m by n and y is length m or m by 1. Normalize measured features, then add one bias column; predict reuses training means and scales without adding a second bias."),
            part("b", 1, "Handle a zero-variance feature.", "Use a scale of one for that column or drop it under a documented policy, preserving finite transformed values and consistent prediction behavior."),
        ]),
        task(2, "Vectorized optimizer", 4, "Implement full-batch gradient descent with cost history and finite guards.", "Trainer, gradient tests, and convergence trace.", "MSE, gradient, update sign, averaging, and stopping are correct.", [
            part("a", 2, "Derive and implement the gradient of one-half mean squared error.", "With residual r=Xw-y, grad=X^T r/m. The update subtracts alpha times grad and has the same shape as w."),
            part("b", 1, "Compute one update for X=[[1,0],[1,1]], y=[1,3], w=[0,0], alpha=0.5.", "Residual is [-1,-3], gradient is [-2,-1.5], and w becomes [1,0.75]."),
            part("c", 1, "Define divergence and stopping checks.", "Reject nonfinite loss or weights, cap iterations, and stop only under a positive tolerance based on gradient norm or repeated small cost change."),
        ]),
        task(3, "Oracle comparison", 2, "Compare learned predictions with NumPy pseudoinverse least squares.", "Tolerance checks on several synthetic datasets.", "Predictions, not unstable coefficients alone, match within justified tolerance.", [
            part("a", 1, "State why the pseudoinverse is preferable to explicitly inverting X transpose X.", "It handles rank deficiency and avoids squaring the condition number through an explicit Gram-matrix inverse."),
            part("b", 1, "Define a comparison for a collinear dataset.", "Compare training predictions and residual norm with a relaxed documented tolerance; do not demand identical nonunique coefficients."),
        ]),
        task(4, "Experiments and tests", 2, "Evaluate learning rate and scaling while covering small and degenerate inputs.", "Controlled table and focused test suite.", "Evidence isolates one variable and includes numerical boundaries.", [
            part("a", 1, "Compare two learning rates with and without scaling.", "Use identical initialization and data; report iterations, final loss, and whether loss is monotone or divergent."),
            part("b", 1, "Test one feature, m<n, constant feature, empty input, and nonfinite data.", "Valid small cases return finite predictions; invalid empty or nonfinite inputs raise clear errors; underdetermined training is compared by predictions."),
        ]),
    ],
    ["A constant feature.", "One training example.", "More features than examples.", "Learning rate causes nonfinite loss.", "Predict is called before fit."],
    ["Use a safe scale convention.", "Produce a documented fit or reject if a minimum is required.", "Allow nonunique weights and compare predictions.", "Stop and report divergence.", "Raise a not-fitted error."],
    "Explain one case where the loss curve looked plausible but an oracle or invariant exposed a defect.",
    "A strong answer cites a shape, averaging, scaling, or leakage invariant, shows the discrepancy, and names the regression test added after repair.",
)

SPECS["week_09_assignment"] = spec(
    "Week 9 Assignment: A Neural Network from Scratch",
    "Vectorized forward propagation, backpropagation, and gradient checking",
    "Week 9 Assignment",
    "Implement a small feedforward network in raw NumPy and certify its gradients.",
    "Week 9: architecture, activations, backpropagation, and finite differences",
    "8-10 hours", "Repository plus gradient-check report", 10,
    [
        "Represent arbitrary layer sizes with explicit shapes.",
        "Cache a vectorized forward pass.",
        "Compute every parameter gradient by backpropagation.",
        "Validate gradients with two-sided finite differences.",
        "Train only after the correctness gate passes.",
    ],
    [
        task(1, "Architecture and forward pass", 2, "Implement affine layers and configurable hidden activations.", "NeuralNetwork class, caches, and shape tests.", "Batch convention, broadcasting, activations, and cache ownership are correct.", [
            part("a", 1, "State the shape of W and b for each layer and vectorize over m examples.", "Under the course convention W[l] is n_l by n_(l-1), b[l] is n_l by 1, and activations are n_l by m with examples as columns."),
            part("b", 1, "Test duplicated examples and permuted batch columns.", "Duplicated input columns must yield duplicated outputs; permuting example columns must permute outputs identically without changing parameters."),
        ]),
        task(2, "Backpropagation", 4, "Compute output and hidden deltas, weight gradients, and bias gradients.", "Backward method and hand trace.", "Chain rule, transposes, activation derivatives, and batch averaging are correct.", [
            part("a", 2, "Derive dW, db, and the previous-layer delta.", "dW=delta A_prev^T/m, db=sum(delta across examples)/m, and delta_prev=(W^T delta) elementwise activation_prime(Z_prev)."),
            part("b", 1, "Explain why all gradients must be computed before any parameter update.", "Earlier-layer gradients depend on the same forward-pass parameter values. Updating during reverse traversal mixes parameter versions and invalidates the chain-rule computation."),
            part("c", 1, "Give a duplicated-batch invariant.", "Repeating every example leaves mean loss and correctly averaged gradients unchanged; a missing divide-by-m doubles the gradient."),
        ]),
        task(3, "Numerical gradient check", 3, "Implement two-sided finite differences without autograd.", "Per-parameter check, relative-error summary, and failing-case diagnostic.", "Perturbation, restoration, deterministic loss, and tolerance are correct.", [
            part("a", 1, "State the numerical derivative and relative error.", "g_num=[L(theta+epsilon)-L(theta-epsilon)]/(2epsilon). Compare flattened vectors using norm difference divided by the sum of norms plus a tiny guard."),
            part("b", 1, "Describe how to check every parameter without corrupting state.", "Perturb one scalar, compute both losses on fixed data, restore its original value immediately, and repeat with dropout or randomness disabled."),
            part("c", 1, "Define the release gate and a ReLU boundary precaution.", "Require maximum or aggregate relative error below the declared tolerance; choose inputs away from z=0 because ReLU is nondifferentiable there."),
        ]),
        task(4, "Training and defenses", 1, "Run a short training experiment only after gradient checks pass.", "Loss trace and edge-case tests.", "Training uses analytical gradients and reports finite, reproducible evidence.", [
            part("a", 1, "Report the correctness gate, loss trend, and three defensive tests.", "Include checked parameter count and maximum relative error, then a seeded loss curve plus empty batch, invalid label shape, and nonfinite input tests."),
        ]),
    ],
    ["Empty batch.", "One-example batch.", "ReLU preactivation exactly zero.", "Wrong target shape.", "A parameter becomes nonfinite."],
    ["Reject empty training input.", "Preserve all matrix dimensions.", "Avoid that point in gradient checking or document a subgradient.", "Raise before loss computation.", "Stop and record the failing step."],
    "Describe the first gradient defect you found, the evidence that localized it, and why a decreasing loss would not have been sufficient proof.",
    "A strong response names a tensor or reduction, cites analytical-versus-numerical evidence, explains the fix, and distinguishes trainability from derivative correctness.",
)

SPECS["quiz_03"] = spec(
    "Quiz 3: Approximation, Probability, and Neural Computation",
    "Weeks 6-9",
    "Quiz 3",
    "Apply semi-gradients, Bayes rule, gradient descent, and neural-network shapes.",
    "Weeks 6-9", "35 minutes", "Individual PDF", 20,
    ["Compute a linear TD update.", "Normalize a posterior.", "Perform one gradient step.", "Trace a neural layer.", "Explain a stability mechanism."],
    [
        task(1, "Linear Q update", 4, "Use w=[0.2,-0.1], f=[1,2], reward=1, gamma=0.5, max-next-Q=2, alpha=0.25.", "Arithmetic trace.", "Q, target, delta, and weight update are correct.", [
            part("a", 2, "Compute Q, target, and delta.", "Q=0.2-0.2=0; target=1+0.5(2)=2; delta=2."),
            part("b", 2, "Compute the new weights and state the terminal target.", "Increment is 0.25(2)[1,2]=[0.5,1], so new w=[0.7,0.9]. For a terminal transition target is reward 1."),
        ]),
        task(2, "Bayesian update", 4, "Prior over two hazards is [0.6,0.4]; observation likelihood is [0.2,0.8].", "Posterior calculation.", "Unnormalized masses and normalization are correct.", [
            part("a", 2, "Compute the unnormalized masses and evidence probability.", "Masses are [0.12,0.32] and evidence probability is 0.44."),
            part("b", 2, "Normalize and identify the most likely hazard.", "Posterior is approximately [0.2727,0.7273], so the second hazard is most likely."),
        ]),
        task(3, "Regression step", 4, "X=[[1,0],[1,2]], y=[1,5], w=[0,0], alpha=0.25.", "One batch-gradient step.", "Residual, averaged gradient, and update are correct.", [
            part("a", 2, "Compute residual and gradient for one-half mean squared error.", "Residual=[-1,-5]; X^T residual=[-6,-10]; divide by 2 to get [-3,-5]."),
            part("b", 2, "Compute new w.", "w_new=[0,0]-0.25[-3,-5]=[0.75,1.25]."),
        ]),
        task(4, "Network shapes", 4, "A batch has 10 examples with 3 inputs, a 5-unit hidden layer, and 2 outputs.", "Shape table.", "W, b, Z, and A shapes follow the declared convention.", [
            part("a", 2, "Give W1, b1, and A1 shapes.", "W1 is 5 by 3, b1 is 5 by 1, and A1 is 5 by 10."),
            part("b", 2, "Give W2, b2, and output shapes.", "W2 is 2 by 5, b2 is 2 by 1, and output activation is 2 by 10."),
        ]),
        task(5, "Stability reasoning", 4, "Explain one role of replay and one role of numerical gradient checking.", "Short explanation.", "Mechanisms and limits are distinguished.", [
            part("a", 2, "Why does replay help DQN?", "Random batches reduce short-range temporal correlation and reuse transitions; replay does not guarantee convergence or remove target motion."),
            part("b", 2, "Why is gradient checking not used for training?", "Finite differences provide an independent derivative oracle but require two loss evaluations per parameter and are far too expensive for iterative training."),
        ]),
    ],
    ["Terminal TD step.", "Zero posterior normalization.", "Batch of one.", "ReLU at zero."],
    ["Remove bootstrap.", "Raise or use a declared impossible-evidence policy.", "Keep two-dimensional shapes.", "Use a documented subgradient and avoid the point in numerical checks."],
    "Name the most useful invariant in this quiz.",
    "A full-credit sentence states a concrete invariant such as posterior normalization, gradient shape, terminal masking, or duplicated-batch averaging and explains what defect it exposes.",
    requirements=["Work independently.", "Show every numeric step.", "State shape convention and terminal assumptions.", "No electronic communication."],
    submission_steps=["Write your name and assumptions.", "Show arithmetic and intermediate vectors.", "Submit only the completed response PDF."],
)

SPECS["week_10_assignment"] = spec(
    "Week 10 Assignment: Logistic Regression and Regularization",
    "Stable cross-entropy, L2 comparison, and protected test evaluation",
    "Week 10 Assignment",
    "Build a binary classifier from raw NumPy and run a leakage-resistant regularization study.",
    "Week 10: logistic regression, cross-entropy, overfitting, and L2",
    "7-9 hours", "Repository plus model-selection report", 10,
    [
        "Implement stable sigmoid probabilities and cross-entropy.",
        "Derive and vectorize the logistic gradient.",
        "Apply L2 to weights but not the intercept.",
        "Create disjoint train, validation, and test partitions.",
        "Select lambda without test-set feedback.",
    ],
    [
        task(1, "Classifier mathematics", 4, "Implement predict_proba, loss, and gradient in raw NumPy.", "LogisticRegression class and numerical tests.", "Stable probability, cross-entropy, gradient, and vectorization are correct.", [
            part("a", 2, "State the binary model, loss, and gradient.", "p=sigmoid(Xw+b); mean loss is -mean[y log p+(1-y)log(1-p)]; dw=X^T(p-y)/m and db=mean(p-y)."),
            part("b", 1, "Compute p and loss for z=0 and y=1.", "Sigmoid(0)=0.5 and loss=-log(0.5), approximately 0.6931."),
            part("c", 1, "Describe stable implementations for large-magnitude logits.", "Use a branch-stable sigmoid and a fused logits loss such as mean(softplus(z)-yz), or clip probabilities only for the logarithm."),
        ]),
        task(2, "L2 regularization", 2, "Add configurable L2 while excluding the intercept.", "Regularized gradient test and convention note.", "Penalty, normalization, and bias exclusion match the declared formula.", [
            part("a", 1, "Write the L2 loss and weight-gradient addition.", "Add lambda||w||^2/(2m) and lambda w/m to dw; do not add this term to db."),
            part("b", 1, "Give a test that would catch accidental bias regularization.", "Use zero feature values so only b affects predictions; changing lambda must not change the computed db or add a direct shrinkage term to b."),
        ]),
        task(3, "Split and selection", 2, "Implement a seeded, disjoint train-validation-test split and search at least three lambdas.", "Index audit and full validation table.", "Partitions do not overlap and the test set is unused until selection is locked.", [
            part("a", 1, "Prove partition completeness and nonoverlap.", "Store original indices; assert pairwise intersections are empty and their union equals every example exactly once, with a documented class-balance policy."),
            part("b", 1, "State the lambda-selection protocol.", "Fit preprocessing and models using training data, compare lambdas on validation only, lock the best declared metric, and then run one final test evaluation."),
        ]),
        task(4, "Evidence and defenses", 2, "Report train-validation behavior and final test metrics.", "Comparison table, curves or summaries, and edge tests.", "The report distinguishes selection evidence from final confirmation.", [
            part("a", 1, "Report at least lambda=0 and two positive values.", "For each configuration report final train and validation loss plus a classification metric; justify the locked lambda using validation evidence only."),
            part("b", 1, "Test one-class data, empty partition, extreme logits, and predict-before-fit.", "Invalid split or unfitted use raises a clear error; extreme logits remain finite; a one-class partition is reported rather than causing a silent metric failure."),
        ]),
    ],
    ["Logit magnitude exceeds 1,000.", "Validation set contains one class.", "A split is empty.", "Lambda is negative.", "Test metrics were viewed during tuning."],
    ["Use stable logits formulas.", "Report the limitation and safe metric conventions.", "Reject the split.", "Reject configuration.", "Invalidate the experiment and repeat with a fresh held-out test set."],
    "Describe the train-validation signature across lambdas and justify the selected value without citing test performance.",
    "A strong response cites the validation table, explains the bias-variance tradeoff, and states that test results were obtained only after the choice was frozen.",
)

SPECS["week_11_assignment"] = spec(
    "Week 11 Assignment: Evaluation and Hyperparameter Search",
    "Metrics, cross-validation, search, and a single final test",
    "Week 11 Assignment",
    "Implement evaluation tooling and select a classifier configuration from first principles.",
    "Week 11: confusion metrics, cross-validation, and hyperparameter tuning",
    "7-9 hours", "Repository plus complete trial ledger", 10,
    [
        "Compute confusion counts and derived metrics.",
        "Handle zero denominators explicitly.",
        "Construct deterministic nonoverlapping k-fold splits.",
        "Train a fresh pipeline inside every fold.",
        "Search two hyperparameters and preserve the test set.",
    ],
    [
        task(1, "Metrics", 4, "Implement confusion_matrix and precision_recall_f1 from raw predictions.", "Metric functions and hand-computed tests.", "Counts, label semantics, formulas, and zero cases are correct.", [
            part("a", 2, "Given TP=8, FP=2, FN=4, TN=6, compute precision, recall, and F1.", "Precision=8/10=0.8; recall=8/12=2/3; F1=2(0.8)(2/3)/(0.8+2/3), approximately 0.7273."),
            part("b", 1, "Define the zero-denominator convention.", "Return zero or a configured undefined marker with a warning and counts; never raise an accidental division error or silently claim perfect performance."),
            part("c", 1, "Give one permutation invariant.", "Applying the same row permutation to y_true and y_pred leaves every confusion count and derived metric unchanged."),
        ]),
        task(2, "K-fold validation", 3, "Implement seeded fold assignment and fit a fresh model and preprocessing in every round.", "Fold audit and k score records.", "Coverage, nonoverlap, freshness, leakage prevention, and summaries are correct.", [
            part("a", 1, "State the fold coverage invariants.", "Every example appears in exactly one validation fold, no training-validation overlap exists within a round, and fold sizes differ by at most one unless stratification constraints require otherwise."),
            part("b", 1, "Explain where feature scaling is fit.", "Fit scaler statistics on the k-1 training folds independently in each round and apply those frozen statistics to the held-out fold."),
            part("c", 1, "Report mean, standard deviation, and all fold scores.", "Preserve individual scores because the mean alone hides instability; use the same fixed folds for fair candidate comparison."),
        ]),
        task(3, "Search and selection", 2, "Search learning rate and L2 strength with grid or random search.", "Complete configuration ledger and selection rule.", "All candidates use the same validation protocol and no test feedback.", [
            part("a", 1, "Define at least three values for each of two hyperparameters and compute the fit budget.", "A 3-by-3 grid has nine candidates and requires 9k model fits under k-fold CV, excluding a final refit."),
            part("b", 1, "Resolve a near tie without using the test set.", "Use a preregistered secondary criterion such as lower variance, smaller model, lower compute, or stronger regularization when mean differences are practically negligible."),
        ]),
        task(4, "Final report", 1, "Lock one configuration and perform one final test evaluation.", "One test result with provenance and limitations.", "The report clearly separates cross-validation selection from held-out confirmation.", [
            part("a", 1, "List the minimum evidence in the final report.", "Include all trial means and spreads, selection rule, locked configuration, one test confusion matrix and metrics, seeds, split identifiers, and limitations."),
        ]),
    ],
    ["A fold has no predicted positives.", "k exceeds the example count.", "A model object is reused across folds.", "Random search repeats a candidate.", "Test set is inspected before selection."],
    ["Apply the declared zero rule.", "Reject k.", "Create a fresh model and preprocessing.", "Record or resample under a documented policy.", "Restart with a new untouched test partition."],
    "Identify a configuration that looked strong on one fold but not across folds. Explain what the spread changed about your decision.",
    "A strong response cites fold-level evidence, avoids cherry-picking, and explains how variance, simplicity, or cost affected the final validation-only choice.",
)

SPECS["quiz_04"] = spec(
    "Quiz 4: Classification, Generalization, and Evaluation",
    "Weeks 10-11",
    "Quiz 4",
    "Compute classification losses and metrics, diagnose learning curves, and protect model selection.",
    "Weeks 10-11", "30 minutes", "Individual PDF", 20,
    ["Compute cross-entropy.", "Apply L2 reasoning.", "Diagnose bias and variance.", "Compute confusion metrics.", "Detect evaluation leakage."],
    [
        task(1, "Cross-entropy", 4, "A binary classifier predicts p=0.8 for y=1 and p=0.2 for y=0.", "Two loss calculations.", "The correct label term and logarithm are used.", [
            part("a", 2, "Compute the loss for p=0.8, y=1.", "Loss=-log(0.8), approximately 0.2231."),
            part("b", 2, "Compute the loss for p=0.2, y=0.", "Loss=-log(1-0.2)=-log(0.8), also approximately 0.2231."),
        ]),
        task(2, "Regularization", 4, "A model has w=[3,4], m=5, and lambda=0.5.", "Penalty and gradient addition.", "Normalization and bias convention are correct.", [
            part("a", 2, "Compute lambda||w||^2/(2m).", "The squared norm is 25; penalty is 0.5*25/10=1.25."),
            part("b", 2, "Compute the L2 addition to dw.", "lambda w/m=0.5[3,4]/5=[0.3,0.4]; the intercept is not included."),
        ]),
        task(3, "Learning curves", 4, "Training error is 0.05 and validation error is 0.35 after training; both began near 0.6.", "Diagnosis and experiment.", "Overfitting is identified and the proposed test targets variance.", [
            part("a", 2, "Diagnose the pattern.", "Low training error with a large validation gap is overfitting or high variance, assuming the split and preprocessing are valid."),
            part("b", 2, "Name one controlled next experiment.", "Increase L2, reduce capacity, add representative training data, or use earlier stopping while keeping the split and evaluation metric fixed."),
        ]),
        task(4, "Confusion metrics", 4, "TP=18, FP=6, FN=2, and TN=74.", "Metric calculation.", "Precision, recall, and F1 are correct.", [
            part("a", 2, "Compute precision and recall.", "Precision=18/24=0.75; recall=18/20=0.90."),
            part("b", 2, "Compute F1.", "F1=2(0.75)(0.90)/(1.65), approximately 0.8182."),
        ]),
        task(5, "Evaluation discipline", 4, "A grid search selects the configuration with highest test F1.", "Short critique and repair.", "The role of validation and test sets is correct.", [
            part("a", 2, "Explain the defect.", "The test set influenced selection and is no longer an unbiased final estimate; the reported maximum is optimistically selected."),
            part("b", 2, "State a valid workflow.", "Select candidates using a validation set or cross-validation, lock the entire pipeline, optionally refit under a predeclared rule, and evaluate once on untouched test data."),
        ]),
    ],
    ["Probability equals zero.", "No predicted positives.", "Train and validation errors are both high.", "Two configurations are practically tied."],
    ["Use stable logits loss.", "Apply declared zero-division rule.", "Diagnose underfitting rather than variance.", "Use a declared secondary criterion without test feedback."],
    "State one evaluation rule you would enforce in code.",
    "A full-credit sentence gives a testable rule such as disjoint split indices, preprocessing fit only on training folds, or a single test-evaluation gate.",
    requirements=["Work independently.", "Show numerical work.", "Use natural logarithms.", "No electronic communication."],
    submission_steps=["Write your name and assumptions.", "Show intermediate arithmetic.", "Submit only the completed response PDF."],
)

SPECS["week_12_assignment"] = spec(
    "Week 12 Module Project C: Classifier Fairness Audit",
    "Train, disaggregate, mitigate, document, and monitor",
    "Module Project C",
    "Evaluate a from-scratch classifier across sensitive groups and produce a model-card-style audit.",
    "Weeks 8-12: classification, metrics, fairness, documentation, and deployment",
    "12-16 hours", "Repository plus separate 800-1200 word audit report", 20,
    [
        "Train a validated from-scratch classifier.",
        "Compute group confusion matrices and disparity metrics.",
        "Flag low-confidence subgroup evidence.",
        "Implement and evaluate one mitigation.",
        "Document intended use, limitations, and monitoring.",
    ],
    [
        task(1, "Model and data discipline", 4, "Train a logistic or small neural classifier using a protected train-validation-test protocol.", "Versioned model pipeline and baseline metrics.", "Core model is correct, splits are isolated, and data provenance is documented.", [
            part("a", 2, "Describe the model, split, preprocessing, and sensitive attribute handling.", "State architecture and loss, index-level partitions, training-only preprocessing, whether A is used as a feature, and why. Protected information may still be retained for auditing."),
            part("b", 2, "Provide overall validation and final test confusion metrics.", "Select using validation only, lock the pipeline, then report one test confusion matrix with accuracy, precision, recall, and F1 plus counts."),
        ]),
        task(2, "Disaggregated metrics", 5, "Implement evaluate_subgroups and two formal disparity measures.", "Per-group counts, metrics, unit tests, and disparity table.", "First-principles computations match hand examples and publish denominators.", [
            part("a", 2, "Compute confusion counts, positive rate, TPR, FPR, precision, and sample size per group.", "Condition y_true and y_pred by A, build each confusion matrix, derive metrics with explicit zero rules, and return counts as well as rates."),
            part("b", 2, "Define demographic-parity difference and equalized-odds gap.", "DP difference is the difference or absolute difference in group positive prediction rates under the declared direction. EO gap summarizes the maximum or reported pair of absolute TPR and FPR gaps."),
            part("c", 1, "Validate against a hand-computed tiny dataset.", "The unit test lists labels, predictions, groups, expected group counts, and exact disparity values; it fails if conditioning or denominators are reversed."),
        ]),
        task(3, "Confidence and diagnosis", 3, "Interpret disparities using the Week 12 bias taxonomy and subgroup sample sizes.", "Cause hypotheses and low-confidence flags.", "The report separates measured association, uncertainty, and causal speculation.", [
            part("a", 1, "Define a low-count flag and show it in the table.", "Declare a threshold or interval-based rule before inspecting results; retain the metric but visibly mark limited evidence and publish n."),
            part("b", 2, "Give two plausible pipeline-stage explanations and evidence that would distinguish them.", "Examples include sampling undercoverage versus label bias; propose provenance checks, label audits, feature distributions, or additional data rather than claiming a cause from rates alone."),
        ]),
        task(4, "Mitigation experiment", 4, "Implement one concrete mitigation and compare before and after.", "Controlled fairness-performance comparison.", "The intervention, protocol, overall metrics, and disparity metrics are all explicit.", [
            part("a", 2, "Specify a mitigation such as reweighting, resampling, threshold adjustment, or feature revision.", "Define precisely which data, loss, threshold, or feature changes and fit it without touching test labels or selecting on the final test."),
            part("b", 2, "Report the fairness-performance tradeoff.", "Use the same evaluation set and publish overall performance plus group metrics before and after, including variability or counts; avoid declaring universal improvement when criteria conflict."),
        ]),
        task(5, "Model-card audit", 4, "Produce a separate audit report suitable for release review.", "800-1200 word report with reusable sections.", "The report covers scope, evidence, limitations, tradeoffs, and postdeployment controls.", [
            part("a", 2, "Include intended use, out-of-scope use, data, evaluation, disaggregated results, and limitations.", "Each section is concrete to the submitted version and links claims to result tables or repository artifacts."),
            part("b", 1, "Discuss tension with at least one fairness criterion not selected.", "Explain which facts each criterion conditions on and why differing base rates or imperfect prediction can make simultaneous satisfaction impossible."),
            part("c", 1, "Specify two monitors and a response owner.", "Each monitor has metric, baseline, threshold, window, owner, and action such as human review, restriction, or rollback."),
        ]),
    ],
    ["A subgroup has no positive labels.", "A subgroup contains very few examples.", "Mitigation improves DP but worsens recall.", "Sensitive attribute is missing at deployment.", "A postlaunch feature distribution shifts."],
    ["Report undefined recall under the declared convention.", "Flag low confidence and collect more evidence.", "Report the tradeoff and justify context-specific choice.", "Define whether auditing is possible and what proxy risks remain.", "Trigger the declared monitor and response process."],
    "Identify the hardest judgment in your audit. Explain what evidence informed it, what remained uncertain, and who should own the decision.",
    "A strong response distinguishes measured facts from normative choice, names affected stakeholders and residual uncertainty, and assigns an accountable decision or escalation owner.",
)

SPECS["week_13_assignment"] = spec(
    "Week 13 Assignment: Cross-Module Debugging Practicum",
    "Localize failures, make targeted repairs, and prevent regressions",
    "Week 13 Assignment",
    "Repair three supplied implementations using failing tests as the first evidence.",
    "Weeks 1-12 integration and debugging",
    "5-7 hours", "Patched repository plus diagnosis log", 10,
    [
        "Reproduce a failure before editing code.",
        "Localize defects using minimal counterexamples.",
        "Preserve public APIs and make targeted patches.",
        "Add regression tests across three modules.",
        "Explain why each repair is correct.",
    ],
    [
        task(1, "Module A search defect", 3, "Repair a search implementation that fails a cheaper-rediscovery test.", "Targeted patch, before-after trace, and regression test.", "Diagnosis distinguishes frontier ordering from best-cost bookkeeping.", [
            part("a", 1, "Record the exact first failing assertion and a minimal graph trace.", "The log includes expected and actual path or cost and shows where a worse state entry blocks a later cheaper route."),
            part("b", 1, "Make the smallest API-preserving repair.", "Update best cost on cheaper rediscovery and ignore stale frontier entries, or implement equivalent decrease-key behavior without rewriting the domain."),
            part("c", 1, "Add a regression test and rerun the whole suite.", "The test fixes the graph and expected optimal cost; all previous search tests remain passing."),
        ]),
        task(2, "Module B terminal defect", 3, "Repair a Q-learning implementation that bootstraps after termination.", "Targeted patch, numeric trace, and regression test.", "Terminal semantics and update arithmetic are correct.", [
            part("a", 1, "Show the failing numeric update.", "Choose a terminal transition with a large next Q; the defective target includes gamma max Q and differs from the reward-only expected target."),
            part("b", 1, "Patch only the target construction.", "Set target to reward when done and retain the nonterminal formula otherwise; preserve public methods and training loop."),
            part("c", 1, "Add terminal and nonterminal regression tests.", "The pair proves the bootstrap is removed only at termination and that ordinary updates are unchanged."),
        ]),
        task(3, "Module C gradient defect", 3, "Repair a backpropagation implementation whose bias gradient uses the wrong axis.", "Shape evidence, finite-difference check, and regression test.", "Reduction axis, keepdims, averaging, and result shape are correct.", [
            part("a", 1, "Use shape evidence to localize the defect.", "For delta shape n_l by m, db must sum across example columns to n_l by 1; the wrong axis yields m-shaped or broadcasted values."),
            part("b", 1, "Make the targeted repair.", "Compute sum(delta, axis=1, keepdims=True)/m under the course convention and do not change unrelated weight-gradient code."),
            part("c", 1, "Report numerical-gradient relative error before and after.", "The bias check fails before, passes the declared tolerance after, and all other parameter checks remain passing."),
        ]),
        task(4, "Diagnosis report", 1, "Summarize evidence and change discipline across all three repairs.", "One table mapping test, symptom, cause, patch, and regression.", "The report is concise, reproducible, and avoids retrospective guessing.", [
            part("a", 1, "Explain why running the full suite after each patch matters.", "A targeted fix can violate another contract; the full suite detects regressions while the new minimal test permanently protects the discovered boundary case."),
        ]),
    ],
    ["A failing test is nondeterministic.", "Several tests fail from one root cause.", "The tempting fix rewrites the public API.", "A repair passes only the original example.", "Generated caches obscure the diff."],
    ["Freeze seed and minimize the reproducer.", "Find the earliest shared invariant violation.", "Preserve the interface and patch locally.", "Add a nearby boundary regression.", "Clean caches and review only intentional source changes."],
    "Choose one bug and explain how the first failing test changed your hypothesis. Distinguish evidence observed before and after the patch.",
    "A strong response gives the original hypothesis, cites concrete failure data, explains the invariant that localized the root cause, and names the full-suite evidence after repair.",
)

SPECS["week_14_assignment"] = spec(
    "Week 14 Assignment: Final Project Proposal and Feasibility Checkpoint",
    "A testable plan plus a working end-to-end walking skeleton",
    "Week 14 Assignment",
    "Submit a scoped integration proposal and demonstrate one representative input through the complete pipeline.",
    "Week 14: project design, scope, risk, and checkpoint engineering",
    "5-7 hours", "Proposal, checkpoint code, and short demo evidence", 10,
    [
        "Define a meaningful two-module handoff.",
        "State measurable success and a baseline.",
        "Create milestones for the remaining schedule.",
        "Declare a reduced-scope fallback.",
        "Run an end-to-end checkpoint with an automated assertion.",
    ],
    [
        task(1, "Problem and integration", 3, "Write a concrete problem statement and architecture using at least two course modules.", "Proposal section and interface diagram.", "Need, module roles, behavioral handoff, inputs, and outputs are precise.", [
            part("a", 1, "State the user or research problem and a falsifiable success criterion.", "The statement names the task, representative input, expected output, and a metric or comparison that separates success from failure."),
            part("b", 2, "Describe the cross-module handoff.", "Name component A's output, its shape and semantics, how component B consumes it, and how removing or replacing the handoff changes system behavior."),
        ]),
        task(2, "Evaluation and milestones", 2, "Plan a baseline, metrics, datasets or scenarios, and dated milestones.", "Evaluation table and remaining-day plan.", "Evidence is feasible and milestones have acceptance tests.", [
            part("a", 1, "Define the baseline and two metrics.", "The baseline is runnable under the same conditions; metrics cover correctness and performance or responsibility and have declared aggregation."),
            part("b", 1, "Write at least four milestones as artifact plus acceptance test plus deadline.", "Each milestone can be checked as complete without relying on vague activity descriptions."),
        ]),
        task(3, "Risk and fallback", 2, "Identify the highest-risk dependency and a reduced-scope plan.", "Risk register and fallback trigger.", "Fallback preserves one meaningful integration and has an objective activation condition.", [
            part("a", 1, "Name the dependency, likelihood, impact, and timebox.", "The risk is concrete, such as unfamiliar data or library setup, and the proposal limits investigation to a stated number of hours."),
            part("b", 1, "Specify the fallback and trigger.", "If the walking skeleton or acceptance test misses its deadline, remove a nonessential extension while keeping the core handoff, baseline, and evaluation."),
        ]),
        task(4, "Walking skeleton", 3, "Run one real or representative input through every component.", "Checkpoint script, output evidence, and at least one automated check.", "The pipeline runs without crashing and validates the interface.", [
            part("a", 2, "Demonstrate end-to-end execution and record the exact command.", "The run starts from a clean documented setup, processes a representative input through both module components, and produces the declared output."),
            part("b", 1, "Add a shape, range, legality, or determinism assertion.", "The assertion checks the handoff contract, such as a normalized posterior, legal action, finite feature vector, or expected prediction shape."),
        ]),
    ],
    ["A required dataset is unavailable.", "A new library consumes the timebox.", "The handoff output is nonfinite.", "The baseline cannot run.", "The project uses two modules only side by side."],
    ["Use a permitted synthetic or provided dataset.", "Activate the fallback.", "Fail the checkpoint and repair the producer.", "Reduce scope until a baseline runs.", "Redesign so one output changes the other component's behavior."],
    "Which scope decision most increased the probability of a complete, credible final submission? Cite checkpoint evidence.",
    "A strong response identifies a removed or bounded risk, explains the preserved core learning objective, and cites a passing end-to-end or interface test.",
)

SPECS["week_15_assignment"] = spec(
    "Week 15 Final Project: Submission and Showcase",
    "A complete, tested, integrated, and responsibly documented AI system",
    "Final Project",
    "Deliver the approved cross-module system with reproducible evidence, report, and showcase.",
    "Weeks 1-15 comprehensive integration",
    "20-30 hours across Weeks 14-15", "Tagged repository, report, and live or local demo", 100,
    [
        "Deliver a correct end-to-end system integrating at least two modules.",
        "Provide student-authored unit and integration tests.",
        "Compare against a meaningful baseline with controlled evidence.",
        "Document design, results, limitations, and responsible-use boundaries.",
        "Present a concise reproducible technical demonstration.",
    ],
    [
        task(1, "Technical correctness", 30, "Complete the approved system and verify its core algorithms and interfaces.", "Working tagged code, configuration, and correctness evidence.", "Algorithms, dataflow, edge handling, and reproducibility are correct.", [
            part("a", 15, "Implement the core algorithms and declared module handoff.", "Both techniques are faithful to course definitions, inputs and outputs satisfy the frozen contract, and one component's output materially affects the other."),
            part("b", 10, "Handle boundary and invalid inputs defensively.", "The system validates shapes, ranges, legality, termination, nonfinite values, and missing resources with clear behavior."),
            part("c", 5, "Provide one clean-environment reproduction command.", "A tagged commit plus environment and configuration reproduces the primary output within stated tolerances."),
        ]),
        task(2, "Integration quality", 20, "Demonstrate that the combination is more than two independent components.", "Architecture, contract tests, and ablation.", "The handoff is necessary, justified, and measured.", [
            part("a", 10, "Explain the boundary with shape, units, uncertainty, and failure semantics.", "The report includes an interface diagram and complete contract that another engineer could implement independently."),
            part("b", 10, "Ablate or replace one component and compare behavior.", "The controlled baseline or ablation uses the same data, seed budget, and metric, showing what value or tradeoff the integration creates."),
        ]),
        task(3, "Code quality and tests", 20, "Submit maintainable code and student-authored verification.", "Unit, integration, and regression tests plus README.", "Tests cover core logic, boundaries, and the end-to-end path.", [
            part("a", 10, "Provide focused unit tests for each component.", "Tests include hand-sized oracles and name the defect they detect; stochastic behavior is seeded and tolerances are justified."),
            part("b", 6, "Provide at least one end-to-end integration test.", "A representative input passes through the full handoff and the output is checked for correctness, legality, or a declared invariant."),
            part("c", 4, "Keep repository and APIs readable.", "Modules have clear ownership, public interfaces are documented, commands are current, and secrets or generated caches are absent."),
        ]),
        task(4, "Evaluation and report", 20, "Write a technical report with problem, approach, results, and limitations.", "Versioned report and result artifacts.", "Claims are supported, bounded, and reproducible.", [
            part("a", 8, "Describe the problem, architecture, assumptions, and baseline.", "The narrative identifies stakeholder or research need, module contributions, data or environment, and a fair comparison."),
            part("b", 8, "Report quantitative or structured qualitative results with variability.", "Tables or figures include configurations, sample sizes or seeds, metrics, baseline, and uncertainty or limitations."),
            part("c", 4, "Discuss limitations and what you would do differently.", "The section identifies at least one failed assumption, residual risk, and prioritized next experiment rather than hiding weaknesses."),
        ]),
        task(5, "Showcase and responsibility", 10, "Present a concise demonstration and responsible-use handoff.", "Seven-minute presentation, demo, and risk note.", "The presentation is clear, reproducible, candid, and actionable.", [
            part("a", 5, "Show problem, architecture, fixed demo, and evidence within the time limit.", "The tagged version and representative input are identified; the demo result connects directly to the reported claim."),
            part("b", 5, "State intended use, out-of-scope use, monitoring, fallback, and owner.", "At least one operational risk has a metric, threshold, response, and accountable role."),
        ]),
    ],
    ["The live dependency fails.", "The integrated model underperforms the baseline.", "A test is flaky.", "Results differ across seeds.", "The final scope differs from the approved proposal."],
    ["Use a transparent local or screenshot fallback without fabricating behavior.", "Report the result and analyze why rather than hiding it.", "Control randomness and remove timing assumptions.", "Report variability and bound the claim.", "Document the pivot, rationale, and instructor approval if required."],
    "What is the strongest claim your evidence supports, and what nearby claim does it not support? Explain the most important next experiment.",
    "A strong response states a bounded reproducible claim, identifies a specific unsupported generalization or causal claim, and proposes an experiment that directly reduces that uncertainty.",
    requirements=[
        "Integrate techniques from at least two of Modules A, B, and C through a real behavioral handoff.",
        "Submit student-authored unit and end-to-end tests that pass from the tagged commit.",
        "Provide reproducible data provenance, environment, configuration, seeds, and commands.",
        "Compare against a meaningful baseline or ablation under controlled conditions.",
        "Include an honest limitations section and responsible-use boundaries.",
    ],
)

SPECS["quiz_05"] = spec(
    "Quiz 5: Fairness, Responsibility, and Integration",
    "Weeks 12-13",
    "Quiz 5",
    "Compute group disparities, design a production control, and connect methods across modules.",
    "Weeks 12-13", "35 minutes", "Individual PDF", 20,
    ["Compute group-conditioned rates.", "Compare fairness criteria.", "Distinguish shift and drift.", "Specify an operational monitor.", "Reason across modules."],
    [
        task(1, "Group metrics", 5, "Group A0 has TP=30,FN=10,FP=10,TN=50; A1 has TP=20,FN=20,FP=20,TN=40.", "Rate and gap calculations.", "TPR, FPR, and equalized-odds gaps are correct.", [
            part("a", 2, "Compute each group TPR.", "A0 TPR=30/40=0.75; A1 TPR=20/40=0.50."),
            part("b", 2, "Compute each group FPR.", "A0 FPR=10/60 about 0.1667; A1 FPR=20/60 about 0.3333."),
            part("c", 1, "Report the absolute TPR and FPR gaps.", "The gaps are 0.25 and about 0.1667, so equalized odds is not satisfied."),
        ]),
        task(2, "Criterion choice", 4, "A calibrated risk score is used for limited human review capacity, but group base rates differ.", "Short comparison.", "Calibration and equalized-odds tension is explained.", [
            part("a", 2, "Define calibration within groups.", "Among individuals assigned the same score p in each group, the observed positive frequency should be p."),
            part("b", 2, "Explain why calibration does not guarantee equal error rates.", "With differing base rates and imperfect prediction, a common calibrated score or threshold can yield different FPR and FNR; the criteria condition on different quantities."),
        ]),
        task(3, "Monitoring", 4, "A classifier's input age distribution shifts, while labeled outcomes arrive one month later.", "Control specification.", "Early and delayed evidence are separated.", [
            part("a", 2, "Classify the immediately observable change.", "A change in P(X), here the age distribution, is distribution shift; it does not alone prove concept drift."),
            part("b", 2, "Specify one early monitor and one delayed monitor.", "Track an age-distribution statistic and prediction distribution immediately; when labels mature, recompute overall and group performance such as recall or calibration."),
        ]),
        task(4, "Operational control", 3, "Turn subgroup recall into a complete production control.", "One control tuple.", "Metric, baseline, threshold, window, owner, and action are all present.", [
            part("a", 3, "Write the full control.", "Example: weekly subgroup recall compared with release baseline, alert if absolute drop exceeds 0.08 after at least 100 positives, owned by model-risk lead, action is bounded human review and release investigation."),
        ]),
        task(5, "Cross-module synthesis", 4, "A planner uses a learned heuristic and Bayesian sensor belief.", "Integrated risk analysis.", "At least two module assumptions and one system test are connected.", [
            part("a", 2, "Name one Module A and one Module B/C failure mode.", "The learned heuristic may overestimate and break A-star optimality; a misspecified sensor likelihood may produce a biased posterior; distribution shift may invalidate learned estimates."),
            part("b", 2, "Design one end-to-end test.", "On a small solvable world enumerate the true hidden state and UCS optimal path, feed fixed sensor observations, verify posterior normalization, returned-path legality, and cost or declared bounded-suboptimality."),
        ]),
    ],
    ["Subgroup denominator is zero.", "A monitoring window is too small.", "The heuristic overestimates.", "The sensor observation is impossible."],
    ["Report undefined or the declared safe convention with counts.", "Delay the decision or widen uncertainty.", "Use a safe heuristic or relinquish optimality explicitly.", "Trigger the model's impossible-evidence policy."],
    "State one place where a numerical result still requires professional judgment.",
    "A full-credit sentence identifies a fairness tradeoff, threshold, release decision, or response choice and names the stakeholders or harm that mathematics alone cannot resolve.",
    requirements=["Work independently.", "Show all rate calculations.", "State metric conventions.", "No electronic communication."],
    submission_steps=["Write your name and assumptions.", "Show intermediate counts and denominators.", "Submit only the completed response PDF."],
)
