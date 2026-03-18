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
    week_days = 7
    garden = [Plant("Rose", 25, 30)]
    print("=== Day 1 ===")
    for plant in garden:
        plant.get_info()
    for plant in garden:
        for _ in range(1, week_days):
            plant.grow(1)
            plant.age(1)
    print("=== Day 7 ===")
    for plant in garden:
        plant.get_info()
    print("Growth this week: +6cm")


if __name__ == "__main__":
    main()
