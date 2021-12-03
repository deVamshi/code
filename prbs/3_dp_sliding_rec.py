

def countWays(n):
    memo = {}
    def cWays(num):
        if num in memo: return memo[num]
        if num <= 1:
            return num
        else:
            memo[num] = cWays(num - 1) + cWays(num - 2)
            return memo[num]
             
    return cWays(n + 1) % (10 ** 9 + 7)
    # n + 1 because we need to calculate the no of ways to reach the nth step as well
