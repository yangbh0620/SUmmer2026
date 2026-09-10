"""Generic agent contract used by later search implementations."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

PerceptT = TypeVar("PerceptT")
ActionT = TypeVar("ActionT")


class Agent(ABC, Generic[PerceptT, ActionT]):
    """Base interface for agents that map percepts to actions."""

    @abstractmethod
    def act(self, percept: PerceptT) -> ActionT:
        """Return the next action for the supplied percept."""
        raise NotImplementedError

