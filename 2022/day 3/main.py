def char_to_priority(char):
    if char.isupper():
        return ord(char) - 64 + 26
    elif char.islower():
        return ord(char) - 96

file = open("input.txt")
inputs = file.read().split("\n")

# Part 1
priority = 0

for input in inputs:
    com1 = input[0:len(input)//2]
    com2 = input[len(input)//2 if len(input)%2 == 0 else ((len(input)//2)+1):]

    for char in com1:
        b = False
        for c in com2:
            if char == c:
                prio = char_to_priority(char)
                print(char, prio)
                priority += prio
                b = True
                break
        if b == True:
            break

print("Priority", priority)

# Part 2
priority = 0

i = 0
while i < len(inputs) / 3:
    mem1 = inputs[i * 3]
    mem2 = inputs[i * 3 + 1]
    mem3 = inputs[i * 3 + 2]

    a = False

    for x in mem1:
        if a == True: break
        for y in mem2:
            if a == True: break
            for z in mem3:
                if x == y and y == z:
                    print("Group item:", x)
                    priority += char_to_priority(x)
                    a = True
                    break
    i += 1

print("Priority", priority)