#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height, False)
        self.set_age(age, False)

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

    def grow(self, cm: float) -> None:
        self.set_height(self._height + cm, False)

    def age(self, days: int) -> None:
        self.set_age(self._age + days, False)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height:.1f}cm, {self._age}"
              f" days old")


class Flower(Plant):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            color: str,
            bloom: bool = False
            ) -> None:
        super().__init__(name, _height, _age)
        self.color: str = color
        self.is_bloom: bool = bloom

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloom is False:
            print(f"{self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.is_bloom = True
        self.show()


class Tree(Plant):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            trunk_diameter: float,
            ) -> None:
        super().__init__(name, _height, _age)
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self._height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            _height: float,
            _age: int,
            harvest_season: str,
            nutritional_value: int = 0
            ) -> None:
        super().__init__(name, _height, _age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def grow(self, cm: float) -> None:
        super().grow(cm)

    def grow_and_age(self, cm: float, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self.age(days)
        self.grow(cm)
        self.show()


def main() -> None:

    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", 200, 365, 5)
    tomato = Vegetable("tomato", 5, 10, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    tomato.grow_and_age(42, 20)


if __name__ == "__main__":
    main()
