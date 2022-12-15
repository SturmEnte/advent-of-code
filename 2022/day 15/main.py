file = open("example.txt", "r")
input = file.read()

MIN_X = -2
MIN_Y = 0
def translate(x, y):
    return (x - MIN_X, y - MIN_Y)

def print_map():
    for x in range(len(map)):
        line = ""
        for y in range(len(map[0])):
            if map[x][y] == 0:
                line += "."
            if map[x][y] == 1:
                line += "S"
            if map[x][y] == 2:
                line += "B"
            if map[x][y] == 3:
                line += "#"
        height = str(translate(0, y)[1])
        if len(height) < 2:
            height = "0" + height
        print(height ,"|", line, "|")

map = []

for x in range(50):
    map.append([])
    for _ in range(50):
        map[x].append(0)

for line in input.split("\n"):
    line = line.split()
    sx = int(line[2].split("=")[1].replace(",", ""))
    sy = int(line[3].split("=")[1].replace(":", ""))

    bx = int(line[8].split("=")[1].replace(",", ""))
    by = int(line[9].split("=")[1])
    #print(sx, sy, bx, by)

    s = translate(sx, sy)
    b = translate(bx, by)
    map[s[0]][s[1]] = 1
    map[b[0]][b[1]] = 2

    sx = s[0]
    sy = s[1]

    bx = b[0]
    by = b[1]

    difference = 0
    if sx > bx:
        difference += sx - bx
    else:
        difference += bx - sx

    if sy > by:
        difference += sy - by
    else:
        difference += by - sy
    
    print(translate(sx, sy), difference)

    x = 0 - difference
    y = 0 - difference

    while x < difference:
        t = translate(sx + x, sy)
        if map[t[0]][t[1]] == 0:
            map[t[0]][t[1]] = 3
        x += 1
    while y < difference:
        t = translate(sx, sy + y)
        if map[t[0]][t[1]] == 0:
            map[t[0]][t[1]] = 3
        y += 1

print_map()