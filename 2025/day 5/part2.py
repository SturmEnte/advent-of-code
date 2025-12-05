from copy import deepcopy

file = open("input.txt", "r")
input = file.read().split("\n")

# Read id ranges from fiile
id_ranges = []

for line in input:
    if line == "":
        break

    start_id = int(line.split("-")[0])
    end_id = int(line.split("-")[1])
    id_ranges.append((start_id, end_id))

# Combine id ranges
def combine_ranges(ranges):
    combineable = None
    for i in range(len(ranges)):
        for j in range(len(ranges)):
            if i == j:
                continue

            # Two ranges can be combined if:
            # rangex_start between rangey_start and end
            if ranges[i][0] <= ranges[j][0] <= ranges[i][1] or ranges[j][0] <= ranges[i][0] <= ranges[j][1]:
                combineable = (i, j)
                break

            # rangex_end between rangey_start and end
            if ranges[i][0] <= ranges[j][1] <= ranges[i][1] or ranges[j][0] <= ranges[i][1] <= ranges[j][1]:
                combineable = (i, j)
                break

    if combineable == None:
        return ranges

    print(f"{id_ranges[combineable[0]]} and {id_ranges[combineable[1]]} are combineable")

    # Combine the combineable ranges
    new_ranges = deepcopy(ranges)
    range1 = new_ranges.pop(combineable[0])
    range2 = new_ranges.pop(combineable[1])

    # Set beginning of range to lower value
    start = range2[0]
    if range1[0] < range2[0]:
        start = range1[0]
    
    # Set end of range to higher value
    end = range2[1]
    if range1[1] > range2[1]:
        end = range1[1]

    new_ranges.append((start, end))

    return combine_ranges(new_ranges)

id_ranges = combine_ranges(id_ranges)

# Add the size of each range to get the result 
result = 0

for id_range in id_ranges:
    result += id_range[1] - id_range[0] + 1

print("Result:", result)

file.close()