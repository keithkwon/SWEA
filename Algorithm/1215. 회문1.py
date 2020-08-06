import sys
sys.stdin = open('input.txt')

total_tc = 10

for tc in range(1, total_tc+1):
    pali_len = int(input())
    pali_len-=1
    table = [[input()]for _ in range (8)]
    count = 0
    for i in range (8-pali_len):
        for j in range (8-pali_len):
7            if table[i][j]==table[i+pali_len::-1][j]:
                count +=1

    print (count)


