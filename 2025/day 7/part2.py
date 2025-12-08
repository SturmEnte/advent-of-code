# Not even working for example because its to inefficient

from copy import deepcopy

with open("example.txt", "r", encoding="utf-8") as f:
    input = [list(line.strip('\n')) for line in f]

result = 0

worlds = [deepcopy(input)]

y = 0
while y < len(input) - 1:
    
    for world in worlds:
        line = world[y]
        for x in range(len(line)):
            if line[x] == "|" or line[x] == "S":
                if input[y + 1][x] == "^":
                    # Create a new world for going left
                    new_world = deepcopy(world)
                    new_world[y + 1][x - 1] = "|"
                    worlds.append(new_world)
                    world[y + 1][x + 1] = "|"
                else:
                    world[y + 1][x] = "|"
    y += 1

print(f"Result: {len(worlds)}")
