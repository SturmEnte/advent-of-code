h_pos = 0
depth = 0

file = open("input.txt")
split = file.read().split("\n")

# Part 1
for input in split:
    input = input.split(" ")
    
    if input[0] == "forward":
        h_pos += int(input[1])
    elif input[0] == "up":
        depth -= int(input[1])
    elif input[0] == "down":
        depth += int(input[1])
    else:
        print("Unknown input:", input[0], input[1])

print("Part 1:")
print("Horizontal position:", h_pos, "\nDepth:", depth)
print("Solution:", h_pos * depth)

# Part 2
h_pos = 0
depth = 0
aim = 0

for input in split:
    input = input.split(" ")
    
    if input[0] == "forward":
        h_pos += int(input[1])
        depth += aim * int(input[1])
    elif input[0] == "up":
        aim -= int(input[1])
    elif input[0] == "down":
        aim += int(input[1])
    else:
        print("Unknown input:", input[0], input[1])

print("Part 2:")
print("Horizontal position:", h_pos, "\nDepth:", depth)
print("Solution:", h_pos * depth)