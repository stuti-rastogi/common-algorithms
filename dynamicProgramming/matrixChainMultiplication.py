# Given an array p[] which represents the chain of matrices 
# such that the ith matrix Ai is of dimension p[i-1] x p[i]. 
# We need to write a function MatrixChainOrder() that should return 
# the minimum number of multiplications needed to multiply the chain. 

# Input: p[] = {40, 20, 30, 10, 30}
# A1: 40x20
# A2: 20x30
# A3: 30x10
# A4: 10x30
# Output: 26000 (A1 (A2 A3) )A4 --> 20*30*10 + 40*20*10 + 40*10*30

MAXSIZE = 10
memo = [[-1 for col in range(MAXSIZE)] for row in range(MAXSIZE)]


def MatrixChainOrderRec(p, i, j):
	if memo[i][j] != -1:
		return memo[i][j]

	if i == j:
		memo[i][j] = 0
		return memo[i][j]

	memo[i][j] = float('inf')
	for k in range(i, j):
		memo[i][j] = min(
							memo[i][j], 
							MatrixChainOrderRec(p, i, k) + MatrixChainOrderRec(p, k+1, j) + (p[i-1] * p[k] * p[j])
						)
	return memo[i][j]


def MatrixChainOrder(p):
	n = len(p)
	return MatrixChainOrderRec(p, 1, n-1)


if __name__ == "__main__":
	p = [40, 20, 30, 10, 30]
	print ("Minimum number of multiplications: {}".format(MatrixChainOrder(p)))
