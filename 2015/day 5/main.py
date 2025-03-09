from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

for string in input:
    string = list(string)
    
    vowels = 0
    twice_in_a_row = False
    contains_naughty = False

    for i, char in enumerate(string):

        if char in ["a", "e", "i", "o", "u"]:
            vowels += 1

        if i == len(string) - 1:
            break

        if char == string[i + 1]:
            twice_in_a_row = True

        if char + string[i + 1] in ["ab", "cd", "pq", "xy"]:
            contains_naughty = True

    if vowels >= 3 and twice_in_a_row and not contains_naughty:
        result += 1


print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

for string in input:
    string = list(string)
    
    pair_twice = False
    repeat_with_one_between = False

    for i, char in enumerate(string):

        if i == len(string) - 2:
            break

        if char == string[i + 2]:
            repeat_with_one_between = True

        char1 = char
        char2 = string[i + 1]

        new_string = string[i + 2:]

        for j, char in enumerate(new_string):
            if j < len(new_string) - 1 and char1 == char and char2 == new_string[j + 1]:
                pair_twice = True

    print(pair_twice, repeat_with_one_between)

    if pair_twice and repeat_with_one_between:
        result += 1

print(f"Result: {result}")

file.close()