from colorama import Back

file = open("input.txt", "r")
input = file.read()

sand_source = (500,0)
tiles = []

width = 600
heigth = 300

for x in range(width):
    tiles.append([])
    for y in range(heigth):
        tiles[x].append(0)

tiles[sand_source[0]][sand_source[1]] = 3

lowest_y = 0

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

def print_tiles():
    w = 200
    ws = 400
    h = lowest_y + 1 
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

print("Lowest y:", lowest_y)

# print_tiles()

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

print_tiles()

print("Sand particles:", sand_particles)