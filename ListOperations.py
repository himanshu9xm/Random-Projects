N = int(input())
operation = []
result = []

for i in range(N):
    operation.append(input().split())


for i in range(N):
    length = len(operation[i])
    for j in range(length):
        if operation[i][j] == "insert":
            result.insert(int(operation[i][j + 1]), int(operation[i][j + 2]))
            continue
        if operation[i][j] == "print":
            print(result)
            continue
        if operation[i][j] == "remove":
            result.remove(int(operation[i][j + 1]))
            continue
        if operation[i][j] == "append":
            result.append(int(operation[i][j + 1]))
            continue
        if operation[i][j] == "sort":
            result.sort()
            continue
        if operation[i][j] == "pop":
            result.pop()
            continue
        if operation[i][j] == "reverse":
            result.reverse()
            continue
