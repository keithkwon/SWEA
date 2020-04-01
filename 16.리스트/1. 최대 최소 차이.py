a= int (input())


for i in range (1, a+1):
    b = int(input())
    c = list(map(int, input().split(' ')))
    d = max(c) - min(c)
    print(f"#{i} {d}")