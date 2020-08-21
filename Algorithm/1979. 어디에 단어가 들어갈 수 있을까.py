import sys

sys.stdin = open('input.txt')

total_tc = int(input())

for tc in range (1, total_tc+1):
    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for h in table:
        for i in range(N):
            if h[i]==1:


    print(count)