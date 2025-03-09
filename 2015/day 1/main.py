from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

for char in list(input[0]):
    if char == "(":
        result += 1
    elif char == ")":
        result -= 1
    else:
        print("Error", char)

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0
floor = 0

for i, char in enumerate(list(input[0])):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        print("Error", char)

    if floor == -1:
        result = i + 1
        break

print(f"Result: {result}")

file.close()