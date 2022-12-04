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

# Part 2

ogr = 0 # Oxyen generator rating
co2 = 0 # CO2 scrubber rating

# Turn the data into an 2 dimentional array ([x][y])
data = []

for j in range(width):
        data.append([])

for row in input:
        for j, cell in enumerate([char for char in row]):
                data[j].append(int(cell))

input = inputs
i = 0

odata = data
cdata = data

while i < width:
        
        # Oxygen
        x = 0

        for cell in odata[i]:
                x += cell

        mc = x / height

        if mc < 0.5:                    # More zeros than ones 
                new = []
                for cell in odata[i]:
                        if cell == 0:
                                new.append
        elif mc > 0.5 or mc == 0.5:     # More ones than zeros or Equal amount of zeros and ones
                continue

        # CO2
        x = 0

        for cell in cdata[i]:
                x += cell

        mc = x / height

        if mc < 0.5:                    # More zeros than ones or Equal amount of zeros and ones
                continue
        elif mc > 0.5 or mc == 0.5:     # More ones than zeros
                continue

        i += 1
        

print("Oxigen generator rating:", ogr)
print("CO2 scrubber rating:", co2)
print("Life support rating:", ogr * co2)