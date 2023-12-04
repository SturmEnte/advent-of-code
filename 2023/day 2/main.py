from colorama import Back, Style

file = open("input.txt", "r")
inputs = file.read().split("\n")

# Part 1
print("---Part 1---")
result = 0

for line in inputs:

    if line == "":
        break

    id = int(line.split(":")[0].split(" ")[1])

    possible = True

    for grab in line.split(":")[1].split(";"):
        
        red = 0
        green = 0
        blue = 0

        for cubes in grab.split(","):
            split = cubes[1:].split(" ")

            if split[1] == "red":
                red += int(split[0])
            elif split[1] == "green":
                green += int(split[0])
            elif split[1] == "blue":
                blue += int(split[0])
            else:
                print(Back.YELLOW + f"Error: {split[0]}" + Style.RESET_ALL)

        if red > 12 or green > 13 or blue > 14:
            possible = False  

    if possible:
        result += id
        print(Back.GREEN + f"{id}: r: {red} g: {green} b: {blue}"+ Style.RESET_ALL)
    else:
        print(Back.RED + f"{id}: r: {red} g: {green} b: {blue}"+ Style.RESET_ALL)

print(f"Result: {result}")

# Part 2
print("---Part 2---")
result = 0

for line in inputs:

    if line == "":
        break

    id = int(line.split(":")[0].split(" ")[1])

    possible = True

    lred = 0
    lgreen = 0
    lblue = 0

    for grab in line.split(":")[1].split(";"):
        
        red = 0
        green = 0
        blue = 0

        for cubes in grab.split(","):
            split = cubes[1:].split(" ")

            if split[1] == "red":
                red += int(split[0])
            elif split[1] == "green":
                green += int(split[0])
            elif split[1] == "blue":
                blue += int(split[0])
            else:
                print(Back.YELLOW + f"Error: {split[0]}" + Style.RESET_ALL)

        if red > lred:
            lred = red

        if green > lgreen:
            lgreen = green

        if blue > lblue:
            lblue = blue  

    result += lred * lgreen * lblue

    # if possible:
    #     result += id
    #     print(Back.GREEN + f"{id}: r: {red} g: {green} b: {blue}"+ Style.RESET_ALL)
    # else:
    #     print(Back.RED + f"{id}: r: {red} g: {green} b: {blue}"+ Style.RESET_ALL)

print(f"Result: {result}")