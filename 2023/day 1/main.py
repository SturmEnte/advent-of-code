file = open("input.txt", "r")
inputs = file.read().split("\n")

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