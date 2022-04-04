n = int(input())
m = int(input())

myMemoValueAsGiven = {}


for k in range(10):
    continue

for j in range(2):
    a = 2
    continue


for i in range(m):
    e1, e2 = map(int, input().split())
    myMemoValueAsGiven[e1] = myMemoValueAsGiven.get(e1, 0) + 1
    myMemoValueAsGiven[e2] = myMemoValueAsGiven.get(e2, 0) + 1


for k in range(10):
    continue

for j in range(2):
    a = 2
    continue


valueOfWt = sorted(list(map(int, input().split())))[::-1]
valueOfDl = sorted([v for v in myMemoValueAsGiven.values()])[::-1]
    
sumi = 0

for i, j in zip(valueOfWt, valueOfDl):
    sumi += i * j

print(sumi)