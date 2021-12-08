data = []
f = open('input.txt', 'r')
for line in f:
    data.append(line.rstrip())
f.close()

n = len(data[0])
# print(data)
gamma = ''
epsilon = ''

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
x11 = []
x12 = []
for binary in data:
    x1.append(int(binary[0]))
    x2.append(int(binary[1]))
    x3.append(int(binary[2]))
    x4.append(int(binary[3]))
    x5.append(int(binary[4]))
    x6.append(int(binary[5]))
    x7.append(int(binary[6]))
    x8.append(int(binary[7]))
    x9.append(int(binary[8]))
    x10.append(int(binary[9]))
    x11.append(int(binary[10]))
    x12.append(int(binary[11]))

# print(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)
# print(sum(x1), sum(x2), sum(x3), sum(x4), sum(x5))

for i in [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]:
    if sum(i) > len(data) // 2:
        gamma += str(1)
    else:
        gamma += str(0)


print(f'gamma: {gamma}')

for digit in gamma:
    if digit == '1':
        epsilon += str(0)
    else:
        epsilon += str(1)

print(f'epsilon: {epsilon}')

print(int('0b' + gamma, 2) * int('0b' + epsilon, 2))
