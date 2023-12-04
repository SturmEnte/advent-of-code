file = open("input.txt", "r")
inputs = file.read().split("\n")

result = 0

for line in inputs:

    if line == "":
        break

    id = int(line.split(":")[0].split(" ")[1])

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
            else:
                blue += int(split[0])

    if red <= 12 and green <= 13 and blue <= blue:
        result += id

print(f"Result: {result}")
