#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    print(f"Input data is '{temp_str}")
    try:
        int_str = int(temp_str)
        print(f"Temperature is now {int_str}°C")
        return int_str
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    input_temperature('25')
    print()
    input_temperature('abc')
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
