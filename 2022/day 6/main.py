file = open("input.txt")
data = file.read()

# Part 1
last_4_chars = []
for i, char in enumerate(data):
    last_4_chars.append(char)

    if len(last_4_chars) > 4:
        last_4_chars.pop(0)

    x = False
    if len(last_4_chars) == 4:
        x = True
        # Compare oldest char with other chars
        for j in range(3):
            if last_4_chars[0] == last_4_chars[j + 1]:
                x = False
        
        for j in range(2):
            if last_4_chars[1] == last_4_chars[j + 2]:
                x = False

        for j in range(1):
            if last_4_chars[2] == last_4_chars[j + 3]:
                x = False

    if x == True:
        print("The first start-of-packet marker is received after", i + 1, "bytes")
        break