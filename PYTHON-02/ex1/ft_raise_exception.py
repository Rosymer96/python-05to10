#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    int_str = int(temp_str)
    if int_str < 0 or int_str > 40:
        if int_str < 0:
            raise ValueError(f"{int_str} is too cold for plants "
                             f"(min 0°C)")
        else:
            raise ValueError(f"{int_str} is too hot for plants "
                             f"(max 40°C)")
    return int_str


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    test = ['25', 'abc', '100', '-50']
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
