file = open("input.txt", "r")
content = file.read()
inputs = [char for char in content.replace("\n", "")]
width = content.split("\n")[0].__len__()
height = int(len(inputs) / width)

print("Width:", width)
print("Height:", height)

# Part 1
gamma_rate = ""
epsilon_rate = ""

for w in range(width):
    for h in range(height):
        print(inputs[w*h])

print("Gamma rate:", int(gamma_rate, 2))
print("Epsilon rate:", int(epsilon_rate, 2))