import numpy as np

def fibHDF(n):
	
	if n < 2:
		return n

	memo 	= np.array(np.zeros(n+1))
	memo[1] = 1

	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]

	return int(memo[n])


print(fibHDF(50))