from .creature import Creature
from .creature import Flameling
from .creature import Pyrodon
from .factory import CreatureFactory


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()
