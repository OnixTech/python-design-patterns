from abc import ABC, abstractmethod
from .creatures import Creature, Flamiling, Pyrodon, Aquabub, Torragon


class CreateFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> creature:
        pass

class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_envolved(self) -> Creature:
        return Pyrodon()


class AquaFactory()
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
