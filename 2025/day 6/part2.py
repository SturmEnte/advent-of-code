file = open("input.txt", "r")
input = file.read().split("\n")

result = 0

# Find longes row
max_row = 0
for row in input:
    if len(row) > max_row: max_row = len(row)

# Get problem start and end position and opps
opperations = [input[len(input) - 1][0]]
widths = []

start = 0
x = 1
for char in input[len(input) - 1][1:len(input[0]) - 1]:
    if char != " ":
        opperations.append(char)
        widths.append((start, x - 2))
        start = x

    x += 1

# Add last width
widths.append((start, max_row - 1))

print(opperations)
print(widths)

# Iterate through each problem
for n, width in enumerate(widths):
    numbers = []
    
    for x in range(width[0], width[1] + 1):
        number = ""
        for y in range(len(input) - 1):
            if input[y][x] != " ":
                number += input[y][x]

        numbers.append(int(number))
    
    if opperations[n] == "+":
        current_result = sum(numbers)
        print(current_result)
        result += current_result
    else:
        current_result = numbers[0]
        for number in numbers[1:]:
            current_result *= number
        print(current_result)
        result += current_result

print(f"Result: {result}")

file.close()