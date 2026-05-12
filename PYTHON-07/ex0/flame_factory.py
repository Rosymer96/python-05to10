from .creature import Flameling
from .creature import Pyrodon
from .factory import CreatureFactory


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()
