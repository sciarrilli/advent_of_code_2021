import pandas as pd

data = []
f = open('sample.txt', 'r')
for line in f:
    data.append(line.rstrip())
f.close()

print(data)
gamma = ''
epsilon = ''

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
for binary in data:
    x1.append(int(binary[0]))
    x2.append(int(binary[1]))
    x3.append(int(binary[2]))
    x4.append(int(binary[3]))
    x5.append(int(binary[4]))

print(x1, x2, x3, x4, x5)
print(sum(x1), sum(x2), sum(x3), sum(x4), sum(x5))

if sum(x1) > 6:
    gamma += str(1)
else:
    gamma += str(0)
if sum(x2) > 6:
    gamma += str(1)
else:
    gamma += str(0)
if sum(x3) > 6:
    gamma += str(1)
else:
    gamma += str(0)
if sum(x4) > 6:
    gamma += str(1)
else:
    gamma += str(0)
if sum(x5) > 6:
    gamma += str(1)
else:
    gamma += str(0)

print(gamma)


for digit in gamma:
    if digit == '1':
        epsilon += str(0)
    else:
        epsilon += str(1)

print(epsilon)

pos = 16
gamma_val = 0
for digit in range(len(gamma)):
    print(gamma[digit])
    print(type(gamma[digit]))
    if gamma[digit] == '1':
        gamma_val += pos
        print(f'gamma_val {gamma_val}')
        pos //= 2
    else:
        pos //= 2
        print(f'pos {pos}')

pos = 16
epsilon_val = 0
for digit in range(len(epsilon)):
    print(epsilon[digit])
    print(type(epsilon[digit]))
    if epsilon[digit] == '1':
        epsilon_val += pos
        print(f'epsilon {epsilon_val}')
        pos //= 2
    else:
        pos //= 2
        print(f'pos {pos}')

print(epsilon_val)

print(gamma_val * epsilon_val)
