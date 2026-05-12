from ex0.factory import CreatureFactory
from .transform_creatures import Morphagon
from .transform_creatures import Shiftling


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
