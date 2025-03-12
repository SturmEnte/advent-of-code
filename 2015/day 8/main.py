from colorama import Back, Style

file = open("input.txt", "r")
input = file.read().split("\n")

# Part 1
print(f"{Back.LIGHTWHITE_EX}---Part 1---{Style.RESET_ALL}")
result = 0

literal_chars = 0
mem_chars = 0

for line in input:
    literal_chars += len(line)
    #print(len(line))

    line = line[1:len(line)-1]

    line = line.replace("\\\\", "\\")
    line = line.replace("\\\"", "\"")

    line_as_array = list(line)

    for i, char in enumerate(line_as_array):
        if i < len(line_as_array) - 3 and char + line_as_array[i+1] == "\\x":
            replacement = line_as_array[i+2]+line_as_array[i+3]
            #replacement = bytes.fromhex(replacement).decode('latin-1')

            line = line.replace("\\x" + line_as_array[i+2] + line_as_array[i+3], "#")

    #print(len(line))
    print(line)
    mem_chars += len(line)

result = literal_chars - mem_chars
print(f"Literal Chars: {literal_chars}")
print(f"Mem Chars: {mem_chars}")
print(f"Result: {result}")

# Part 2
print(f"{Back.LIGHTWHITE_EX}---Part 2---{Style.RESET_ALL}")
result = 0



print(f"Result: {result}")

file.close()