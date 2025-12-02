from colorama import Back, Style
import math

file = open("input.txt", "r")
input = file.read().split(",")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

# This function only works if the string length is dividable by x
def slice_string_equal_parts(s: str, x: int) -> list[str]:
    """Slices a string 's' into 'x' equal parts."""
    
    part_length = len(s) // x
    
    return [
        s[k * part_length : (k + 1) * part_length]
        for k in range(x)
    ]

for ids in input:
    limits = ids.split("-")
    
    lower = int(limits[0])
    upper = int(limits[1])

    for i in range(lower, upper + 1):
        i_str = str(i)
        length = len(i_str)

        
        slicing_options = range(2, length + 1)
        new_slicing_options = []

        for option in slicing_options:
            if length % option == 0:
                new_slicing_options.append(option)

        slicing_options = new_slicing_options

        repeating_pattern = False

        for option in slicing_options:
            slices = slice_string_equal_parts(i_str, option)
            #print(slices)

            equal_parts = True

            for k in range(1, option):
                if slices[0] != slices[k]:
                    equal_parts = False
                    break
                
            if equal_parts:
                repeating_pattern = True
                break

        if repeating_pattern:
            print(i, "invalid")
            result += i
        else:
            print(i, "valid")
        

print(f"Result: {Back.GREEN}{result}{Style.RESET_ALL}")

file.close()