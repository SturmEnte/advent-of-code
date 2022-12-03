file = open("input.txt", "r")
inputs = file.read().split("\n")

score = 0

# Part 1
for input in inputs:
    op = input.split(" ")[0]
    me = input.split(" ")[1]

    if me == "X":       # Rock
        score += 1
        if op == "A":   # Rock
            score += 3
        elif op == "B": # Paper
            score += 0
        elif op == "C": # Scissors
            score += 6
    elif me == "Y": # Paper
        score += 2
        if op == "A":   # Rock
            score += 6
        elif op == "B": # Paper
            score += 3
        elif op == "C": # Scissors
            score += 0
    elif me == "Z": # Scissors
        score += 3
        if op == "A":   # Rock
            score += 0
        elif op == "B": # Paper
            score += 6
        elif op == "C": # Scissors
            score += 3

print("Total score (Strategy 1):", score)

score = 0

for input in inputs:
    op = input.split(" ")[0]
    me = input.split(" ")[1]

    if me == "X":   # Lose
        score += 0
        if op == "A":   # Rock
            score += 3
        elif op == "B": # Paper
            score += 1
        elif op == "C": # Scissors
            score += 2
    elif me == "Y": # Draw
        score += 3
        if op == "A":   # Rock
            score += 1
        elif op == "B": # Paper
            score += 2
        elif op == "C": # Scissors
            score += 3
    elif me == "Z": # Win
        score += 6
        if op == "A":   # Rock
            score += 2
        elif op == "B": # Paper
            score += 3
        elif op == "C": # Scissors
            score += 1

print("Total score (Strategy 2):", score)
