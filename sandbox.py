inp = input()
isEvenFound = False
minEven = float('infinity')
numList = []

for i in inp:
    if i.isnumeric():
        if i not in numList:
            numList.append(i)
        if int(i) % 2 == 0:
            isEvenFound = True
            if int(i) < float(minEven):
                minEven = i

if isEvenFound:
    numList.remove(minEven)
    numList.sort(reverse=True)
    out = "".join(numList)
    out += minEven
    print(out)
else:
    print(-1)