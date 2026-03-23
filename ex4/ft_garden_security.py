#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: float, age: int):
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def set_height(self, val: float) -> None:
        if val < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = val
            print(f"Height updated: {self._height}cm")

    def set_age(self, val: int) -> None:
        if val < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age updated rejected")
        else:
            self._age = val
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current state: {self._name}: {round(float(self._height), 1)}"
              f"cm, {self._age} days old")


def plant_factory(name: str, height: int, age: int) -> SecurePlant:
    print(f"Plant created: {name}: {round(float(height), 1)}cm, "
          f"{age} days old")
    return SecurePlant(name, height, age)


def main() -> None:
    print("=== Garden Security System ===")
    rose = plant_factory("Rose", 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-10)
    print()
    rose.get_info()


if __name__ == "__main__":
    main()
