import math
from sys import argv

def calculate_distance(p1, p2):
    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                  + (p2[2] - p1[2])**2)
    return round(dist, 2)

def parsing_coordinates(coords) -> None:
    """ parsing coordinates and handling errors """
    try:
        conver_coords = coords.split(',')
        return tuple(int(coord.strip()) for coord in conver_coords)

    except ValueError as e:
        print(f"Error parsing coordinates {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def main() ->None:
    print("=== Game Coordinate System ===\n")
    av_len = len(argv)
    
    if (av_len == 1 or av_len > 2):
        print("Invalid Argument input !")
        return
    p1 = (0, 0, 0)
    p2 = (10, 20, 5)

    print(f"Postition created: {p2}")
    #calculate first distance
    dist1 = calculate_distance(p1, p2)
    print(f"Distance between {p1} and {p2}: {dist1}\n")

    #parsing valid coordinates
    
    valid_coords = "3,4,0"
    p3 = parsing_coordinates(valid_coords)
    print(f"Parsing coordinates: '{valid_coords}'")
    
    dist2 = calculate_distance(p1, p3)
    print(f"Distance between and {p1} and {p3}: {dist2}\n")

    #parsing invalid coordinates

    invalid_coords = "abc,def,ghi"
    print(f"Parsing invalid coordinates: '{invalid_coords}'")
    p4 = parsing_coordinates(invalid_coords)

    print("Unpacking demonstation:")
    print(f"Player at x={p3[0]}, y={p3[1]}, z={p3[2]}")
    print(f"Coordinates: X={p3[0]}, Y={p3[1]}, Z={p3[2]}")


if __name__ == "__main__":
    main()