from abc import ABC, abstractmethod

class Creature(ABC):
    @abstractmethod
    def attack() -> None:
        pass
        

    def describe() -> str:
        