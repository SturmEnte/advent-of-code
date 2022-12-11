from copy import deepcopy

file = open("input.txt", "r")
input = file.read()

def calc_worry_level(old, operation):
    one = 0
    two = 0
    operator = ""
    for i, part in enumerate(operation.split(" ")):
        if i == 0:
            if part == "old":
                one = old
            else:
                one = int(part)
        elif i == 1:
            operator = part
        elif i == 2:
            if part == "old":
                two = old
            else:
                two = int(part)

    if operator == "*":
        return one * two
    elif operator == "+":
        return one + two
    else:
        print(one, operator, two)

# Parse input
monkeys = [{
            "items": [],
            "operation": "",
            "divisible_by": 0,
            "true": 0,
            "false": 0
        }]

monkey = 0
for line in input.split("\n"):
    if line == "":
        monkey += 1
        monkeys.append({
            "items": [],
            "operation": "",
            "divisible_by": 0,
            "true": 0,
            "false": 0
        })
        continue
    
    parts = line.split()

    if parts[0] == "Starting":
        parts.pop(0)
        parts.pop(0)
        for item in parts:
            monkeys[monkey]["items"].append(int(item.replace(",", "")))
    elif parts[0] == "Operation:":
        parts.pop(0)
        parts.pop(0)
        parts.pop(0)
        monkeys[monkey]["operation"] = " ".join(parts)
    elif parts[0] == "Test:":
        monkeys[monkey]["divisible_by"] = int(parts[3])
    elif parts[1] == "true:":
        monkeys[monkey]["true"] = int(parts[5])
    elif parts[1] == "false:":
        monkeys[monkey]["false"] = int(parts[5])

monkeys_copy = deepcopy(monkeys)

# Part 1
rounds = 20
inspects = []

for _ in range(len(monkeys)):
    inspects.append(0)

for round in range(rounds):
    for i, monkey in enumerate(monkeys):
        for item in monkey["items"]:
            inspects[i] += 1
            worry_level = item
            worry_level = int(calc_worry_level(item, monkey["operation"]) / 3)
        
            if worry_level % monkey["divisible_by"] > 0:
                monkeys[monkey["false"]]["items"].append(worry_level)
            else:
                monkeys[monkey["true"]]["items"].append(worry_level)

        monkey["items"] = []

inspects = sorted(inspects)

print("Monkey business (Part 1):", inspects[len(inspects) - 1] * inspects[len(inspects) - 2])

# Part 2
monkeys = monkeys_copy

rounds = 10000
inspects = []

divider = 1
for monkey in monkeys:
    divider = divider * monkey["divisible_by"]

for _ in range(len(monkeys)):
    inspects.append(0)

for round in range(rounds):
    for i, monkey in enumerate(monkeys):
        for item in monkey["items"]:
            inspects[i] += 1
            worry_level = item
            worry_level = calc_worry_level(item, monkey["operation"]) % divider
        
            if worry_level % monkey["divisible_by"] > 0:
                monkeys[monkey["false"]]["items"].append(worry_level)
            else:
                monkeys[monkey["true"]]["items"].append(worry_level)

        monkey["items"] = []

inspects = sorted(inspects)

print("Monkey business (Part 2):", inspects[len(inspects) - 1] * inspects[len(inspects) - 2])