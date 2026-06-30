#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_in_days: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_in_days}"
              f" days old")

    def grow(self, amount: float) -> None:
        self.height += amount
        self.height = self.height

    def age(self, days: int) -> None:
        self.age_in_days += days


def plant_factory(name: str, height: float, age: int) -> Plant:
    new_plant = Plant(name, height, age)
    return new_plant


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = plant_factory("Rose", 25, 30)
    oak = plant_factory("Oak", 200, 365)
    cactus = plant_factory("Cactus", 5, 90)
    sunflower = plant_factory("Sunflower", 80, 45)
    fern = plant_factory("Fern", 15, 120)
    garden = [rose, oak, cactus, sunflower, fern]
    for plant in garden:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
