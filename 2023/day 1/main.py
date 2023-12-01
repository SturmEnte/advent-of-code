file = open("input.txt", "r")
inputs = file.read().split("\n")

print("---Part 1---")

result = 0

for line in inputs:
    if line == "":
        break

    parts = list(line)
    
    x = ""

    for part in parts:
        if part.isdigit():
            x += part
            break
    
    parts = reversed(parts)
    for part in parts:
        if part.isdigit():
            x += part
            break
    
    result += int(x)

print(f"Result: {result}")

print("---Part 2---")

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def filter(str):
    filtered = ""
    
    chars = list(str)
    i = 0

    for char in chars:
        
        if char.isdigit():
            filtered += char
        else:
            
            j = 1
            for number in numbers:
                if number == "".join(chars[i:i+len(number)]):
                    filtered += j.__str__()
                
                j += 1

        i += 1

    return filtered

    
result = 0

for oline in inputs:
    if oline == "":
        break

    line = filter(oline)

    parts = list(line)
    
    x = ""

    for part in parts:
        if part.isdigit():
            x += part
            break
    
    parts = reversed(parts)
    for part in parts:
        if part.isdigit():
            x += part
            break
    
    result += int(x)

print(f"Result: {result}")