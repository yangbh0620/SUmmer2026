"""Validated gridworld problem representation for the Week 1 lab."""

from __future__ import annotations

from enum import Enum
from typing import TypeAlias

State: TypeAlias = tuple[int, int]


class Action(Enum):
    """The four deterministic grid movements."""

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class GridProblem:
    """A finite rectangular grid problem with unit-cost legal transitions."""

    ACTION_ORDER = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)

    def __init__(
        self,
        rows: int,
        columns: int,
        start: State,
        goal: State,
        blocked: frozenset[State] = frozenset(),
    ) -> None:
        if rows < 1 or columns < 1:
            raise ValueError("grid dimensions must be positive")
        self.rows = rows
        self.columns = columns
        self.start = start
        self.goal = goal
        self.blocked = frozenset(blocked)

        self._validate_state(start)
        self._validate_state(goal)
        for state in self.blocked:
            self._validate_coordinate(state)
        if start in self.blocked or goal in self.blocked:
            raise ValueError("start and goal must be traversable")

    def _validate_coordinate(self, state: State) -> None:
        if (
            not isinstance(state, tuple)
            or len(state) != 2
            or any(type(value) is not int for value in state)
        ):
            raise TypeError("state must be a tuple of two integers")
        row, column = state
        if not (0 <= row < self.rows and 0 <= column < self.columns):
            raise ValueError(f"state is outside the grid: {state}")

    def _validate_state(self, state: State) -> None:
        self._validate_coordinate(state)
        if state in self.blocked:
            raise ValueError(f"state is blocked: {state}")

    def initial_state(self) -> State:
        """Return the immutable initial state."""
        return self.start

    @staticmethod
    def _destination(state: State, action: Action) -> State:
        delta_row, delta_column = action.value
        return state[0] + delta_row, state[1] + delta_column

    def actions(self, state: State) -> list[Action]:
        """Return legal actions in deterministic order."""
        self._validate_state(state)
        legal: list[Action] = []
        for action in self.ACTION_ORDER:
            candidate = self._destination(state, action)
            try:
                self._validate_state(candidate)
            except ValueError:
                continue
            legal.append(action)
        return legal

    def result(self, state: State, action: Action) -> State:
        """Return a new state for a legal action."""
        self._validate_state(state)
        if not isinstance(action, Action):
            raise TypeError("action must be an Action value")
        if action not in self.actions(state):
            raise ValueError(f"illegal action {action.name} at {state}")
        return self._destination(state, action)

    def goal_test(self, state: State) -> bool:
        """Return whether a validated state equals the configured goal."""
        self._validate_state(state)
        return state == self.goal

    def step_cost(
        self,
        state: State,
        action: Action,
        next_state: State,
    ) -> float:
        """Return unit cost only for the matching legal transition."""
        expected = self.result(state, action)
        self._validate_state(next_state)
        if next_state != expected:
            raise ValueError(
                f"{next_state} is not the result of {action.name} at {state}"
            )
        return 1.0

