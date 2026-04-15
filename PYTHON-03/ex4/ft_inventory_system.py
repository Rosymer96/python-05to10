#!/usr/bin/env python3
import sys


def ft_inventory_system(args: list) -> None:
    items = {}
    for arg in args:
        try:
            key, value = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if key in items:
            print(f"Redundant item '{key}' - discarding")
        else:
            try:
                val = int(value)
                items[key] = val
            except ValueError as e:
                print(f"Quantity error for '{key}': {e}")
    total = sum(items.values())
    if total == 0:
        return
    else:
        print("=== Inventory System Analysis ===")
        print(f"Got inventory: {items}")
        item_list = list(items.keys())
        print(f"Item list: {item_list}")
        print(f"Total quantity of the {len(item_list)} items: "
              f"{total}")
        for key in items:
            value = items[key]
            percent = (value / total) * 100
            print(f"Item {key} represents {round(percent, 1)}%")
    max_item = None
    min_item = None
    for key in items:
        if max_item is None or items[key] > items[max_item]:
            max_item = key
        if min_item is None or items[key] < items[min_item]:
            min_item = key
    print(f"Item most abundant: {max_item} with quantity {items[max_item]}")
    print(f"Item least abundant: {min_item} with quantity {items[min_item]}")
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    ft_inventory_system(sys.argv[1:])
