import math


def get_player_pos():
    while True:
        try:
            line = input("Enter new coordinates as floats in format 'x,y,z': ")
            parts = line.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue
            # Intentamos convertir a float. Si falla, saltará al ValueError
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            for p in parts:
                try:
                    float(p)
                except ValueError:
                    print(f"Error on parameter '{p}': {e}")
                    break
            continue


def calculate_distance(p1: tuple[float, float, float],
                       p2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main():
    print("=== Game Coordinate System ===")
    # Primera captura
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    # Distancia al centro (0,0,0)
    dist_to_center = calculate_distance(pos1, (0.0, 0.0, 0.0))
    print(f"Distance to center: {round(dist_to_center, 4)}")
    # Segunda captura
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    # Distancia entre ambos puntos
    dist_between = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
