A = list(map(int, input().split()))
A.pop(0)
A.sort()


i = 0
for i in range(len(A)):
    if A[i] - A[i-1] == 2:
        print(A[i] - 1)
        exit()

print(A[i] + 1)