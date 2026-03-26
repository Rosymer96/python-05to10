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
        self.height = round(self.height, 1)

    def age(self, days: int) -> None:
        self.age_in_days += days

    def grow_and_age(self, grow_cm: float, grow_days: int) -> None:
        inicial_height = self.height
        for day in range(1, grow_days + 1):
            print(f"=== Day {day} ===")
            self.show()
            self.grow(grow_cm)
            self.age(1)
        increased_height = round(self.height - inicial_height)
        print(f"Growth this week: {increased_height}cm")


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.00, 30)
    rose.grow_and_age(0.8, 7)


if __name__ == "__main__":
    main()
