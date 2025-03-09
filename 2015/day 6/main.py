from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

lights = []

for i in range(1000):
    lights.append([False] * 1000)

for line in input:
    line = line.replace("through", "")
    line = line.replace("  ", " ")

    if line.startswith("turn on"):
        line = line.replace("turn on ", "")
        split = line.split(" ")
        x_start = int(split[0].split(",")[0])
        y_start = int(split[0].split(",")[1])
        x_end = int(split[1].split(",")[0])
        y_end = int(split[1].split(",")[1])

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                lights[x][y] = True

    elif line.startswith("turn off"):
        line = line.replace("turn off ", "")
        split = line.split(" ")
        x_start = int(split[0].split(",")[0])
        y_start = int(split[0].split(",")[1])
        x_end = int(split[1].split(",")[0])
        y_end = int(split[1].split(",")[1])

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                lights[x][y] = False

    elif line.startswith("toggle"):
        line = line.replace("toggle ", "")
        split = line.split(" ")
        x_start = int(split[0].split(",")[0])
        y_start = int(split[0].split(",")[1])
        x_end = int(split[1].split(",")[0])
        y_end = int(split[1].split(",")[1])

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                lights[x][y] = not lights[x][y]

for x_line in lights:
    for light in x_line:
        if light:
            result += 1

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()