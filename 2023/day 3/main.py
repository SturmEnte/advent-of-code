from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print("---Part 1---")
result = 0

list = []

for i, line in enumerate(input):
    
    if i == 0 or line == "":
        newLine = []
        for _ in range(0, len(line)):
            newLine.append(".")
        list.append(newLine)

    if line == "":
        break

    newLine = ["."]
    
    for symbol in line:
        newLine.append(symbol)

    newLine.append(".")

    list.append(newLine)

for y, ye in enumerate(list):
    for x, xe in enumerate(ye):
        
        if not xe.isdigit() or ye[x-1].isdigit():
            continue
        
        number_length = 0
        number_str = ""

        for char in ye[x:]:
            if char.isdigit():
                number_length += 1
                number_str += char
                continue
            break

        number = int(number_str)

        add = False

        if not ye[x - 1].isdigit() and ye[x - 1] != ".":
            add = True
        elif not ye[x + number_length].isdigit() and ye[x + number_length] != ".":
            add = True

        for entry in list[y - 1][x-1:x+number_length+1]:
            if not entry.isdigit() and entry != ".":
                add = True
                break
        
        for entry in list[y + 1][x-1:x+number_length+1]:
            if not entry.isdigit() and entry != ".":
                add = True
                break

        if add:
            result += number
            print(f"{Back.GREEN}Number: {number} | Length: {number_length}{Style.RESET_ALL}")
        else:
            print(f"{Back.RED}Number: {number} | Length: {number_length}{Style.RESET_ALL}")

print(list)            
print(f"Result: {result}")

print("---Part 2---")
result = 0

list = []

for i, line in enumerate(input):
    
    if i == 0 or line == "":
        newLine = []
        for _ in range(0, len(line)):
            newLine.append(".")
        list.append(newLine)

    if line == "":
        break

    newLine = ["."]
    
    for symbol in line:
        newLine.append(symbol)

    newLine.append(".")

    list.append(newLine)

for y, ye in enumerate(list):
    for x, xe in enumerate(ye):
        if xe != "*":
            continue
        
        numbers = []

        if list[y][x - 1].isdigit():
            n = 1
            
            while list[y][x - (n + 1)].isdigit():
                n += 1
            
            digits = list[y][x - 1]

        if len(numbers) != 2:
            continue

print(f"Result: {result}")
