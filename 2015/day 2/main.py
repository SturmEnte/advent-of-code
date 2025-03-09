from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

for present_dimensions in input:
    dimensions = present_dimensions.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])

    side1 = l*w
    side2 = l*h
    side3 = w*h

    result += 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

for present_dimensions in input:
    dimensions = present_dimensions.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])

    result += l*w*h

    sides = [l, w, h]
    sides.remove(max(sides))
    result += 2*sides[0] + 2*sides[1]

print(f"Result: {result}")

file.close()