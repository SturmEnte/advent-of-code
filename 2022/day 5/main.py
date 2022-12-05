import copy

def split_string(string, split_string):
    return [string[i:i+split_string] for i in range(0, len(string), split_string)]

file = open("input.txt", "r")

lines = file.read().split("\n")

crates = []

crate_lines = []
moves = []

x = False
for line in lines:
    if line == "":
        x = True
        continue
    if not x:
        crate_lines.append(line + " ")
    else:
        moves.append(line)

stacks = len(crate_lines[len(crate_lines) - 1].split())

for i in range(stacks):
    crates.append([])

for i, line in enumerate(crate_lines):
    if i == len(crate_lines) - 1:
        break

    for j, crate_string in enumerate(split_string(line, 4)):
        char = ord([char for char in crate_string][1])
        if char >= 65 and char <= 90:
            crates[j].append([char for char in crate_string][1])

print("Stacks:", stacks)
print("Crates:", crates)

cm9000_crates = copy.deepcopy(crates)

for move in moves:
    amount = int(move.split(" ")[1])
    from_stack = int(move.split(" ")[3]) - 1
    to_stack = int(move.split(" ")[5]) - 1
    for i in range(amount):
        cm9000_crates[to_stack].insert(0, cm9000_crates[from_stack].pop(0))

solution = ""
for crate in cm9000_crates:
    solution += crate[0]

print("Solution for the CrateMover 9000:", solution)

cm9001_crates = copy.deepcopy(crates)

for move in moves:
    amount = int(move.split(" ")[1])
    from_stack = int(move.split(" ")[3]) - 1
    to_stack = int(move.split(" ")[5]) - 1
    for i in range(amount):
        cm9001_crates[to_stack].insert(i, cm9001_crates[from_stack].pop(0))

solution = ""
for crate in cm9001_crates:
    solution += crate[0]

print("Solution for the CrateMover 9001:", solution)