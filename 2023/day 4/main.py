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

    print(numbers)

print(f"Result: {result}")