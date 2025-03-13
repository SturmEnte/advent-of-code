from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

password = list(input[0])

def increment_password(i):
    if password[i] == "z":
        password[i] = "a"
        increment_password(i - 1)
        return
    
    password[i] = chr(ord(password[i]) + 1)

def is_password_valid(password):

    requirements = [False, True, 0]

    last_pair_end = -1

    for i, letter in enumerate(password):

        # Requirement 1
        if i < len(password) - 2 and ord(letter) + 2 == ord(password[i + 2]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
            requirements[0] = True

        # Requirement 2
        if letter in ["i", "o", "l"]:
            requirements[1] = False
            break

        # Requirement 3
        if i < len(password) - 1 and last_pair_end != i and letter == password[i + 1]:
            requirements[2] += 1
            last_pair_end = i + 1

    if requirements[0] and requirements[1] and requirements[2] >= 2:
        return True

    return False

while not is_password_valid(password):
    increment_password(len(password) - 1)

result = "".join(password)

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()