#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    garden = [(Plant("Rose", 25, 30)), (Plant("Sunflower", 80, 45)),
              (Plant("Cactus", 15, 120))]
    print("=== Garden Plant Registry ===")
    for plant in garden:
        plant.show()


if __name__ == "__main__":
    main()
