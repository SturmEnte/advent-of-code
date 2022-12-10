file = open("input.txt", "r")
input = file.read()

# Part 1
print("---Part 1---")

x_register = 1
cycles = 0
signal_strengths = []

checks = [20, 60, 100, 140, 180, 220]

for line in input.split("\n"):
    cmd = line.split()[0]

    if cmd == "noop":
        cycles += 1
    else:
        cycles += 2

    if cycles >= checks[0]:
        signal_strengths.append((x_register) * checks[0])
        checks.pop(0)

    if cmd == "addx":
        x_register += int(line.split()[1])

    if len(checks) == 0:
        break

signal_strength_sum = 0
for strength in signal_strengths:
    signal_strength_sum += strength

print("Signal strength sum:", signal_strength_sum)

# Part 2
print("")
print("---Part 2---")

width = 40
height = 6

x = 0
y = 0

x_register = 1

screen = []

for _ in range(height):
    screen.append([])

def cycle(n):
    global x, y, screen, x_register

    # Start of cycle


    # During cycle
    if x == x_register - 1 or x == x_register or x == x_register + 1:
        screen[y].append("#")
    else:
        screen[y].append(".")

    print(x_register)

    # End of cycle
    x_register += n

    x += 1
    if x == width:
        y += 1
        x = 0
        if y == height:
            return True
    return False

c = 1

for line in input.split("\n"):
    cmd = line.split()[0]

    if cmd == "noop":
        if cycle(0):
            break
        c += 1
        
    else:
        if cycle(0):
            break
        c += 1
        if cycle(int(line.split()[1])):
            break
        c += 1

print(x, y, c)

print("---Image---")
for row in screen:
    s = ""
    for pixel in row:
        s += pixel
    print(s)