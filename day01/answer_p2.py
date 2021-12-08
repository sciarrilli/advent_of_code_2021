raw = []
n = 3

f = open('input.txt', 'r')
for line in f:
    raw.append(int(line))
f.close()


def sliding_window(l, n):
    start_window = 0
    s = 0
    data = []
    for end_window in range(len(l)):
        # print(raw[end_window])
        s += raw[end_window]
        if end_window >= n - 1:
            # print(f'sum {s}, start {start_window}, end {end_window}')
            data.append(s)
            s -= raw[start_window]
            start_window += 1

    counter = 0
    for idx in range(len(data)):
        # print(idx)
        if idx == len(data) - 1:
            break
        if data[idx + 1] > data[idx]:
            counter += 1
    return counter


print(sliding_window(raw, n))
