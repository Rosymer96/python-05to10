from ex0.factory import CreatureFactory
from .healing_creatures import Bloomelle, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
