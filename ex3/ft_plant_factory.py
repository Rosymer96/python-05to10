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
    print("=== Plant Factory Output ===")
    rose = plant_factory("Rose", 25, 30)
    oak = plant_factory("Oak", 200, 365)
    cactus = plant_factory("Cactus", 5, 90)
    sunflower = plant_factory("Sunflower", 80, 45)
    fern = plant_factory("Fern", 15, 120)
    garden = [rose, oak, cactus, sunflower, fern]
    for plant in garden:
        garden_len += 1

    print(f"\nTotal plants created: {garden_len}")


if __name__ == "__main__":
    main()
