#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


def plant_factory(name: str, height: int, age: int) -> Plant:
    print(f"Created: {name} ({height}cm, {age} days)")
    return Plant(name, height, age)


def main() -> None:
    garden_len = 0
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
    for plant in garden:
        garden_len += 1

    print(f"\nTotal plants created: {garden_len}")


if __name__ == "__main__":
    main()
