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
