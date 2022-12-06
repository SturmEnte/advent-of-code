file = open("input.txt")
data = file.read()

# Part 1
last_4_chars = []
for i, char in enumerate(data):
    last_4_chars.append(char)

    while len(last_4_chars) > 4:
        last_4_chars.pop(0)

    received = False
    if len(last_4_chars) == 4:
        received = True
        for j in range(3):
            if last_4_chars[0] == last_4_chars[j + 1]:
                received = False
        
        for j in range(2):
            if last_4_chars[1] == last_4_chars[j + 2]:
                received = False

        for j in range(1):
            if last_4_chars[2] == last_4_chars[j + 3]:
                received = False

    if x == True:
        print("The first start-of-packet marker is received after", i + 1, "bytes")
        break
else:
    print("Never received an start-of-packet marker :(")

# Part 2
last_14_chars = []
for b, char in enumerate(data):
    last_14_chars.append(char)

    while len(last_14_chars) > 14:
        last_14_chars.pop(0)

    received = False
    if len(last_14_chars) == 14:
        received = True
        # This is NOT an efficient comparision technique because the bytes are compared multiple times with each other
        for j, char in enumerate(last_14_chars):
            for i in range(len(last_14_chars)):
                if i != j and char == last_14_chars[i]:
                    received = False

    if received == True:
        print("The first start-of-message marker is received after", b + 1, "bytes")
        break
else:
    print("Never received an start-of-message marker :(")