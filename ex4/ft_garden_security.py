#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def set_height(self, val: int) -> None:
        if val < 0:
            print_errors(val, "height", "cm")
        else:
            self._height = val
            print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, val: int) -> None:
        if val < 0:
            print_errors(val, "age", "days")
        else:
            self._age = val
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current plant: {self._name} ({self.get_height()}cm,"
              f" {self.get_age()} days)")


def plant_factory(name: str, height: int, age: int) -> Plant:
    print(f"Plan created: {name}")
    return Plant(name, height, age)


def print_errors(val: int, type: str, aux: str) -> None:
    print(f"Invalid operation attemped: {type} {val}{aux} [REJECTED]")
    print(f"Security: Negative {type} rejected")


def main() -> None:
    print("=== Garden Security System ===")
    rose = plant_factory("Rose", 10, 5)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.get_info()


if __name__ == "__main__":
    main()
