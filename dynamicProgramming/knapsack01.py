# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# Input:
#   Two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
#   Integer W which represents knapsack capacity,
# Output:
#   Maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.

# val = { 60, 100, 120 }
# wt = { 10, 20, 30 }
# W = 50
# Solution: 220 (100 + 120)

def knapsack(val, wt, W):
    n = len(val)
    # cols are weights 0 to W, rows are the items 0 to n
    table = [[-1 for i in range(W+1)] for j in range(n+1)]

    for k in range (n+1):
        for w in range (W+1):
            if k == 0 or w == 0:
                table[k][w] = 0
            elif wt[k-1] > w:
                table[k][w] = table[k-1][w]
            else:
                table[k][w] = max(table[k-1][w], val[k-1] + table[k-1][w-wt[k-1]])

    return table[n][W]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50

    print ("Maximum value possible: {}".format(knapsack(val, wt, W)))
