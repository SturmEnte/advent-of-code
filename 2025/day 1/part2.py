#from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
#print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
print("---Part 2---")
result = 0

position = 50

for line in input:
    direction = line[0]
    moves = int(line[1:])

    if direction == "L":
        direction = -1
    else:
        direction = 1

    for i in range(moves):

        position += direction

        if position > 99:
            position = 0
        elif position < 0:
            position = 99

        if position == 0:
            result += 1

    print(position)


print(f"Result: {result}")

file.close()