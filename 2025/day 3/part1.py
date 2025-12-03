file = open("input.txt", "r")
input = file.read().split("\n")

result = 0

for bank in input:
    
    largest_joltage = 0

    for a in range(len(bank)):
        for b in range(a, len(bank)):
            if a == b:
                continue

            joltage = int(bank[a] + bank[b])

            if joltage > largest_joltage:
                largest_joltage = joltage

    result += largest_joltage

print(f"Result: {result}")

file.close()