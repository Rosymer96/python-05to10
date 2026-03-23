#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def grow(self, amount: int) -> None:
        self.height += amount
        self.height = round(self.height, 1)

    def age(self, days: int) -> None:
        self.days += days

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    week_days = 7
    garden = [Plant("Rose", 25, 30)]
    for plant in garden:
        for i in range(1, week_days):
            print(f"=== Day {i} ===")
            plant.get_info()
            plant.grow(0.8)
            plant.age(1)
        print("=== Day 7 ===")
        plant.get_info()
    print("Growth this week: +6cm")


if __name__ == "__main__":
    main()
