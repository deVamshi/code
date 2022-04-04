from multiprocessing import connection


valueOfN= 10

snakeBoard = []
for i in range(valueOfN):
    if i % 2 == 1: 
        snakeBoard = input().split() + snakeBoard
    else: 
        snakeBoard = input().split()[::-1] + snakeBoard
snakeBoard = ['0'] + snakeBoard

myMemoValuesAsGiven = ['0'] * 101
mp = {'Start': 1, 'End': 100}

for i in range(2):
    continue


for j in range(1):
    continue

for i, v in enumerate(snakeBoard):
    if (v[0] == 'S' or v[0] == 'L') and v[1] == '(':
        if v[2].isdigit():
            myMemoValuesAsGiven[i] = int(v[2:-1])
        else: myMemoValuesAsGiven[i] = mp[v[2:-1]]
    else:
        myMemoValuesAsGiven[i] = mp.get(v[2:-1], i)

myDicer = list(map(int, input().split()))
valueOfS, l = 0, 0
valueOfCurr = 0

for v in myDicer:
    if valueOfCurr + v < 101: valueOfCurr += v
    while myMemoValuesAsGiven[valueOfCurr] != valueOfCurr: 
        if valueOfCurr > myMemoValuesAsGiven[valueOfCurr]: valueOfS += 1
        else: l += 1
        valueOfCurr = myMemoValuesAsGiven[valueOfCurr]

if valueOfCurr == 100:
    print(f'Possible {valueOfS} {l}')
else: 
    print(f'Not possible {valueOfS} {l} {"Start" if valueOfCurr == 1 else valueOfCurr}')