from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

input_number = input[0]

last_number = input_number

for i in range(40):
    new_number = ""

    last_number_parts = list(last_number)

    count = 0
    last_processed = last_number_parts[0]

    for number in last_number_parts:

        if number == last_processed:
            count += 1
        else:
            new_number += str(count) + last_processed
            last_processed = number
            count = 1
    
    new_number += str(count) + last_processed
    last_number = new_number

result = len(last_number)

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

input_number = input[0]

last_number = input_number

for i in range(50):
    new_number = ""

    last_number_parts = list(last_number)

    count = 0
    last_processed = last_number_parts[0]

    for number in last_number_parts:

        if number == last_processed:
            count += 1
        else:
            new_number += str(count) + last_processed
            last_processed = number
            count = 1
    
    new_number += str(count) + last_processed
    last_number = new_number

result = len(last_number)

print(f"Result: {result}")

file.close()