from .creature import Creature
from .creature import Aquabub
from .creature import Torragon
from .factory import CreatureFactory


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
