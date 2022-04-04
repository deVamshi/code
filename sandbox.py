# inp = [[6, 4, 1, 9, 9, 4],[6,5,4,9,6,8],[4,1,6,9,7,5],[6,9,8,4,1,5],[4,1,6,9,8,6,1],[6,8,9,5,4,6,4]]
# inp = [[1,2,3,4],[1,3,5,7],[1,4,6,9],[4,6,7,6],[1,6,8,7]]
# inp = [[1,2],[2,3],[3,4],[4,5],[5,6]]

# from itertools import permutations
# from math import gcd
# from random import random

# inp = [5,10,15]
# maxGcd = float('-inf')
# mp = {}
# out = []
# n = 0
# maxInd = 0
# maxGcd = float('-inf')
# for i in range(len(inp)):
#     if inp[i] == 'seen': continue
#     curGcd = None
#     maxi = float('-inf')
#     for j in range(len(inp)):
#         if inp[j] == 'seen': continue
#         curGcd = gcd(inp[i], inp[j])
#         if curGcd > maxGcd:
#             maxGcd = curGcd
#             maxInd = j
#             maxi = inp[j]
#         else:
#             maxInd = j
#     out.append(maxi)
#     inp[maxInd] = "seen"
# print(out)

  
# ans = 2
# def computeGCD(x, y):
#    while(y):
#        x, y = y, x % y
#    return x
# def printCombination(arr, r):
#     data = [0]*r
 
#     combinationUtil(arr, data, 0,
#                     len(arr) - 1, 0, r)
 
# def combinationUtil(arr, data, start,
#                     end, index, r):    
#     global ans
#     if (index == r):
#         gc = 0
#         for j in range(r):
#             gc = computeGCD(data[j], gc)
#         if gc == ans:
#             ans += 1
#         return
#     i = start
#     while(i <= end and end - i + 1 >= r - index):
#         data[index] = arr[i]
#         combinationUtil(arr, data, i + 1,
#                         end, index + 1, r)
#         i += 1
# arr = [2,4,6,8]
# printCombination([2, 4, 6, 8], 2)
# print(ans)


# arr = [2,4]
# mp = {}

# for i in arr:
#     cnt = str(bin(i)).count('1')
#     if cnt in mp:
#         mp[cnt].append(i)
#     else:
#         mp[cnt] = [i]
# out = []
# for key in list(sorted(mp.keys())):
#     out.extend(sorted(mp[key])) 
# s = 1

# score = 0
# for i in reversed(out):
#     score += i * s
#     s *= 10
# print(score)


# def solve(N, A, X):
#     cnt = 0
#     mp = {}
#     res = [[]]
#     for num in sorted(A):
#         curr = []
#         curSum = 0
#         for item in res:
#             curr.append(item + [num])
#             curSum = 0
#             prev = str(item)
#             if prev not in mp: mp[prev] = sum(item)
#             curSum = mp[prev] + num
#             if curSum <= X: cnt += 1
#             else: break
#         res += curr

#     return cnt % (10 ** 9 + 7)


# from itertools import permutations

# n = 5
# m = 20
# out = 0
# allowed = [i for i in range(1, m + 1)]
# prev = None
# for i in list(permutations(allowed, n)):
#     prod = 1
#     if prev != i[0] and i[0] * i[0] <= m:
#         out += 1
#         prev = i[0]
#     for ind, ele in enumerate(i):
#         prod *= ele
#         if prod > m: break
#     else:
#         out += 1
#         print(i)

# print(out)
    





# while n < len(inp):
#     maxGcd = float('-inf')
#     maxi = float('-inf')
#     maxInd = 0

#     for ind, i in enumerate(inp):
#         if i == "seen": continue
#         curGcd = gcd(int(i), out[-1])
#         if curGcd > maxGcd:
#             maxGcd = curGcd
#             maxi = i
#             maxInd = ind

#     out[n] = maxi
#     inp[maxInd] = "seen"
#     n += 1

# print(out[1:])


# for i in list(allPerms):
#     curSum = 0
#     prev = None
#     if len(i) > 0: prev = i[0]
#     for ele in i:
#         curSum += gcd(ele, prev)
#         prev = ele
#     maxGcd = max(maxGcd, curSum)
#     mp[curSum] = i



# n = int(input())
# inp = []
# for i in range(n):
#     l = list(input())
#     inp.append(l)

# mp = {'2':[], '3':[], '5':[], '7':[]}

# for ind, i in enumerate(inp):
#     for prime in mp.keys():
#         if prime in i: 
#             mp[prime].append(i)

# ans = 0
# for key, value in mp.items():
#     n = len(value)
#     if n < 3: continue
#     nume = factorial(n)
#     denom = factorial(3) * (factorial(n - 3))
#     count = nume / denom
#     ans += int(count)
# return 
from datetime import timedelta, date
import calendar
inp = "20211201"

inp, givenWeekday, n = list(input().split(" "))
n = int(n)
year = int(inp[0:4])
month = int(inp[4:6])
day = int(inp[6:])
givenWeekday = givenWeekday.lower()
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

dateGiven = date(year, month, day)
found = False
i = 1
came = False
while True:
    if givenWeekday == calendar.day_name[dateGiven.weekday()][0:3].lower():
        print("NO", 0)
        break
    if is_prime(i):
        updatedDate = date(year, month, day) + timedelta(days=i)

        if calendar.day_name[updatedDate.weekday()][0:3].lower() == givenWeekday: came = True

        if is_prime(updatedDate.month):
            found = True
    if found: break
    if came: i += 7
    else: i += 1

if found: print("YES" if i <= n else "NO", i)





 



