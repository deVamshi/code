# https://codeforces.com/problemset/problem/158/A


n, k = map(int, input().split())
l = list(map(int, input().split()))
kth_val = l[k - 1]
count = 0
total = 0
i = 0
while i < n and  l[i] >= kth_val:
    count += 1
    total += l[i]
    i += 1

print(count if total > 0 else 0)
