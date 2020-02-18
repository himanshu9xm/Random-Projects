series = list(map(int, input().split()))
record = []
print(series)
length = len(series)
i = 0
while i < length:
    differnece = abs(series[i + 1] - series[i])
    for j in range(i, length):
        if abs(series[j + 1] - series[j]) == differnece:
            continue
        else:
            record.append(i)
            record.append(j)
            record.append(j - i)
            i = j
            break

print(record)
