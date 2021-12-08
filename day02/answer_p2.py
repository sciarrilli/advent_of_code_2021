data = []

f = open('input.txt', 'r')
for line in f:
    data.append(line.split())
f.close()

# print(data)

hor, dep, aim = 0, 0, 0

for comm in data:
    if comm[0] == 'forward':
        hor += int(comm[1])
        dep += aim * int(comm[1])
        # print(f'aim {aim}, dep {dep}')
    elif comm[0] == 'down':
        # dep += int(comm[1])
        aim += int(comm[1])
    elif comm[0] == 'up':
        # dep -= int(comm[1])
        aim -= int(comm[1])

print(hor, dep)
print(hor * dep)
