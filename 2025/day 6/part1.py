file = open("input.txt", "r")
input = file.read().split("\n")

result = 0

parsed_input = []

# Reading the data
for i, line in enumerate(input):
    
    parts = (' '.join(line.split())).split(" ")
    print(parts)

    if parts[0].isdigit():
        parsed_input.append([int(number) for number in parts])
        continue
    parsed_input.append(parts)    

# Iterate through each column
for x in range(len(parsed_input[0])):
    # Get the operant (last row in parsed input)
    operant = parsed_input[len(parsed_input) - 1][x]
    
    # Calculate column
    column = parsed_input[0][x]
    for y in range(1, len(parsed_input) - 1):
        if operant == "+":
            column += parsed_input[y][x]
        else:
            column *= parsed_input[y][x]

    print(column)
    result += column

print(f"Result: {result}")

file.close()