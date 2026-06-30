#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height, False)
        self.set_age(age, False)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age}"
              f" days old")

    def set_height(self, val: float, print_set: bool = True) -> None:
        if val < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = val
            if print_set:
                print(f"Height updated: {self._height}cm")

    def set_age(self, val: int, print_set: bool = True) -> None:
        if val < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = val
            if print_set:
                print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def current_state(self) -> None:
        print("Current state: ", end="")
        self.show()


def plant_factory(name: str, height: int, age: int) -> Plant:
    new_plant = Plant(name, height, age)
    print("Plant created: ", end="")
    new_plant.show()
    return new_plant


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
    rose.current_state()


if __name__ == "__main__":
    main()
