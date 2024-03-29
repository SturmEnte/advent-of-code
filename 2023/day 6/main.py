from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print("---Part 1---")
def parse(part):
    if part == 1:
        raw_times = input[0].split(":")[1].split(" ")
        raw_distances = input[1].split(":")[1].split(" ")

        times = []
        distances = []

        for time in raw_times:
            if time != "":
                times.append(int(time))

        for distance in raw_distances:
            if distance != "":
                distances.append(int(distance))

        if len(times) != len(distances):
            print(f"{Back.RED}There is a not equal amount of times and distances{Style.RESET_ALL}")

        races = []

        for i in range(len(times)):
            races.append((times[i], distances[i]))

        return races
    elif part == 2:
        raw_time = input[0].split(":")[1]
        raw_distance = input[1].split(":")[1]

        time = int(raw_time.replace(" ", ""))
        distance = int(raw_distance.replace(" ", ""))

        return (time, distance)

result = 1

races = parse(1)

for race in races:
    time = race[0]
    record = race[1]

    possibilities = []

    for speedup_time in range(0, time):
        travel_time = time - speedup_time
        distance = speedup_time * travel_time
        if distance > record:
            possibilities.append(speedup_time)

    print(possibilities)
    result *= len(possibilities)

print(f"Result: {result}")

# Part 2
print("---Part 2---")
result = 1

race = parse(2)

time = race[0]
record = race[1]

possibilities = []

for speedup_time in range(0, time):
    travel_time = time - speedup_time
    distance = speedup_time * travel_time
    if distance > record:
        possibilities.append(speedup_time)

# print(possibilities)
result *= len(possibilities)

print(f"Result: {result}")
