# Given two sequences, find the length of longest subsequence present in both of them.
# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

def lcs(x, y):
	m = len(x)
	n = len(y)

	# Adding extra row and col for i = 0 and j = 0
	# l[i][j] in this case has LCS of X[1...i-1] and Y[1...j-1]
	l = [[-1 for i in range(n+1)] for j in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				l[i][j] = 0
			# i goes from 0 to m, whereas x goes from 0 to m-1
			elif x[i-1] == y[j-1]:
				l[i][j] = l[i-1][j-1] + 1
			else:
				l[i][j] = max(l[i-1][j], l[i][j-1])

	return l[m][n]


if __name__ == "__main__":
	s1 = "ABCDGH"
	s2 = "AEDFHR"
	print ("Length of LCS of {0} and {1}\t: {2}".format(s1, s2, lcs(s1, s2)))

	s3 = "AGGTAB"
	s4 = "GXTXAYB"
	print ("Length of LCS of {0} and {1}\t: {2}".format(s3, s4, lcs(s3, s4)))
