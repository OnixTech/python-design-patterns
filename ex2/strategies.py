from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability

from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Creature cannot use AggressiveStrategy"
                    )

        transformer = cast(TransformCapability, creature)

        return [
                transformer.transform(),
                creature.attack(),
                transformer.revert(),
            ]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Creature cannot use DefensiveStrategy"
                    )

        healer = cast(HealCapability, creature)

        return [creature.attack(), healer.heal()]
