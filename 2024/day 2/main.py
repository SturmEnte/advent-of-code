from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

for report in input:
    levels = report.split(" ")

    # Convert to integers
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    safe = True

    decreasing = False

    if levels[0] > levels[1]:
        decreasing = True

    for i in range(len(levels) - 1):
        # Check for decreasing difference safety
        if levels[i] > levels[i + 1] and levels[i] - levels[i + 1] > 3:
            safe = False
            break

        # Check for increasing difference safety
        if levels[i] < levels[i + 1] and levels[i + 1] - levels[i] > 3:
            safe = False
            break

        # Check if only decreasing or increasing
        if levels[i] > levels[i + 1] and not decreasing:
            safe = False
            break

        if levels[i] < levels[i + 1] and decreasing:
            safe = False    
            break

        if levels[i] == levels[i + 1]:
            safe = False
            break

    if safe:
        result += 1
        print(f"{report} is safe")

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

print(f"Result: {result}")

file.close()