from colorama import Back, Style
from hashlib import md5

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

i = 0

while True:
    
    md5_hash = md5(f"{input[0]}{i}".encode()).hexdigest()

    if md5_hash[:5] == "00000":
        result = i
        break

    i += 1

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

i = 0

while True:
    
    md5_hash = md5(f"{input[0]}{i}".encode()).hexdigest()

    if md5_hash[:6] == "000000":
        result = i
        break

    i += 1

print(f"Result: {result}")

file.close()