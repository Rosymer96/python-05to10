#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{self.get_height()}cm, {round(self.get_age(), 1)} days old")

    def act(self) -> None:
        pass


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str,
            bloom: bool = False
            ):
        super().__init__(name, height, age)
        self._color: str = color
        self._bloom: bool = bloom

    def get_info(self) -> None:
        super().get_info()
        print(f" Color: {self._color}")
        if self._bloom is False:
            print(f"{self._name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True
        self.get_info()
        print(f"{self._name.capitalize()} is blooming beautifully!")

    def act(self) -> None:
        self.bloom()


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float,
            ):
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter

    def get_info(self) -> None:
        super().get_info()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")

    def act(self) -> None:
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int = 0
            ):
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def get_info(self) -> None:
        super().get_info()
        print(f" Harvest season: {self._harvest_season}")

    def act(self) -> None:
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:

    rose = Flower("rose", 15.00, 10, "red")
    oak = Tree("oak", 200.00, 365, 5.00)
    tomato = Vegetable("tomato", 5.00, 10, "April")
    print("=== Garden Plant Types ===\n")
    print("=== Flower")
    rose.get_info()
    rose.bloom()
    print()
    print("=== Tree")
    oak.get_info()
    print()
    print("=== Vegetable")
    tomato.get_info()


if __name__ == "__main__":
    main()
