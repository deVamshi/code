ls = [2,3,6]
n = len(ls)

def allPermsExtraSpace(ds, mp):
    if len(ds) == n:
        print(ds)
        return
    for i in range(n):
        if mp[i]: continue
        mp[i] = True
        ds.append(ls[i])
        allPermsExtraSpace(ds, mp)
        mp[i] = False
        ds.pop()
        
allPermsExtraSpace([], [False for i in range(n)])

def allPermNoExtraSpace(ind, ds):
    if ind == n:
        print(ds)
        return

    for i in range(ind, n):
        ds[ind], ds[i] = ds[i], ds[ind]
        allPermNoExtraSpace(ind + 1, ds)
        ds[ind], ds[i] = ds[i], ds[ind]
        
allPermNoExtraSpace(0, ls)