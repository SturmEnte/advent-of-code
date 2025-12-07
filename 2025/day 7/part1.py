with open("input.txt", "r", encoding="utf-8") as f:
    input = [list(line.strip('\n')) for line in f]

result = 0

y = 0
while y < len(input) - 1:
    line = input[y]
    for x in range(len(line)):
        if line[x] == "|" or line[x] == "S":
            if input[y + 1][x] == "^":
                input[y + 1][x - 1] = "|"
                input[y + 1][x + 1] = "|"
                result += 1
            else:
                input[y + 1][x] = "|"
    y += 1

    # Print field
    for line in input:
        string = ""
        for char in line:
            string += char
        print(string)
    print()

print(f"Result: {result}")
