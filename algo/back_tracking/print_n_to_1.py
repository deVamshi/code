

def myPrint(i, n):
    if i > n: return
    myPrint(i + 1, n)
    print(i)


n = int(input())
myPrint(1, n)
