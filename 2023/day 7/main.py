from colorama import Back, Style

file = open("example-input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

# Ratings:
# 7 - Five of a kind
# 6 - Four of a kind
# 5 - Full house
# 4 - Three of a kind
# 3 - Two pair
# 2 - One pair
# 1 - High card
# 0 - None

def high_card(cards):
    unique = []

    for card in cards:
        if card not in unique:
            unique.append(card)
    
    if len(cards) == len(unique):
        return True
    
    return False

def pairs(cards):
    card_dict = {}

    for card in cards:
        if card_dict.get(card):
            card_dict[card] = card_dict.get(card) + 1
        else:
            card_dict[card] = 1

    pairs = 0
    three_of_a_kind = False

    for entry in card_dict.items():
        if entry[1] == 2:
            pairs += 1
        
        if entry[1] == 3:
            three_of_a_kind = True

    return (pairs, three_of_a_kind)

hands = []

for line in input:
    if line == "":
        continue

    cards = list(line.split(" ")[0])  
    bid = int(line.split(" ")[1])

    print(cards)
    
    rating = 0

    if high_card(cards):
        rating = 1

    hand_pairs, three_of_a_kind = pairs(cards)

    if hand_pairs == 1:
        rating = 2
    
    if hand_pairs == 2:
        rating = 3

    if three_of_a_kind:
        rating = 4

    print(rating)

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()