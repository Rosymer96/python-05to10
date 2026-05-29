from functools import reduce
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return max(spells)
    if operation == "min":
        return min(spells)
    raise ValueError("Invalid Operation")
