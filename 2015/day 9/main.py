from colorama import Back, Style
from itertools import permutations
from sys import maxsize

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

n = 10

indexCityTable = []
weightTable = [[None for i in range(n)] for j in range(n)]

for line in input:
    line = line.replace(" to ", " ")
    line = line.replace(" = ", " ")
    
    print(line)
    
    parts = line.split(" ")

    if parts[0] not in indexCityTable:
        indexCityTable.append(parts[0])

    if parts[1] not in indexCityTable:
        indexCityTable.append(parts[1])
    
    index1 = indexCityTable.index(parts[0])
    index2 = indexCityTable.index(parts[1])

    weightTable[index1][index2] = int(parts[2])
    weightTable[index2][index1] = int(parts[2])

def distance(path):
    distance = 0
    for i, city in enumerate(path):
        if i == len(path) - 1:
            break
        distance += weightTable[city][path[i + 1]]
    return distance

possible_paths = list(permutations(range(len(indexCityTable))))

shortest_distance = maxsize
shortest_path = None

for path in possible_paths:
    dist =  distance(path)
    if shortest_distance > dist:
        shortest_distance = dist
        shortest_path = path

path_string = ""

for city in shortest_path:
    if path_string != "":
        path_string += " -> "
    
    path_string += indexCityTable[city]

print(path_string)

result = shortest_distance

print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0

longest_distance = 0
longest_path = None

for path in possible_paths:
    dist =  distance(path)
    if longest_distance < dist:
        longest_distance = dist
        longest_path = path

path_string = ""

for city in longest_path:
    if path_string != "":
        path_string += " -> "
    
    path_string += indexCityTable[city]

print(path_string)

result = longest_distance

print(f"Result: {result}")

file.close()