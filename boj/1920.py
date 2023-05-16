N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))

for b in B:
    print('1' if b in A else '0')
