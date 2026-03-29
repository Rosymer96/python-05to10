#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    int_str = int(temp_str)
    return int_str


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test = ['25', 'abc']
    for n in test:
        try:
            print(f"Input data is '{n}'")
            temp = input_temperature(n)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
