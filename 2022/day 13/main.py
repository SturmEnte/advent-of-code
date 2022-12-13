from copy import deepcopy
from json import loads

file = open("input.txt", "r")
input = file.read()

def compare(pair):
    left_a = pair[0]
    right_a = pair[1]

    for _ in range(len(right_a)):
        if len(left_a) == 0 and len(right_a) != 0:
            return True

        left = left_a.pop(0)
        right = right_a.pop(0)

        if type(left) == type(0) and type(right) == type(0):
            if left == right:
                continue
            elif left > right:
                return False
            elif left < right:
                return True
        elif type(left) == type([]) and type(right) == type([]):
            res = compare([left, right])
            if res != None:
                return res
        else:
            if type(left) == type(0):
                left = [left]
            else:
                right = [right]
            res = compare([left, right])
            if res != None:
                return res

    if len(left_a) > len(right_a):
        return False

    return None

# Part 1
print("---Part 1---")
pairs = [[]]

pair_i = 0
i = 0
for line in input.split("\n"):
    if line == "":
        pair_i += 1
        i = 0
        pairs.append([])
        continue
    pairs[pair_i].append([])
    pairs[pair_i][i] = loads(line)
    i += 1
        
right_pairs = 0
for i, pair in enumerate(pairs):
    if compare(deepcopy(pair)) == True:
        right_pairs += i + 1

print("Right pairs:", right_pairs)

# Part 2
print("---Part 2---")

packets = [[[2]], [[6]]]

for line in input.split("\n"):
    if line != "":
        packets.append(loads(line))

sorted = False

i = 0
while not sorted:
    if compare([deepcopy(packets[i]), deepcopy(packets[i + 1])]) == False:
        packets.insert(i, packets.pop(i + 1))
        i = 0
    else:
        i += 1
    
    if i == len(packets) - 1:
        sorted = True
        break

for p in packets: print(p)

d_packet2 = 1
d_packet6 = 1

for i, packet in enumerate(packets):
    if packet == [[2]]:
        d_packet2 += i
    elif packet == [[6]]:
        d_packet6 += i

print("Decoder key:", d_packet2 * d_packet6)