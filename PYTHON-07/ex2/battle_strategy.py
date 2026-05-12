from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from abc import ABC, abstractmethod
from typing import cast


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [
            creature.attack()
            ]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature._name}'"
                                       f" for this aggressive strategy")
        transformer = cast(TransformCapability, creature)
        return [
            transformer.transform(),
            creature.attack(),
            transformer.revert()
            ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature._name}'"
                                       f" for this defensive strategy")
        healer = cast(HealCapability, creature)
        return [
            creature.attack(),
            healer.heal()
            ]
