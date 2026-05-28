def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: x['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = sum(map(lambda x: x['power'], mages))/len(mages)
    res = {}
    res["max_power"] = max_power
    res["min_power"] = min_power
    res["avg_power"] = avg_power
    return res


def main() -> None:
    artifacts = [
        {'name': 'Lightning Rod', 'power': 108, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 82, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 61, 'type': 'focus'},
        {'name': 'Light Prism', 'power': 117, 'type': 'weapon'}]
    mages = [
        {'name': 'Luna', 'power': 56, 'element': 'light'},
        {'name': 'Alex', 'power': 57, 'element': 'shadow'},
        {'name': 'Riley', 'power': 98, 'element': 'water'},
        {'name': 'Storm', 'power': 54, 'element': 'fire'},
        {'name': 'Storm', 'power': 56, 'element': 'ice'}]
    spells = ['lightning', 'earthquake', 'meteor', 'fireball']

    print("\nTesting artifact sorter...")
    sorted = artifact_sorter(artifacts)
    for i, x in enumerate(sorted):
        if i < len(sorted) - 1:
            print(f"{x['name']} ({x['power']} power)", end=" ")
            print(f"comes before {sorted[i + 1]['name']} "
                  f"({sorted[i + 1]['power']} power)")

    print("\nTesting power filter...")
    powers_filtered = power_filter(mages, 55)
    for power in powers_filtered:
        print(f"{power['name']} ({power['power']} power)")

    print("\nTesting spell transformer...")
    spell_transformed = spell_transformer(spells)
    print(" ".join([x for x in spell_transformed]))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
