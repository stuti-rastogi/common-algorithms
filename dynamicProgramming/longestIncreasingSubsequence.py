# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence 
# such that all elements of the subsequence are sorted in increasing order.

# Input: arr[] = {3, 10, 2, 1, 20}
# Output: Length of LIS = 3

# Input: arr[] = {3, 2}
# Output: Length of LIS = 1

# Input: arr[] = {50, 3, 10, 7, 40, 80}
# Output: Length of LIS = 4

def lis(arr):
	n = len(arr)
	lis = [1 for i in range(n)]

	for i in range(1, n):
		for j in range(i):
			if arr[j] < arr[i] and lis[i] < lis[j]+1:
				lis[i] = lis[j] + 1
	return lis[-1]


if __name__ == "__main__":
	arr1 = [3, 10, 2, 1, 20]
	print ("\nLength of LIS in {} is: {}\n".format(arr1, lis(arr1)))

	arr2 = [3, 2]
	print ("Length of LIS in {} is: {}\n".format(arr2, lis(arr2)))

	arr3 = [50, 3, 10, 7, 40, 80]
	print ("Length of LIS in {} is: {}\n".format(arr3, lis(arr3)))
