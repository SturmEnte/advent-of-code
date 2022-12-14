file = open("input.txt", "r")
grid = []

for y, line in enumerate(file.read().split("\n")):
    for x, h in enumerate(line):
        if y == 0:
            grid.append([])
        grid[x].append(int(h))

width = len(grid)
height = len(grid[0])

# Part 1
visible_trees = 0
invisible_trees = 0

for x in range(width):
    if x == 0 or x == width - 1:
        visible_trees += height
        continue

    for y in range(height):
        if y == 0 or y == height - 1:
            visible_trees += 1
            continue

        tree = grid[x][y]
        visible_l = True
        visible_r = True
        visible_t = True
        visible_b = True

        for xi in range(x):                     # Trees left of the tree
            if grid[xi][y] >= tree:
                visible_l = False
        for xi in range(len(grid) - x - 1):     # Trees left of the tree
            if grid[x + xi + 1][y] >= tree:
                visible_r = False
        for yi in range(y):                     # Trees above the tree
            if grid[x][yi] >= tree:
                visible_t = False
        for yi in range(len(grid[0]) - y - 1):  # Trees below the tree
            if grid[x][y + yi + 1] >= tree:
                visible_b = False
        
        if visible_l == True or visible_r == True or visible_t == True or visible_b == True:
            visible_trees += 1
        else:
            invisible_trees += 1
    

print("Visible trees:", visible_trees)
print("Invisible trees:", invisible_trees)
print("Trees:", invisible_trees + visible_trees)

# Part 2
hss = 0

for x in range(width):
    for y in range(height):
        tree = grid[x][y]
        vdl = 0
        vdr = 0
        vdt = 0
        vdb = 0

        xi = x - 1
        while xi >= 0:                          # Trees left of the tree
            vdl += 1
            if grid[xi][y] >= tree:
                break
            xi -= 1
        for xi in range(len(grid) - x - 1):     # Trees left of the tree
            vdr += 1
            if grid[x + xi + 1][y] >= tree:
                break
        yi = y - 1
        while yi >= 0:                          # Trees above the tree
            vdt += 1
            if grid[x][yi] >= tree:
                break
            yi -= 1
        for yi in range(len(grid[0]) - y - 1):  # Trees below the tree
            vdb += 1
            if grid[x][y + yi + 1] >= tree:
                break
        
        scenic_score = vdl * vdr * vdt * vdb

        if hss < scenic_score:
            hss = scenic_score

print("Highest scenic score:", hss)