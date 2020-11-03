import sys
sys.stdin = open('1247.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    coor = list(map(int, input().split()))
    customers = []
    home = [coor[0], coor[1]]
    office = [coor[2], coor[3]]
    for i in range(4, 2*N+4, 2):
        customers.append([coor[i], coor[i+1]])
    print(home, office, customers)
    N = len(customers)
    visi


