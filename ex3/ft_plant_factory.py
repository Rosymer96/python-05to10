#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def plant_factory(name: str, height: int, age: int) -> Plant:
    return Plant(name, height, age)


def main() -> None:
    garden: list[Plant] = []
    data: list[tuple[str, int, int]] = [
        ("Rose", 25, 30), ("Oak", 200, 365),
        ("Cactus", 5, 90), ("Sunflower", 80, 45), ("Fern", 15, 120)]
    for name, height, age in data:
        new_plant = plant_factory(name, height, age)
        garden.append(new_plant)
    for plant in garden:
        plant.get_info()
    print(f"Total plants created: {len(garden)}")


if __name__ == "__main__":
    main()
