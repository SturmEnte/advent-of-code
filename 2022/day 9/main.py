file = open("input.txt")

hx = 0
hy = 0

tx = 0
ty = 0

head_visits = [(0, 0)]

def touching_head(cx, cy):
    x = -1
    y = -1

    for i in range(9):
        if cx + x == hx and cy + y == hy:
            return True

        x += 1
        if x == 2:
            x = -1
            y += 1
    return False

z = 0 # Debugging var

def update_tail():
    touching = touching_head(tx, ty)

    if touching == True:
        print(z, "n touching")
        return (0, 0)

    nx = 0
    ny = 0

    if ty == hy:
        if tx + 2 == hx:
            nx = 1
        elif tx - 2 == hx:
            nx = -1
        else:
            print("Imposible", hx, hy, tx, ty)
    elif tx == hx:
        if ty + 2 == hy:
            ny = 1
        elif ty - 2 == hy:
            ny = -1
        else:
            print("Imposible", hx, hy, tx, ty)
    else:
        if touching_head(tx + 1, ty + 1):
            nx = 1
            ny = 1
        elif touching_head(tx + 1, ty - 1):
            nx = 1
            ny = -1
        elif touching_head(tx - 1, ty + 1):
            nx = -1
            ny = 1
        else:
            nx = -1
            ny = -1

    head_visits.append((nx + tx, ny + ty))
    print(z, "n", tx + nx, ty + ny, hx, hy)
    return (nx, ny)

for j, move in enumerate(file.read().split("\n")):
    z = j * 10
    direction = move.split()[0]
    amount = int(move.split()[1])
    print(direction, amount)

    for i in range(amount):
        z += 1
        if direction == "U":
            hy += 1
            pos = update_tail()
            tx += pos[0]
            ty += pos[1]
        elif direction == "D":
            hy -= 1
            pos = update_tail()
            tx += pos[0]
            ty += pos[1]
        elif direction == "L":
            hx -= 1
            pos = update_tail()
            tx += pos[0]
            ty += pos[1]
        elif direction == "R":
            hx += 1
            pos = update_tail()
            tx += pos[0]
            ty += pos[1]
        else:
            print("Unknown move:", move)

print("")
print(head_visits)
print("")

different_positions = 0
counted = []
for pos in head_visits:
    if pos not in counted:
        counted.append(pos)
        different_positions += 1

print("Head:", hx, hy)
print("Tail:", tx, ty)
print("The head visited", different_positions, "different positions")