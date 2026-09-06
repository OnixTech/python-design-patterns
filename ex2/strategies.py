from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability

from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> None:
        if hasattr(creature, "transform"):
            return hasattr(creature, "revert")
        return False

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Creature cannot use DefensiveStrategy"
                    )

        return [
                creature.transform(),
                creature.attack(),
                creature.revert(),
            ]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")
 
    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Creature cannot use DefensiveStrategy"
                    )
        return [creature.attack(), creature.heal()]
