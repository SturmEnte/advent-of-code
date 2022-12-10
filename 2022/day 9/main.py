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

print("---Part 1---")
print("Head end position:", hx, hy)
print("Tail end position:", tx, ty)
print("The tail visited", different_positions, "different positions")

# Part 2
knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
last_knot_positions = [(0, 0)]

def touches_knot(knot, m_knot):
    x = -1
    y = -1
    for _ in range(9):
        if knot[0] + x == m_knot[0] and knot[1] + y == m_knot[1]:
            return True
        x += 1
        if x == 2:
            x = -1
            y += 1
    return False

def update_knots():
    global knots
    
    for i in range(1, 10):
        knot = knots[i]
        m_knot = knots[i - 1]

        # Check if knot touches knot that comes before it
        if touches_knot(knot, m_knot) == True:
            continue

        # Move the knot
        if knot[1] == m_knot[1]:
            if knot[0] + 2 == m_knot[0]:
                knot[0] += 1
            elif knot[0] - 2 == m_knot[0]:
                knot[0] -= 1
            else:
                print("Imposible", knot, m_knot)
        elif knot[0] == m_knot[0]:
            if knot[1] + 2 == m_knot[1]:
                knot[1] += 1
            elif knot[1] - 2 == m_knot[1]:
                knot[1] -= 1
            else:
                print("Imposible", knot, m_knot)
        else:
            if touches_knot([knot[0] + 1, knot[1] + 1], m_knot):
                knot[0] += 1
                knot[1] += 1
            elif touches_knot([knot[0] + 1, knot[1] - 1], m_knot):
                knot[0] += 1
                knot[1] -= 1
            elif touches_knot([knot[0] - 1, knot[1] + 1], m_knot):
                knot[0] -= 1
                knot[1] += 1
            else:
                knot[0] -= 1
                knot[1] -= 1

        if i == 9:
            last_knot_positions.append((knot[0], knot[1]))
        knots[i] = knot


for move in input.split("\n"):
    direction = move.split()[0]
    amount = int(move.split()[1])

    for _ in range(amount):
        if direction == "U":
            knots[0][1] += 1
            update_knots()
        elif direction == "D":
            knots[0][1] -= 1
            update_knots()
        elif direction == "L":
            knots[0][0] -= 1
            update_knots()
        elif direction == "R":
            knots[0][0] += 1
            update_knots()
        else:
            print("Unknown move:", move)

different_positions = 0
counted = []
for pos in last_knot_positions:
    if pos not in counted:
        counted.append(pos)
        different_positions += 1

print("---Part 2---")
print("The last knot was at", different_positions, "positions")