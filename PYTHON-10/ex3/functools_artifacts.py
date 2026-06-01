from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return max(spells)
    if operation == "min":
        return min(spells)

    raise ValueError("Invalid Operation")


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    fire_enchantment = partial(
        base_enchantment, 50, "fire"
    )
    ice_enchantment = partial(
        base_enchantment, 50, "ice"
    )
    lightning_enchantment = partial(
        base_enchantment, 50, "lightning"
    )

    return {
        "fire": fire_enchantment,
        "ice": ice_enchantment,
        "lightning": lightning_enchantment
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    """Base enchantment function to be specialized."""
    return f"Cast {element} spell with power {power} on {target}"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using memoization."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch_spell(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch_spell.register
    def _(arg: int) -> str:
        return f"{arg} damage"

    @dispatch_spell.register
    def _(arg: str) -> str:
        return f"{arg}"

    @dispatch_spell.register
    def _(arg: list) -> str:
        return f"{len(arg)} spells"
    return dispatch_spell


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))  # Output: 100
    print("Product:", spell_reducer(spells, "multiply"))  # Output: 240000
    print("Max:", spell_reducer(spells, "max"))  # Output: 40
    print("Min:", spell_reducer(spells, "min"))  # Output: 10

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"]("dragon"))
    print(enchantments["ice"]("goblin"))
    print(enchantments["lightning"]("wizard"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print("Damage spell:", dispatcher(42))
    print("Enchantment:", dispatcher("fireball"))
    print("Multi-cast:", dispatcher([1, "ice", 3]))
    print("Unknown type:", dispatcher({"Hola": 5}))


if __name__ == "__main__":
    main()
