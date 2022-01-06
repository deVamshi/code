string = "abasijeorjwiegwjijrffffff"
has = {}
for i in string:
    if i in has:
        has[i] += 1
    else:
        has[i] = 1
freqList = sorted(has.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

for i in range(len(freqList)):
    freqList[i] = list(freqList[i])

loopingCount = 0
if len(freqList) >= 1:
    loopingCount = freqList[0][1]
out = " "
notPossible = False
for i in range(loopingCount):
    for itemSet in freqList:
        if itemSet[1] == 0:
            break
        if out[-1] == itemSet[0]:
            notPossible = True
        out += itemSet[0]
        itemSet[1] -= 1
    if notPossible:
        break

if notPossible or loopingCount == 0:
    print("NOT POSSIBLE" )
else:
    print(out.strip())


