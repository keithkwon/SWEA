a=int(input())

b=0


for i in range (1, a+1, 1):
    if a%i==0:
        b+=1


if b==2:
    print('소수입니다.')

else :
    print('소수가 아닙니다.')