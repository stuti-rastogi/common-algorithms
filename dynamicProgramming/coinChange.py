# Given a value N, if we want to make change for N cents, 
# and we have infinite supply of each of D = {d1, d2, ..., dn} valued coins.
# What is the minimum number of coins needed to make change?

# Denominations: [6, 4, 1]
# N = 8
# Output = 2 (2 coins of 4)
MAXSIZE = 10


def coinChangeRec(d, n, N):
    c = [[-1 for i in range (N+1)] for j in range (n)]

    for i in range(n):
        c[i][0] = 0

    for i in range(n):
        for j in range(1,N+1):
            val1 = c[i-1][j] if i-1>=0 else float('inf')
            val2 = 1 + c[i][j-d[i]] if j-d[i]>=0 else float('inf')
            c[i][j] = min(val1, val2)

    return c[n-1][N]


def coinChange(d, N):
    n = len(d)
    return coinChangeRec(d, n, N)


if __name__ == "__main__":
    d = [1, 4, 6]
    N = 8
    print ("Minimum number of coins: {}".format(coinChange(d, N)))
