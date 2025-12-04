from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

# Parse the file
# Replace @ with 1 . with 0
# Add frame of 0s around the field
grid = [[0] * (len(input[0]) + 2)]

for line in input:
    y = [0]
    for char in line:
        if char == "@":
            y.append(1)
            continue
        y.append(0)
    y.append(0)
    grid.append(y)

grid.append(grid[0])

# Replace 1 with 2 for valid rolls
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):

        # Skip empty fields
        if grid[y][x] == 0:
            continue

        # Check sourounding fields
        surounding_rolls = 0

        for xi in range(-1, 2):
            for yi in range(-1, 2):
                if xi == 0 and yi == 0:
                    continue
                
                if grid[y + yi][x + xi] > 0:
                    surounding_rolls += 1
        
        if surounding_rolls < 4:
            result += 1
            grid[y][x] = 2

# Pretty field
for y in grid:
    line = ""
    for x in y:
        if x == 1: line += "@"
        elif x == 2: line += "x"
        else: line += "."
    print(line)

print(f"Result: {result}")

file.close()