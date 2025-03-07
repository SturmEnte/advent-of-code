from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

left = []
right = []

for line in input:
    left.append(line.split("   ")[0])
    right.append(line.split("   ")[1])

left.sort()
right.sort()

for i in range(len(left)):
    if left[i] > right[i]:
        result += int(left[i]) - int(right[i])
    else:
        result += int(right[i]) - int(left[i])

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

left = []
right = []

for line in input:
    left.append(line.split("   ")[0])
    right.append(line.split("   ")[1])

for left_char in left:
    for right_char in right:
        if left_char == right_char:
            result += int(left_char)

print(f"Result: {result}")

file.close()