"""Contract tests for the Week 1 grid-problem reference solution."""

import unittest

from src.problem import Action, GridProblem


class GridProblemTests(unittest.TestCase):
    """Verify normal, boundary, illegal, and malformed cases."""

    def setUp(self) -> None:
        self.problem = GridProblem(
            rows=3,
            columns=3,
            start=(0, 0),
            goal=(2, 2),
            blocked=frozenset({(1, 1)}),
        )

    def test_corner_actions_are_deterministic(self) -> None:
        self.assertEqual(
            self.problem.actions((0, 0)),
            [Action.DOWN, Action.RIGHT],
        )

    def test_known_transition_and_cost(self) -> None:
        next_state = self.problem.result((0, 0), Action.RIGHT)
        self.assertEqual(next_state, (0, 1))
        self.assertEqual(
            self.problem.step_cost((0, 0), Action.RIGHT, next_state),
            1.0,
        )

    def test_blocked_and_outside_moves_are_absent(self) -> None:
        self.assertEqual(
            self.problem.actions((1, 0)),
            [Action.UP, Action.DOWN],
        )

    def test_illegal_action_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.problem.result((0, 0), Action.UP)
        with self.assertRaises(TypeError):
            self.problem.result((0, 0), "RIGHT")  # type: ignore[arg-type]

    def test_goal_test_and_hashability(self) -> None:
        self.assertFalse(self.problem.goal_test((0, 0)))
        self.assertTrue(self.problem.goal_test((2, 2)))
        explored = {(0, 0), (0, 1)}
        self.assertIn((0, 1), explored)

    def test_one_cell_grid_has_no_actions(self) -> None:
        problem = GridProblem(1, 1, (0, 0), (0, 0))
        self.assertEqual(problem.actions((0, 0)), [])
        self.assertTrue(problem.goal_test((0, 0)))

    def test_malformed_and_blocked_states_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.problem.goal_test((3, 0))
        with self.assertRaises(TypeError):
            self.problem.goal_test([0, 0])  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            self.problem.actions((1, 1))

    def test_incorrect_next_state_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.problem.step_cost((0, 0), Action.RIGHT, (0, 0))


if __name__ == "__main__":
    unittest.main()

