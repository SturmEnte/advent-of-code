file = open("input.txt", "r")
lines = file.read().split("\n")

current_path = ""
folders = {'/': 0}

def cd(path):
    split = current_path.split("/")
    if path == "..":
        split.pop()
    elif path != "/":
        split.append(path)

    return "/".join(split)

for line in lines:
    split = line.split()
    if split[0] == "$":
        
        if split[1] == "cd":
            current_path = cd(split[2])
    else:
        if split[0] == "dir":
            if current_path == "":
                folders["/" + split[1]] = 0
            else:
                folders[current_path + "/" + split[1]] = 0
        else:
            if current_path == "":
                size = int(split[0])
                folders["/"] += size
            else:
                size = int(split[0])
                folders[current_path] += size

total_size = 0
for folder in folders:
    if folders[folder] <= 100000:
        total_size += folders[folder]

print("Part 1:", total_size)
