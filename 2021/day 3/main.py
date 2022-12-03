file = open("input.txt", "r")
content = file.read()
inputs = content.split("\n")
width = content.split("\n")[0].__len__()
height = int(len([char for char in content.replace("\n", "")]) / width)

print("Width:", width)
print("Height:", height)

# Part 1
gamma_rate = ""
epsilon_rate = ""

zeros = []
ones = []

for i in range(width):
        zeros.append(0)
        ones.append(0)


for h in range(height):
        row = [char for char in inputs[h]]
        for i, char in enumerate(row):
                if char == "0":
                        zeros[i] += 1
                elif char == "1":
                        ones[i] += 1

for i in range(width):
        if zeros[i] > ones[i]:
                gamma_rate += "0"
                epsilon_rate += "1"
        else:
                gamma_rate += "1"
                epsilon_rate += "0"

print("Gamma rate:", int(gamma_rate, 2))
print("Epsilon rate:", int(epsilon_rate, 2))
print("Submarine power comsumption:", int(gamma_rate, 2) * int(epsilon_rate, 2))