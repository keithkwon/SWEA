a = int(input())

c=0


for i in range(1, a+1):



    k, n, m = map(int, input().split(' '))
    q=list(input().split(' '))
    q.append(f'{n}')
    

    print(q[0])
    print(q[m])

    start = 0 
    for move in range (k, 0, -1):
        for station in range (m, -1, -1):
            if start + move == q[station]:
                start = start + move
                
                break
        
                



print(c)


