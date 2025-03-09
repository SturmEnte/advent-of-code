from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

x = 0
y = 0

houses = [(x, y)]

for direction in list(input[0]):
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1

    if (x, y) not in houses:
        houses.append((x, y))

result = len(houses)

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()