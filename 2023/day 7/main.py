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


print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()