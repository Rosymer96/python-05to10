#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        int_str = int(temp_str)
        if int_str >= 0 and int_str <= 40:
            print(f"Temperature is now {int_str}°C")
            return int_str
        elif int_str < 0:
            print(f"Caught input_temperature error: {int_str} is"
                  f" too cold for plants (min 0°C)")
        else:
            print(f"Caught input_temperature error: {int_str} is"
                  f" too hot for plants (max 40°C)")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    input_temperature('25')
    print()
    input_temperature('abc')
    print()
    input_temperature('100')
    print()
    input_temperature('-50')
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
