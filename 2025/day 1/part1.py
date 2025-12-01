#from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
#print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
print("---Part 1---")
result = 0

position = 50

for line in input:
    direction = line[0]
    moves = int(line[1:])

    if direction == "L":
        position -= moves
    else:
        position += moves

    while position > 99:
        position -= 100

    while position < 0:
        position += 100

    if position == 0:
        result += 1

    print(position)


print(f"Result: {result}")

# Part 2
#print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
print("---Part 2---")
result = 0



print(f"Result: {result}")

file.close()