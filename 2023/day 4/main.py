file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print("---Part 1---")
result = 0

for card in input:
    if card == "":
        continue
    
    raw_winning_numbers, raw_numbers = card.split(":")[1].split("|")
    
    winning_numbers = []

    for winning_number in raw_winning_numbers.split(" "):
        if winning_number == "":
            continue
        winning_numbers.append(int(winning_number))

    numbers = []

    for number in raw_numbers.split(" "):
        if number == "":
            continue
        numbers.append(int(number))

    value = 0

    for number in numbers:
        if number in winning_numbers:
            if value == 0:
                value = 1
            else:
                value *= 2

    result += value

print(f"Result: {result}")

# Part 2
print("---Part 2---")
result = 0

cards = []

for card in input:
    if card == "":
        continue
    
    raw_winning_numbers, raw_numbers = card.split(":")[1].split("|")
    
    winning_numbers = []

    for winning_number in raw_winning_numbers.split(" "):
        if winning_number == "":
            continue
        winning_numbers.append(int(winning_number))

    numbers = []

    for number in raw_numbers.split(" "):
        if number == "":
            continue
        numbers.append(int(number))

    cards.append((winning_numbers, numbers))

def process_card(id):
    card = cards[id]
    winning_numbers = card[0]
    numbers = card[1]

    i = 1

    n = 1

    for number in numbers:
        if number in winning_numbers:
            n += process_card(id + i)
            i += 1

    return n

for i, card in enumerate(cards):
    result += process_card(i)

print(f"Result: {result}")