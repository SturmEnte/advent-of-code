file = open("input.txt")
input = file.read()

# Part 1
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

def update_tail():
    touching = touching_head(tx, ty)

    if touching == True:
        return (0, 0)

    nx = 0
    ny = 0

    if ty == hy:
        if tx + 2 == hx:
            nx = 1
        elif tx - 2 == hx:
            nx = -1
    elif tx == hx:
        if ty + 2 == hy:
            ny = 1
        elif ty - 2 == hy:
            ny = -1
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
    return (nx, ny)

for move in input.split("\n"):
    direction = move.split()[0]
    amount = int(move.split()[1])

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

different_positions = 0
counted = []
for pos in head_visits:
    if pos not in counted:
        counted.append(pos)
        different_positions += 1

print("Head end position:", hx, hy)
print("Tail end position:", tx, ty)
print("The head visited", different_positions, "different positions")

# Part 2