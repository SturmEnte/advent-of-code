file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print("---Part 1---")
result = 0

list = []

for line in input:
    
    if line == "":
        break

    newLine = []
    
    for symbol in line:
        newLine.append(symbol)

    list.append(newLine)

print(list)

print(f"Result:{result}")