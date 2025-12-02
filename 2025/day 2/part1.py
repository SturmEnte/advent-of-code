from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split(",")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

for ids in input:
    limits = ids.split("-")
    
    lower = int(limits[0])
    upper = int(limits[1])

    for i in range(lower, upper + 1):
        i_str = str(i)
        length = len(i_str)

        # All ids not dividable by 2 must be valid
        if length % 2 != 0:
            print(i, "valid")
            continue
        
        # If the first half and second half of a string dividable by 2 are not the same
        # Then it does not have a repeating pattern
        if i_str[:length // 2] != i_str[length // 2:]:
            print(i, "valid")
            continue
        
        # If both of the checks above are false, then it is a string with a repeating pattern
        print(i, "invalid")

        result += i
        

print(f"Result: {Back.GREEN}{result}{Style.RESET_ALL}")

file.close()