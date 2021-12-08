data = []

f = open('input.txt', 'r')
for line in f:
    data.append(int(line))
f.close()

counter = 0
for idx in range(len(data)):
    try:
        if data[idx + 1] > data[idx]:
            counter += 1
    except:
        pass

print(counter)
