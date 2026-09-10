# Rational Agents and Problem Solving as Search - Video Script

**Course:** CMPSC 480 - AI Curriculum Engineering
**Unit:** Week 1, Lesson 2
**Target duration:** Approximately 50 minutes
**Format:** Narration script only; no video or audio is produced.

## Production Notes

- Use the matching PowerPoint slide number shown in each section.
- Read equations deliberately and define every symbol on first use.
- Pause after checkpoint questions before discussing the instructor guidance.
- On-screen emphasis cues are optional and must not change the slide content.

## Slide 1 - Opening

**Suggested pacing:** 2 minutes
**Visual cue:** Emphasize the sequence specification, representation, and search.

Today we establish the vocabulary and abstraction that will organize all of Module A. An intelligent system does not begin with a search algorithm. It begins with a task: what observations are available, what actions can change the environment, and what outcome counts as good performance? We will use the PEAS framework to make that task explicit. We will then classify the environment, select an appropriate agent architecture, and translate the resulting description into a formal search problem. That translation matters because breadth-first search, depth-first search, uniform-cost search, Greedy Best-First Search, A-star, minimax, and alpha-beta pruning all explore structured state spaces. Their differences become clearer once the common problem representation is stable. By the end of the lesson, you should be able to move from an informal product story to a precise Problem interface whose states, actions, transitions, goals, and costs can be implemented and tested.

## Slide 2 - Learning objectives

**Suggested pacing:** 2 minutes
**Visual cue:** Reveal the objectives in order and identify the two translation objectives.

The first objective gives us a precise language for discussing behavior without treating intelligence as magic. The next two objectives concern task specification. PEAS records what success means and what interface connects the agent to its world, while environment properties identify uncertainty, time, and interaction constraints. The fourth objective concerns architecture: different agent types retain different internal information and optimize different kinds of criteria. The final two objectives make the engineering transition. You will express a search problem as a formal tuple and as methods with enforceable contracts, then recognize why a path tree can contain many copies of one world state. These objectives are cumulative. If the performance measure is vague, rationality is vague. If state equality is vague, graph search is unsafe. If transitions and costs are underspecified, no frontier policy can repair the model. We therefore move from specification to formalization before discussing algorithm details.

## Slide 3 - An agent maps percept history to action

**Suggested pacing:** 3 minutes
**Visual cue:** Read the function signature, then contrast rationality with omniscience.

Formally, an agent function maps every possible finite percept history to an action. A percept is the information delivered by sensors at one moment; a percept sequence records what has been observed so far. The agent program is the concrete implementation of this abstract function on an architecture with finite memory and computation. Rationality is evaluated relative to four things: the performance measure, the percept history, the agent's prior knowledge, and the actions it can take. A rational agent selects the action that maximizes expected performance under that information. It need not know the true future, and a poor outcome does not prove the earlier choice irrational. Omniscience would require knowing the actual consequences of every action before acting, which is unavailable in realistic environments. Key takeaway: always judge an agent against an explicit measure and information set, not against hindsight.

## Slide 4 - PEAS specifies the task before the implementation

**Suggested pacing:** 3 minutes
**Visual cue:** Move through PEAS from left to right, then return to Performance.

PEAS stands for Performance measure, Environment, Actuators, and Sensors. The order matters. Begin with performance, because an agent cannot be rational until good behavior is defined. Include priorities and penalties rather than a single attractive metric. A delivery robot might value successful delivery, safety, timeliness, energy use, and avoidance of disruption. The environment lists the entities and processes that influence outcomes, including people and other agents. Actuators describe how the system can intervene; sensors describe what evidence is available and with what limitations. This specification exposes mismatches early. A performance requirement for avoiding fragile objects is not actionable if no sensor can detect them. A route planner cannot promise real-time response if observations arrive minutes late. Key takeaway: PEAS prevents an implementation from quietly inventing a different task than the one stakeholders intended.

## Slide 5 - Worked PEAS: campus delivery robot, part I

**Suggested pacing:** 3 minutes
**Visual cue:** Ask which performance terms conflict and how priorities should be encoded.

This delivery robot is nontrivial because the performance measure is multi-objective and the environment changes. Correct delivery is necessary but insufficient. A robot that arrives quickly by endangering pedestrians is unacceptable, so safety must dominate ordinary efficiency. Energy, distance, and timeliness can be optimized subject to those constraints. The environment includes physical infrastructure and moving participants, but also network services and institutional rules. Those elements can affect available actions and observations. A closed door may remove a transition; a wireless outage may make authorization uncertain. Notice that PEAS is more specific than a product slogan such as deliver packages autonomously. It identifies quantities and constraints that later become costs, hard validity checks, or escalation conditions. Key takeaway: performance is a prioritized contract, while the environment defines the sources of state, change, and uncertainty that the contract must address.

## Slide 6 - Worked PEAS: campus delivery robot, part II

**Suggested pacing:** 3 minutes
**Visual cue:** Connect each sensor to a decision and each actuator to a safety constraint.

Actuators and sensors form the executable boundary of the agent. Driving and steering create motion, but braking and holding position are equally important actions because safe inaction may be rational. Signaling and escalation allow the robot to coordinate with people rather than treating every uncertainty as a path-planning problem. Sensors combine local physical measurements with network information. Each observation has accuracy, latency, and failure modes. GNSS can be unreliable near buildings; a camera can be occluded; a map can be stale; a message can arrive late. The agent therefore reasons over an estimate of the world rather than direct access to reality. The actuator list also reveals feasibility. A planner should not produce a transition through a locked door unless the platform can request access. Key takeaway: a specification is complete only when every planned decision can be supported by observations and every chosen action can be executed through a real interface.

## Slide 7 - Environment properties determine what memory is needed

**Suggested pacing:** 3 minutes
**Visual cue:** Use the robot to illustrate partial observability, stochasticity, and dynamics.

These three dimensions tell us whether a current percept is enough and whether a fixed plan can be trusted. In a fully observable environment, the sensors expose all state variables relevant to the next decision. Partial observability requires memory or a belief about hidden state. Deterministic transitions assign one successor to each legal state-action pair, whereas stochastic transitions assign a distribution. Strategic uncertainty is different: another decision maker chooses actions in response to ours, which motivates adversarial search. Static environments do not change while the agent deliberates. Dynamic ones do, so computation time becomes part of action quality. The delivery robot is partially observable because intent and occluded hazards are hidden, stochastic because motion and observation have uncertainty, and dynamic because people move during planning. Key takeaway: environment classification is not decoration; it identifies the information and temporal assumptions an algorithm must satisfy.

## Slide 8 - Environment properties also shape the objective

**Suggested pacing:** 3 minutes
**Visual cue:** Contrast a spam classifier, a robot route, and a two-player game.

An episodic task allows each decision to be evaluated independently, as in classifying isolated images under a fixed distribution. A sequential task couples choices across time: entering a corridor changes which destinations remain reachable and how much battery remains. Discrete models have enumerable states or actions, while continuous models include real-valued quantities such as speed and steering angle. Engineers often discretize continuous variables, gaining tractability while introducing approximation error that must be acknowledged. Finally, multiple participants may cooperate or compete. A single-agent abstraction can still contain moving people, but it does not model them as optimizing against the agent. Minimax becomes appropriate only when opponent choices are represented strategically. Key takeaway: classification should follow the modeled decision process, not the superficial appearance of the application. The same physical system can support different models for different questions.

## Slide 9 - Checkpoint: classify the robot's environment

**Suggested pacing:** 3 minutes
**Visual cue:** Pause for 45 seconds before discussing the expected classification.

The expected classification is partially observable, stochastic, dynamic, and sequential. Nearby sensing does not reveal the complete relevant state. Motion noise makes the transition outcome uncertain. Pedestrians can change the environment while computation occurs. Each delivery consumes battery and changes later feasibility, so decisions are temporally coupled. The domain also mixes continuous physical motion with a discrete planning abstraction, so either discrete or continuous may be a defensible answer if the representation is stated. Multi-agent classification depends on whether pedestrians are modeled as strategic decision makers or as stochastic environment dynamics. This is the important reasoning habit: classifications are claims about a model. They should be justified from the variables, transition assumptions, and objectives in that model. A label without those assumptions is not yet an engineering decision.

## Slide 10 - Agent architectures add information and decision power

**Suggested pacing:** 3 minutes
**Visual cue:** Describe what new internal element appears in each column.

A simple reflex agent selects actions from rules conditioned on the current percept. It can be appropriate when the relevant state is fully visible and the response is local. A model-based reflex agent maintains an internal estimate using knowledge of how the world changes and how observations relate to world state. This memory supports decisions under partial observability, although the action may still come from rules. A goal-based agent introduces an explicit set of desirable states and considers future consequences. Search becomes useful because the agent must compare action sequences that may or may not reach a goal. Each architecture strictly changes what information is represented and how decisions are justified. More expressive is not automatically better; additional models and planning require computation and introduce new failure modes. Key takeaway: select the least complex architecture that can represent the information and objective required by the task.

## Slide 11 - Utility resolves tradeoffs that a goal test cannot

**Suggested pacing:** 3 minutes
**Visual cue:** Use two safe deliveries with different delay and energy outcomes.

A goal test answers a Boolean question: is this state acceptable? That is enough when all successful outcomes are equivalent or when a separate path-cost model orders plans. Utility is more general. A utility function assigns relative value to outcomes, allowing the agent to trade timeliness against energy, comfort, risk, or other quantities. Under uncertainty, a utility-based agent can compare distributions through expected utility rather than pretending that one predicted outcome is certain. This power creates a specification burden. We must determine whose preferences the utility represents, how incompatible objectives are scaled, and which safety constraints remain hard rather than tradable. A robot should not exchange a large collision risk for a small time saving merely because weights were chosen carelessly. Key takeaway: goals identify acceptable destinations; utility represents preference among consequences, especially when quality varies or outcomes are uncertain.

## Slide 12 - Checkpoint: choose an agent architecture

**Suggested pacing:** 2 minutes
**Visual cue:** Accept a layered answer and ask students to name the dominant architecture.

The strongest description is utility-based with a model-based state estimate. Heat loss and delayed actuator effects require a model of how temperature evolves. A simple reflex rule such as heat when cold can work in a limited setting, but it does not represent delayed dynamics, energy price, or the difference between several comfortable trajectories. A goal-based controller could maintain temperature inside a range, yet it would treat all in-range outcomes as equivalent unless cost is added. Utility can rank energy consumption, comfort deviation, and perhaps actuator wear while hard constraints prevent unsafe temperatures. Agent types are best understood as layers rather than exclusive product categories. A utility-based agent normally contains a state representation and a predictive model as part of its decision process.

## Slide 13 - A search problem has five operational components

**Suggested pacing:** 4 minutes
**Visual cue:** Point to each tuple component and distinguish step cost c from path cost g.

A search problem converts an agent's planning task into five operational components over a state set S. The initial state s zero describes where planning begins. ACTIONS maps a state to its legal choices. RESULT maps a legal state-action pair to a successor state. The goal test decides whether a state satisfies the objective. The step-cost function assigns a positive cost to a legal transition, and path cost g is the sum of those steps from the initial state. Some texts combine actions and result into a successor function, but the engineering obligations remain the same. A state is not merely a snapshot of visible data. It must include enough information for future legality, goal status, and cost to depend only on that state and the chosen action. If battery level affects reachability, omitting battery from state makes the model inconsistent. Key takeaway: a valid state is a sufficient summary for the planning model.

## Slide 14 - Worked formalization: blocked gridworld

**Suggested pacing:** 4 minutes
**Visual cue:** Trace the example path and ask whether a shorter legal path can exist.

This gridworld makes every component concrete. A state is an immutable coordinate tuple within the grid and not in the blocked set. The initial state is zero comma zero. The action function filters the four candidate directions so that a move neither leaves the grid nor enters the blocked cell. RESULT adds the action's displacement to the current coordinate. The goal test compares the state with two comma three. Unit step cost makes path cost equal the number of moves. The displayed route moves across the top row and then down twice, so its cost is five. Manhattan distance between start and goal is also five, and the obstacle does not block this route, proving that no shorter path exists under four-direction motion. Key takeaway: a worked formalization should let another engineer implement and test every operation without guessing an unstated rule.

## Slide 15 - The formal tuple becomes a Problem interface

**Suggested pacing:** 3 minutes
**Visual cue:** Connect each formal component to a method and one testable property.

The Week 1 code lab asks you to preserve the formal semantics in an executable interface. The initial state should be immutable and validated because search algorithms will store it in frontier or explored structures. ACTIONS should return legal actions in a documented deterministic order, which makes traces and tests reproducible. RESULT should create a new state and reject an action that is not legal for the supplied state; silently leaving the state unchanged would hide a caller defect. The goal test should return a Boolean, not an arbitrary truthy object, and should reject malformed states rather than treating them as ordinary non-goals. Step cost should validate that the proposed successor is the result of the action. Key takeaway: every mathematical noun becomes a data contract, and every mathematical function becomes behavior that can be challenged with normal, boundary, and invalid inputs.

## Slide 16 - Search trees represent paths; search graphs deduplicate states

**Suggested pacing:** 4 minutes
**Visual cue:** Draw attention to node identity versus state identity.

A search-tree node represents a path, not only a world state. It normally stores a state, parent reference, generating action, depth, and accumulated path cost. Two different paths can therefore produce two different nodes with equal states. Without recognition, reversible actions can generate an infinite tree even when the underlying state graph is finite. Graph search uses state equality to avoid repeating work, typically with an explored set and some form of frontier membership tracking. This improves performance but introduces policy questions. If a state is rediscovered through a cheaper path, cost-based algorithms may need to replace or reopen a node. State keys must have stable equality and hashing; mutating a key after insertion can make membership incorrect. Key takeaway: the tree is a structure of candidate paths, while the graph is the domain's state connectivity. Correct code must not confuse those identities.

## Slide 17 - Generic graph search separates control from ordering

**Suggested pacing:** 4 minutes
**Visual cue:** Trace one loop iteration, then identify what the frontier controls.

This preview intentionally leaves the frontier policy abstract. The Problem object supplies legal domain behavior. A node records one candidate path and its accumulated metadata. The frontier determines which node is removed next, while the explored set prevents repeated expansion of the same state under the chosen policy. The add-or-update operation signals an important issue for cost-based algorithms: rediscovering an existing state through a better path may require replacement rather than unconditional rejection. Different algorithms will refine these details, and adversarial search will use a different backup structure, but the separation remains useful. Failure must also be explicit so that it cannot be confused with the valid empty solution when the initial state is already a goal. Key takeaway: a reusable search engine depends on a precise Problem contract and makes ordering a policy rather than scattering it through domain code.

## Slide 18 - Frontier policy is the unifying thread of Module A

**Suggested pacing:** 3 minutes
**Visual cue:** State the priority expression for UCS, Greedy, and A-star aloud.

The algorithms ahead are not arbitrary names to memorize. Breadth-first search orders candidates by shallowest depth, while depth-first search follows the most recently generated path. Uniform-cost search prioritizes accumulated path cost g. Greedy Best-First Search prioritizes only a heuristic estimate h of remaining cost. A-star combines evidence already paid with an estimate still to come, using g plus h. Adversarial procedures explore game states and back up values according to who controls each choice; alpha-beta pruning avoids branches that cannot change the minimax decision. These procedures differ in guarantees and details, but each manages which part of a state space to examine and what information guides that order. Key takeaway: keep the domain model stable, then compare algorithms by frontier or backup policy, duplicate handling, information requirements, and resulting guarantees.

## Slide 19 - Checkpoint: repair an incomplete formalization

**Suggested pacing:** 3 minutes
**Visual cue:** Pause, then build the tuple state one field at a time.

Location alone is not sufficient because two visits to the same location can have different legal futures and costs. Time influences toll price and perhaps road availability; remaining charge determines which destinations are reachable. ACTIONS, RESULT, and step cost would therefore depend on hidden path history rather than only on the stored state. One valid discrete representation might be a tuple containing location identifier, time interval, and integer charge level. A continuous model could use real-valued time and energy, but hashing and equality would need careful design or discretization. The general test is Markov sufficiency for the planning abstraction: given the state and an action, can the model determine the successor distribution, goal status, and relevant cost without consulting the full prior path? If not, the state has omitted information or the model must explicitly retain history.

## Slide 20 - Key terms: behavior and environment

**Suggested pacing:** 2 minutes
**Visual cue:** Use the glossary as a rapid retrieval check rather than reading every line.

Use these terms precisely in assignments and design documents. A percept is one observation, whereas a percept sequence is the information history available to an agent function. Rationality is relative to expected performance under evidence, not guaranteed success. Utility ranks outcomes; it is not synonymous with reward unless the model defines that relationship. Environment labels describe the decision model. Observable does not mean every physical fact is visible, only that the state variables relevant to the modeled decision are available. Deterministic means the modeled successor is fixed by state and action. Sequential means an action changes later decision conditions. Dynamic means the world can change during deliberation. A concise definition should always be followed by the operational consequence: memory, probability, real-time response, or strategic reasoning.

## Slide 21 - Key takeaways

**Suggested pacing:** 2 minutes
**Visual cue:** Connect each takeaway to one artifact students can inspect in code.

The disciplined sequence is now visible. Begin with PEAS so that success, environment, actions, and observations are explicit. Classify the environment to determine whether the agent needs state estimation, uncertainty modeling, real-time response, or strategic reasoning. Select an architecture that can represent the objective without unnecessary complexity. For planning, define the initial state, legal actions, transition model, goal test, and costs. Ensure that state contains enough information for the model and has stable equality when graph search will deduplicate it. Keep node identity separate from state identity. Finally, view Module A algorithms as policies for exploring and evaluating the same underlying state-space abstraction. This perspective will let us compare guarantees rather than memorize disconnected procedures. Your Week 1 lab makes the abstraction executable; Week 2 will place concrete frontier policies on top of it.

## Slide 22 - Check your understanding

**Suggested pacing:** 3 minutes
**Visual cue:** Assign one question per small group, then solicit one-sentence answers.

Use these questions to test transfer rather than recognition. The first asks you to distinguish expected choice quality from realized luck. The PEAS question requires a complete task specification, including review quality, repository context, comment actions, and code or test observations. Online chess is fully observable with respect to the board, strategic rather than stochastic under the game model, sequential, semidynamic when clocks matter, discrete, and multi-agent. The vacuum-world formalization should define a compact state containing agent location and the cleanliness of both rooms, together with legal actions, transitions, a goal test, and costs. The search-tree question targets repeated paths and reversible actions. Safe explored-set use requires immutable state keys, stable value equality and hashing, and a duplicate policy consistent with the algorithm's cost guarantees. If any answer depends on an assumption, state it explicitly.

## Reference Notes

- Repository prompt: week_01/Week_1_Lesson_2_Rational_Agents_and_Problem_Solving_as_Search.md
- Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 4th edition, Chapters 2-3.

**Approximate narration word count:** 3057
