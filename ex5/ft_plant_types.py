#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"{self._name} ({self.__class__.__name__}): "
              f"{self.get_height()}cm, {self.get_age()} days",
              end="")

    def act(self) -> None:
        pass


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            ):
        super().__init__(name, height, age)
        self._color: str = color

    def get_info(self) -> None:
        super().get_info()
        print(f", {self._color} color")

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def act(self) -> None:
        self.bloom()


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int,
            shade: int
            ):
        super().__init__(name, height, age)
        self._trunk_diameter: int = trunk_diameter
        self._shade: int = shade

    def get_info(self) -> None:
        super().get_info()
        print(f", {self._trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self._name} provides {self._shade} "
              f"square meters of shade")

    def act(self) -> None:
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def get_info(self) -> None:
        super().get_info()
        print(f", {self._harvest_season} harvest")

    def act(self) -> None:
        print(f"{self._name} is rich in {self._nutritional_value}")


def main() -> None:
    garden = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50, 78),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Flower("Sunflower", 10, 5, "yellow"),
        Tree("Pine", 200, 250, 40, 53),
        Vegetable("Carrot", 30, 70, "spring", "vitamin A"),
    ]
    print("=== Garden Plant Types ===\n")
    for plant in garden:
        plant.get_info()
        plant.act()
        print()


if __name__ == "__main__":
    main()
