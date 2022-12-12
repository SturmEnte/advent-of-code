# This version is to slow for the input

file = open("input.txt", "r")
input = file.read()

map = []

start_pos = (0, 0)
target_pos = (0, 0)

for y, line in enumerate(input.split("\n")):
    if y == 0:
        for _ in range(len(line)):
            map.append([])
    
    for x, height in enumerate(line):
        map[x].append(ord(height))
        
        if height == "S":
            start_pos = (x, y)
            map[x][y] = ord("a")
        elif height == "E":
            target_pos = (x, y)
            map[x][y] = ord("z")

def possible_moves(x, y):
    pos = map[x][y]
    moves = []

    if x - 1 >= 0 and (map[x - 1][y] == pos or map[x - 1][y] + 1 == pos or map[x - 1][y] - 1 == pos):
        moves.append((x - 1, y))
    
    if x + 1 < len(map) and (map[x + 1][y] == pos or map[x + 1][y] + 1 == pos or map[x + 1][y] - 1 == pos):
        moves.append((x + 1, y))

    if y - 1 >= 0 and (map[x][y - 1] == pos or map[x][y - 1] + 1 == pos or map[x][y - 1] - 1 == pos):
        moves.append((x, y - 1))

    if y + 1 < len(map[0]) and (map[x][y + 1] == pos or map[x][y + 1] + 1 == pos or map[x][y + 1] - 1 == pos):
        moves.append((x, y + 1))

    return moves

x = False

rp = [(1,0), (1,1), (1,2), (2,2), (2,3)]

def way_to_target(pos, move_history, depth):
    move_history.append(pos)

    pos_moves = possible_moves(pos[0], pos[1])

    if depth == 0 or len(pos_moves) == 0 or (len(pos_moves) == 1 and pos_moves[0] == move_history[len(move_history) - 1]):
        return -99999999999999

    moves = []

    for move in pos_moves:
        if move == target_pos:
            return 1

        if move not in move_history:
            moves.append(way_to_target(move, move_history.copy(), depth - 1) + 1)

    n_moves = []

    for move in moves:
        if move > 0:
            n_moves.append(move)

    if len(n_moves) > 0:
        return sorted(n_moves)[0]

    return -99999999999999

print(way_to_target(start_pos, [], 1000))

