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

        print(f"Number: {number} | Length: {number_length}")

        add = False

        if x-1 >= 0 and not ye[x - 1].isdigit() and ye[x - 1] != ".":
            add = True
        elif x+1 <= len(ye) and not ye[x + number_length].isdigit() and ye[x + number_length] != ".":
            add = True

        for entry in list[y - 1][x-1:x+number_length]:
            if not entry.isdigit() and entry != ".":
                add = True
                break
        
        for entry in list[y + 1][x-1:x+number_length]:
            if not entry.isdigit() and entry != ".":
                add = True
                break

        result += number
            

print(f"Result: {result}")