# The increased counter starts at -1 because the first maesurement will always be bigger because it compares to 0
decreased = 0
no_change = 0
increased = -1

file = open("input.txt", "r")
split = file.read().split("\n")

# Part 1
last_height = 0
for h in split:    
    height = int(h)
    
    if height < last_height:
        decreased += 1
    elif height == last_height:
        no_change += 1
    else:
        increased += 1

    last_height = height 

print("The depth increased", increased,"times, decreased", decreased, "times and didn't change", no_change, "times")

# Part 2
decreased = 0
no_change = 0
increased = -1

windows = [len(split) - 2]
window = 0

# Put the windows in an array
while window < len(split) - 2:
    windows.append(int(split[window]) + int(split[window + 1]) + int(split[window + 2]))
    window += 1

last_window = 0
for window in windows:        
    if window < last_window:
        decreased += 1
    elif window == last_window:
        no_change += 1
    else:
        increased += 1

    last_window = window 

print("The depth increased", increased,"times, decreased", decreased, "times and didn't change", no_change, "times when using three-measurement sliding windows")