#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = height
        self.age: int = age


def plant_factory(name: str, height: float, age: int) -> Plant:
    print(f"Created: {name}: {round(float(height), 1)}cm, {age} days old")
    return Plant(name, height, age)


def main() -> None:
    data = (
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    )
    print("=== Plant Factory Output ===")
    garden = []
    for name, height, age in data:
        plant = plant_factory(name, height, age)
        garden += [plant]


if __name__ == "__main__":
    main()
