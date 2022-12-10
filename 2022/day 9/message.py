field = [["H"]]
path_field = [["#"]]

with open("example.txt", "r") as f:
    lines = f.readlines()

def expand_x(direction):
    if direction == "left":
        for row in field:
            row.insert(0, ".")
    if direction == "right":
        for row in field:
            row.append(".")
    if direction == "left":
        for row in path_field:
            row.insert(0, ".")
    if direction == "right":
        for row in path_field:
            row.append(".")

def expand_y(direction):
    row = []
    for i in field[0]:
        row.append(".")
    if direction == "up":
        field.insert(0, row)
    if direction == "down":
        field.append(row)
    row = []
    for i in field[0]:
        row.append(".")
    if direction == "up":
        path_field.insert(0, row)
    if direction == "down":
        path_field.append(row)

def get_pos(figure):
    x = None
    y = None
    for i, row in enumerate(field):
        try:
            x = row.index(figure)
            y = i
            break
        except ValueError:
            pass
    if x == None or y == None:
        for i, row in enumerate(field):
            try:
                x = row.index("H")
                y = i
                break
            except ValueError:
                pass
    return (x,y)
    
def move(figure, coords_old, coords_new):
    print("move ",figure)
    overlap = True
    for row in field:
        if "T" in row:
            overlap = False
            break
    if overlap:
        field[coords_old[1]][coords_old[0]] = "T"
        path_field[coords_old[1]][coords_old[0]] = "#"
        print("set t to ",coords_old)
    else:
        field[coords_old[1]][coords_old[0]] = "."
        if figure == "T":
            path_field[coords_old[1]][coords_old[0]] = "#"
    field[coords_new[1]][coords_new[0]] = figure
    if figure == "T":
        path_field[coords_new[1]][coords_new[0]] = "#"

def show(fld):
    for row in fld:
        print(row)

def get_touch(pos):
    touching = True
    for row in field:
        if "T" in row:
            touching = False
            break
    if touching == False:
        touching_fields = []
        try:
            if -1 not in (pos[1],pos[0]+1):
                print(pos[1],pos[0]+1,field[pos[1]][pos[0]+1])
                touching_fields.append(field[pos[1]][pos[0]+1])
        except:
            pass
        try:
            if -1 not in (pos[1],pos[0]-1):
                print(pos[1],pos[0]-1,field[pos[1]][pos[0]-1])
                touching_fields.append(field[pos[1]][pos[0]-1])
        except:
            pass
        try:
            if -1 not in (pos[1]+1,pos[0]+1):
                print(pos[1]+1,pos[0]+1,field[pos[1]+1][pos[0]+1])
                touching_fields.append(field[pos[1]+1][pos[0]+1])
        except:
            pass
        try:
            if -1 not in (pos[1]+1,pos[0]):
                print(pos[1]+1,pos[0],field[pos[1]+1][pos[0]])
                touching_fields.append(field[pos[1]+1][pos[0]])
        except:
            pass
        try:
            if -1 not in (pos[1]+1,pos[0]-1):
                print(pos[1]+1,pos[0]-1,field[pos[1]+1][pos[0]-1])
                touching_fields.append(field[pos[1]+1][pos[0]-1])
        except:
            pass
        try:
            if -1 not in (pos[1]-1,pos[0]+1):
                print(pos[1]-1,pos[0]+1,field[pos[1]-1][pos[0]+1])
                touching_fields.append(field[pos[1]-1][pos[0]+1])
        except:
            pass
        try:
            if -1 not in (pos[1]-1,pos[0]):
                print(pos[1]-1,pos[0],field[pos[1]-1][pos[0]])
                touching_fields.append(field[pos[1]-1][pos[0]])
        except:
            pass
        try:
            if -1 not in (pos[1]-1,pos[0]-1):
                print(pos[1]-1,pos[0]-1,field[pos[1]-1][pos[0]-1])
                touching_fields.append(field[pos[1]-1][pos[0]-1])
        except:
            pass
        print("Touching fields:", touching_fields)
        if "T" in touching_fields:
            touching = True
    return touching

for line in lines:
    direction = line[0]
    for i in range(int(line[2:-1])):        
        h_pos = get_pos("H")

        #h movement
        if direction == "R":
            new_h_pos = (h_pos[0]+1, h_pos[1])
            print(new_h_pos)
            if new_h_pos[0] >= len(field[0]):
                expand_x("right")
            move("H", h_pos, new_h_pos)
        
        elif direction == "L":
            new_h_pos = (h_pos[0]-1, h_pos[1])
            if new_h_pos[0] < 0:
                expand_x("left")
                h_pos = get_pos("H")
                new_h_pos = (h_pos[0]-1, h_pos[1])
            move("H", h_pos, new_h_pos)

        elif direction == "U":
            new_h_pos = (h_pos[0], h_pos[1]-1)
            if new_h_pos[1] < 0:
                expand_y("up")
                h_pos = get_pos("H")
                new_h_pos = (h_pos[0], h_pos[1]-1)
            move("H", h_pos, new_h_pos)
        
        elif direction == "D":
            new_h_pos = (h_pos[0], h_pos[1]+1)
            print(new_h_pos)
            if new_h_pos[1] >= len(field):
                expand_y("down")
            move("H", h_pos, new_h_pos)
        
        #t movement
        h_pos = get_pos("H")
        t_pos = get_pos("T")
        is_touching = get_touch(h_pos)
        if not is_touching:
            print("not touching")
            if t_pos[0] < h_pos[0]-1:
                move("T", t_pos, (h_pos[0]-1, h_pos[1]))
            elif t_pos[0] > h_pos[0]+1:
                move("T", t_pos, (h_pos[0]+1, h_pos[1]))
            elif t_pos[1] < h_pos[1]:
                move("T", t_pos, (h_pos[0], h_pos[1]-1))
            elif t_pos[1] > h_pos[1]:
                move("T", t_pos, (h_pos[0], h_pos[1]+1))
        
        print(line[0:-1])
        #show(field)
print("\nEND RESULT: ------------------------------------")
show(field)
print("\n")
show(path_field)
field_visits = 0
for row in path_field:
    for char in row:
        if char == "#":
            field_visits += 1
print(field_visits)