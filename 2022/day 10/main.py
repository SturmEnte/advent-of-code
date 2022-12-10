file = open("input.txt", "r")

x_register = 1
cycles = 0
signal_strengths = []

checks = [20, 60, 100, 140, 180, 220]

for line in file.read().split("\n"):
    cmd = line.split()[0]

    if cmd == "noop":
        cycles += 1
    else:
        cycles += 2

    if cycles >= checks[0]:
        print(checks[0],x_register)
        signal_strengths.append((x_register) * checks[0])
        checks.pop(0)

    if cmd == "addx":
        x_register += int(line.split()[1])

    if len(checks) == 0:
        break

signal_strength_sum = 0
for strength in signal_strengths:
    signal_strength_sum += strength

print("---Part 1---")
print("Signal strength sum:", signal_strength_sum)