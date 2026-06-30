#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str | None = None) -> None:
        if message is None:
            message = "A garden error occurred"
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        if message is None:
            message = "Unknown plant error"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str | None = None) -> None:
        if message is None:
            message = "Unknown water error"
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
