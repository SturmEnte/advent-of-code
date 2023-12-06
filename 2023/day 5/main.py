from colorama import Back, Style

file = open("example-input.txt", "r")
input = file.read().split("\n")

# Part 1
print("---Part 1---")
result = 0

ids = []
new_ids = []

processing = False

for i, line in enumerate(input):

    if line == "":
        processing = False
        for id in new_ids:
            ids.append(id)
        
        new_ids = []
        
        print(ids)
        continue
    
    if i == 0:
        for seed in line.split(":")[1].split(" "):
            if seed == "":
                continue
            ids.append(int(seed))
        print(f"{Back.BLUE}seeds{Style.RESET_ALL}")
        continue

    if processing == False and line.find("map:") >= 0:
        processing = True
        print(f"{Back.BLUE}{line.split(" ")[0]}{Style.RESET_ALL}")
        continue

    destination_start, source_start, length = line.split(" ")

    destination_start = int(destination_start)
    source_start = int(source_start)
    length = int(length)

    for i in range(0, length):
        destination = destination_start + i
        source = source_start + i

        for id in ids:
            if id == source:
                new_ids.append(destination)
                ids.remove(id)

result = min(ids)

print(f"Result: {result}")

# Part 2
print("---Part 2---")
result = 0

print(f"Result: {result}")
