file = open("example.txt", "r")
grid = []

for y, line in enumerate(file.read().split("\n")):
    for x, h in enumerate(line):
        if y == 0:
            grid.append([])
        grid[x].append(int(h))

# Part 1
visible_trees = 0
invisible_trees = 0

for x in range(len(grid)):
    if x == 0 or x == len(grid) - 1:
        visible_trees += len(grid[x]) 
        continue
    for y in range(len(grid[0])):
        if y == 0 or y == len(grid[0]) - 1:
            visible_trees += 1
            continue
        tree = grid[x][y]
        visible_l = True
        visible_r = True
        visible_t = True
        visible_b = True

        print(tree)
        print(x, y)

        for xi in range(x): # Trees left of the tree
            if grid[xi][y] > tree:
                visible_l = False
        for xi in range(len(grid) - x - 1): # Trees left of the tree
            if grid[x + xi + 1][y] > tree:
                visible_r = False
        for yi in range(y):
                if grid[x][yi] > tree:
                    visible_t = False
        for yi in range(len(grid[0]) - y - 1):
            if grid[x][y + yi + 1] > tree:
                visible_t = False
        
    if visible_l == True or visible_r == True or visible_t == True or visible_b == True:
        visible_trees += 0
    else:
        invisible_trees += 0

print("Visible trees:", visible_trees)
print("Invisible trees:", invisible_trees)
print("Trees:", invisible_trees + visible_trees)