from colorama import Back
from copy import deepcopy

file = open("input.txt", "r")
input = file.read()

sand_source = (500,0)
tiles = []

width = 800
heigth = 300

for x in range(width):
    tiles.append([])
    for y in range(heigth):
        tiles[x].append(0)

tiles[sand_source[0]][sand_source[1]] = 3

lowest_y = 0

copy = deepcopy(tiles)

def print_tiles(w, ws, h):
    for y in range(h):
        line = ""
        for x in range(w):
            if tiles[x + ws][y] == 0:
                line += Back.RESET + " "
            elif tiles[x + ws][y] == 1:
                line += Back.LIGHTBLACK_EX + " "
            elif tiles[x + ws][y] == 2:
                line += Back.YELLOW + " "
            elif tiles[x + ws][y] == 3:
                line += Back.BLUE + " "
        s = str(y)
        if y < 10:
            s = " " + s    
        if y < 100:
            s = " " + s         
        print(s,"|",line,"|")

# Part 1
print("---Part 1---")
for line in input.split("\n"):
    points = line.split(" -> ")
    
    for i in range(len(points) - 1):
        from_p = points[i].split(",")
        to_p = points[i + 1].split(",")

        fx = int(from_p[0])
        fy = int(from_p[1])

        tx = int(to_p[0])
        ty = int(to_p[1])

        if fx == tx:
            if fy < ty:
                for i in range(ty - fy + 1):
                    tiles[fx][fy + i] = 1
            elif fy > ty:
                for i in range(fy - ty + 1):
                    tiles[fx][fy - i] = 1
        elif fy == ty:
            if fx < tx:
                for i in range(tx - fx + 1):
                    tiles[fx + i][fy] = 1
            elif fx > tx:
                for i in range(fx - tx + 1):
                    tiles[fx - i][fy] = 1
        else:   
            print("No no zone:", from_p, to_p)

        if fy > lowest_y:
            lowest_y = fy
        if ty > lowest_y:
            lowest_y = ty

print("Lowest y:", lowest_y)

sand_particles = 0

done = False
while not done:
    sx = sand_source[0]
    sy = sand_source[1]
    while True:
        if sy > lowest_y:
            done = True
            break
        elif tiles[sx][sy + 1] == 0:
            sy += 1
            continue
        elif tiles[sx - 1][sy + 1] == 0:
            sx -= 1
            sy += 1
            continue
        elif tiles[sx + 1][sy + 1] == 0:
            sx += 1
            sy += 1
            continue

        sand_particles += 1
        tiles[sx][sy] = 2
        break

print_tiles(200, 400, lowest_y + 1)

print("Sand particles:", sand_particles)

# Part 2
print("---Part 2---")

tiles = copy

for i in range(len(tiles)):
    tiles[i][lowest_y + 2] = 1

for line in input.split("\n"):
    points = line.split(" -> ")
    
    for i in range(len(points) - 1):
        from_p = points[i].split(",")
        to_p = points[i + 1].split(",")

        fx = int(from_p[0])
        fy = int(from_p[1])

        tx = int(to_p[0])
        ty = int(to_p[1])

        if fx == tx:
            if fy < ty:
                for i in range(ty - fy + 1):
                    tiles[fx][fy + i] = 1
            elif fy > ty:
                for i in range(fy - ty + 1):
                    tiles[fx][fy - i] = 1
        elif fy == ty:
            if fx < tx:
                for i in range(tx - fx + 1):
                    tiles[fx + i][fy] = 1
            elif fx > tx:
                for i in range(fx - tx + 1):
                    tiles[fx - i][fy] = 1
        else:   
            print("No no zone:", from_p, to_p)

        if fy > lowest_y:
            lowest_y = fy
        if ty > lowest_y:
            lowest_y = ty

print("Lowest y:", lowest_y)

sand_particles = 0

done = False
while not done:
    sx = sand_source[0]
    sy = sand_source[1]
    i = 0
    while True:
        if tiles[sx][sy + 1] == 0:
            sy += 1
            i+=1
            continue
        elif tiles[sx - 1][sy + 1] == 0:
            sx -= 1
            sy += 1
            i+=1
            continue
        elif tiles[sx + 1][sy + 1] == 0:
            sx += 1
            sy += 1
            i+=1
            continue
        elif (sx, sy) == sand_source and i == 0:
            done = True

        sand_particles += 1
        tiles[sx][sy] = 2
        break

print_tiles(width, 0, lowest_y + 3)

print("Sand particles:", sand_particles)