import numpy as np
# dp = [[-1]*10]*10
dp = [[-1]*10 for i in range(10)]

# for i in range(len(dp)):
# 	for j in range(len(dp[0])):
# 		if i == 0 or j == 0:
# 			dp[i][j] = 0

# for i in range(1,len(dp)):
# 	for j in range(1,len(dp[0])):
# 		if weight[i-1]<=j:
# 		dp[i][j] = max(dp[i-1]+dp[j(weight, price, k_weight-weight[length-1], length-1), 
# 	  		knapsack(weight,price,k_weight,length-1))
        
def knapsack(weight, price, k_weight, length) -> int:
	print(weight, price, k_weight, length, dp[k_weight][length])

	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if i == 0 or j == 0:
				dp[i][j] = 0

	for i in range(1,len(dp)):
		for j in range(1,len(dp[0])):
			if weight[i-1]<=j:
				dp[i][j] = max(price[i-1]+dp[j-dp[i-1]],dp[j][i-1])
			else:
				dp[i][j] = dp[i][j-1]

	# if k_weight==0 or length == 0:
	# 	return 0
	
	# if dp[k_weight][length] != -1:
	# 	return dp[k_weight][length]
	
	# if weight[length-1]<=k_weight:
	# 	max_p = max(price[length-1]+knapsack(weight, price, k_weight-weight[length-1], length-1), 
	#   		knapsack(weight,price,k_weight,length-1))
	# 	dp[k_weight][length] = max_p
	# 	return max_p
	# else:
	# 	p_p = knapsack(weight, price, k_weight, length-1)
	# 	dp[k_weight][length] = p_p
	# 	return p_p
	
weight = [1,3,5,8,9]
price = [10,20,30,40,50]
k_weight = 6

print(knapsack(weight, price, k_weight, 5))
print(np.matrix(dp))