
k = int(input())
for j in range(k):
    n = int(input())
    l = list(map(int, input().split()))
    l.append("noone")
    uniq = list(set(l))
    globalCount = float('-inf')
    maxEle = float('inf')
    for ele in uniq:
        localCount = 1
        i = 0
        while i < n:
            if ele == l[i]: localCount += 1
            if l[i] == l[i + 1]: i += 2
            else: i += 1
        if localCount > globalCount:
            if localCount == globalCount:
                maxEle = min(maxEle, ele)
            else:
                maxEle = ele
            globalCount = localCount
    print(maxEle)
                



    
