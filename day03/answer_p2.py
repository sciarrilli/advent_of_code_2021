import numpy as np
from collections import Counter

data = []
f = open('sample.txt', 'r')
for line in f:
    data.append(line.rstrip())
f.close()

col = len(data[0])
matrix = [int(digit) for num in data for digit in num]
matrix = np.array(matrix).reshape(-1, col)
print(matrix)
print(matrix.sum(axis=0))

ndt = matrix.copy()
curr_c = 0
while curr_c < len(matrix[0]):
    print(f"Current Col: {curr_c}")
    counts = [sorted(dict(Counter(ndt[:, curr_c])).items(), key=lambda item: item[1])]
    counts = np.array(counts).reshape(-1, 2)
    print(counts)
    if len(counts) > 1:
        if counts[0, 1] == counts[1, 1]:
            ndt = ndt[ndt[:, curr_c] == 1]
        else:
            ndt = ndt[ndt[:, curr_c] == counts[1][0]]
    else:
        ndt = ndt[ndt[:, curr_c] == counts[1][0]]
    print(f"Current Col: {curr_c} Rows: {len(ndt)}")

    curr_c += 1
res = int("".join(list(map(str, ndt[0]))), 2)
print(res)


ndt = matrix.copy()


curr_c = 0
while curr_c < len(matrix[0]):

    counts = [sorted(dict(Counter(ndt[:, curr_c])).items(), key=lambda item: item[1])]
    counts = np.array(counts).reshape(-1, 2)
    if len(counts) > 1:
        if counts[0, 1] == counts[1, 1]:
            ndt = ndt[ndt[:, curr_c] == 0]
        else:
            ndt = ndt[ndt[:, curr_c] == counts[0][0]]
    else:
        ndt = ndt[ndt[:, curr_c] == counts[0][0]]

    #         print(ndt)
    print(f"Current Col: {curr_c} Rows: {len(ndt)}")
    curr_c += 1
print(int("".join(list(map(str, ndt[0]))), 2))

'''
NOT WORKING!!!


x = {i: [] for i in range(len(data[0]))}

for binary in data:
    x[0].append(int(binary[0]))
    x[1].append(int(binary[1]))
    x[2].append(int(binary[2]))
    x[3].append(int(binary[3]))
    x[4].append(int(binary[4]))

# print(x)
# print(n)
# print(n // 2)

temp = data[:]
print(f'temp: {temp}')

i = 0
while len(temp) > 1:
    if sum(x[i]) == n // 2:
        print('bit == 1, sum == 6')
        for j in temp:
            if j[i] == '0':
                temp.remove(j)
        print(f'i: {i}, temp: {temp}')
        i += 1
    if sum(x[i]) > n // 2:
        print('bit == 1')
        for j in temp:
            # print(j[i])
            if j[i] == '0':
                print(j)
                temp.remove(j)
        print(f'i: {i}, temp: {temp}')
        i += 1
    else:
        print('bit == 0')
        for j in temp:
            if j[i] == '0':
                temp.remove(j)
        print(f'i: {i}, temp: {temp}')
        i += 1

print(temp)
print(data)



'''
