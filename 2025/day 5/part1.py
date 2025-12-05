file = open("input.txt", "r")
input = file.read().split("\n")

result = 0
reading_ranges = True
fresh_id_ranges = []

for line in input:
    if line == "":
        reading_ranges = False
        continue

    if reading_ranges:
        start_id = int(line.split("-")[0])
        end_id = int(line.split("-")[1])
        fresh_id_ranges.append((start_id, end_id))
        continue

    # Reading and checking available ids
    id = int(line)
    for id_range in fresh_id_ranges:
        if id_range[0] <= id <= id_range[1]:
            result += 1
            break

print(f"Result: {result}")

file.close()