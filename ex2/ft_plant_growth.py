#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def grow(self, amount: int) -> None:
        self.height += amount

    def age(self, days: int) -> None:
        self.days += days

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30)
    grow_days = 6
    garden: list[Plant] = []
    garden.append(rose)
    print("=== Day 1 ===")
    for plant in garden:
        plant.get_info()
        for _ in range(grow_days):
            plant.grow(1)
            plant.age(1)
    print(f"=== Day {1 + grow_days} ===")
    for plant in garden:
        plant.get_info()
    print(f"Growth this week: +{grow_days}cm")


if __name__ == "__main__":
    main()
