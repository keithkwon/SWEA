n = int(input())


for i in range (1, n+1):
    k = str(i)
    a = 0
    for j in k:
        if int(j) ==3 or int(j) ==6 or int(j) ==9 :
            print('-', end=' ')
            a+=1

    if a == 0:
        print(i, end= ' ')
    








