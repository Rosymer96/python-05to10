
def ft_helper(actual, total):
    if (actual > total):
        return
    print(f"Day {actual}")
    ft_helper(actual + 1, total)


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    ft_helper(1, day)
    print("Harvest time!")
