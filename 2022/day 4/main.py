file = open("input.txt", "r")
inputs = file.read().split("\n")

fully_contained = 0

for input in inputs:
    start1, end1 = input.split(",")[0].split("-")
    start2, end2 = input.split(",")[1].split("-")

    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)

    if start1 <= start2 and end1 >= end2:
        fully_contained += 1
        print(start1, end1, start2, end2)
    elif start2 <= start1 and end2 >= end1:
        fully_contained += 1
        print(start1, end1, start2, end2)

print("Fully contained:",fully_contained)

overlaping = 0

for input in inputs:
    start1, end1 = input.split(",")[0].split("-")
    start2, end2 = input.split(",")[1].split("-")

    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)

    if end1 >= start2 and end1 <= end2:
        overlaping += 1
    elif end2 >= start1 and end2 <= end1:
        overlaping += 1

print("Overlaping:",overlaping)