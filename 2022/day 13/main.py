from copy import deepcopy
from json import loads

file = open("input.txt", "r")
input = file.read()
            
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
        
right_pairs = 0
for i, pair in enumerate(pairs):
    if compare(deepcopy(pair)) == True:
        right_pairs += i + 1

print("Right pairs:", right_pairs)