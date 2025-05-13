from colorama import Back, Style
from re import findall

class Dynamic2DArray:
    min_row = 0
    max_row = 0
    min_col = 0
    max_col = 0

    def __init__(self, default_value=None):
        self.data = {}
        self.default_value = default_value

    def __getitem__(self, key):
        row, col = key
        return self.data.get((row, col), self.default_value)

    def __setitem__(self, key, value):
        row, col = key
        
        if row < self.min_row:
            self.min_row = row

        if row > self.max_row:
            self.max_row = row

        if col < self.min_col:
            self.min_col = col

        if col > self.max_col:
            self.max_col = col

        self.data[(row, col)] = value

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")

TARGET_LINE = 10

result = 0

map = Dynamic2DArray(default_value=".")
sensors = []

for line in input:
    # Extract the numbers
    raw_values = findall(r"x=(-?\d+), y=(-?\d+)",line)
    sensor_cords = (int(raw_values[0][0]), int(raw_values[0][1]))
    beacon_cords = (int(raw_values[1][0]), int(raw_values[1][1]))

    # Apply sensor and beacon position to the map
    map[sensor_cords[0], sensor_cords[1]] = "S"
    map[beacon_cords[0], beacon_cords[1]] = "B"


    # Determine distance between the sensor and beacon (x distance + y distance)
    distance = abs(sensor_cords[0] - beacon_cords[0]) + abs(sensor_cords[1] - beacon_cords[1])

    # Mark the clean area around the sensor
    for x in range(0, distance + 1):

        for y in range(0, distance + 1 - x):
            if map[sensor_cords[0] + x, sensor_cords[1] + y] == ".":
                map[sensor_cords[0] + x, sensor_cords[1] + y] = "#"

            if map[sensor_cords[0] - x, sensor_cords[1] - y] == ".":
                map[sensor_cords[0] - x, sensor_cords[1] - y] = "#"

            if map[sensor_cords[0] + x, sensor_cords[1] - y] == ".":
                map[sensor_cords[0] + x, sensor_cords[1] - y] = "#"

            if map[sensor_cords[0] - x, sensor_cords[1] + y] == ".":
                map[sensor_cords[0] - x, sensor_cords[1] + y] = "#"

print(map.min_col, map.min_row, map.max_col, map.max_row)

# Print the map
# for y in range(map.min_col, map.max_col + 1):
#     line = ""
#     for x in range(map.min_row, map.max_row + 1):
#         line += map[x, y]

#     print(line)

for x in range(map.min_row, map.max_row + 1):
    if map[x, TARGET_LINE] == "#":
        result += 1

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()