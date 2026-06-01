from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")
    res: dict[str, Callable[..., Any]] = {}
    res["store"] = store
    res["recall"] = recall
    return res


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_a call 1:", counter_b())

    print("\nTesting spell accumulator...")
    accumulator_a = spell_accumulator(100)
    accumulator_b = spell_accumulator(100)
    print("Base 100, add 20:", accumulator_a(20))
    print("Base 100, add 50:", accumulator_b(50))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    print(flaming("Sword"))
    frozen = enchantment_factory("Frozen")
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory["store"]("secret", 42)
    print("Recall 'secret':", memory["recall"]("secret"))
    print("Recall 'unknown':", memory["recall"]("unknown"))


if __name__ == "__main__":
    main()
