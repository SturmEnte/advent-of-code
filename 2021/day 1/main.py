# The increased counter starts at -1 because the first maessurement will always be bigger because it compares to 0
decreased = 0
no_change = 0
increased = -1

file = open("input.txt", "r")

last_height = 0
for h in file.read().split("\n"):
    if h == "":
        continue
    
    height = int(h)

    print(height)
    print(last_height)
    
    if height < last_height:
        decreased += 1
    elif height == last_height:
        no_change += 1
    else:
        increased += 1

    last_height = height 

print("The depth increased", increased,"times, decreased", decreased, "times and didn't change", no_change, "times")