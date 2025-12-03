file = open("input.txt", "r")
input = file.read().split("\n")

result = 0

# Choose the largest number in the number array in all numbers from the first to the nth so that the last depth numbers remain for the next cycle
# After choosing the number and storing its index give the remaining numbers (those which come after the index of the largest)
# Do this until depth 1 is reached. Then combine all the largest numbers after the current number and return the resulting number
def find_largest_number_of_n(numbers: list[int], depth: int) -> int:
    
    largest_number = 0
    largest_index = 0

    for i, number in enumerate(numbers[:len(numbers) - depth + 1]):
        if number > largest_number:
            largest_number = number
            largest_index = i

    if depth == 1:
        return largest_number

    following_numbers = str(find_largest_number_of_n(numbers[largest_index + 1:], depth - 1))

    return int(str(largest_number) + following_numbers)

for bank in input:
    
    print(f"Computing {bank}...")

    joltages = []
    for letter in bank:
        joltages.append(int(letter))

    largest_joltage = find_largest_number_of_n(joltages, 12)

    print(largest_joltage)

    result += largest_joltage

print(f"Result: {result}")

file.close()