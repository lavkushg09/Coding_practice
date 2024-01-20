import numpy as np
weight = [2,3,4,5]
price = [1,2,3,4]
container_weight = 12
weight = [1,3,5,8,9]
price = [10,20,30,40,50]
k_weight = 6


# This solution is used to recursion and memorization
memo = [[-1]*(k_weight+1) for _ in range(len(weight)+1)] 
print(np.matrix(memo))

def find_max_price(weight, price, index, container_weight):
    print(index, container_weight)
    if index == 0 or container_weight == 0:
        return 0
    
    if memo[index-1][container_weight] != -1:
        return memo[index-1][container_weight]
    
    if weight[index-1] <= container_weight:
        memo[index-1][container_weight] = max(price[index-1]+find_max_price(weight, price, index-1, container_weight-weight[index-1]),
                   find_max_price(weight, price, index-1, container_weight))
        return memo[index-1][container_weight]
    else:
        memo[index-1][container_weight] = find_max_price(weight, price, index-1, container_weight)
        return memo[index-1][container_weight]
    



# this solution is using top down methodology to find the maximum price(using dp)  
def find_max_price_using_dp(weight, price, index, container_weight):
    dp_t = [[-1]*(container_weight+1) for _ in range(len(weight)+1)]
    print(np.matrix(dp_t))

    # initialize_table_with
    for i in range(len(dp_t)):
        for j in range(len(dp_t[0])):
            if i == 0 or j == 0:
                dp_t[i][j] = 0
    
    for i in range(1,len(dp_t)):
        for j in range(1,len(dp_t[0])):
            if weight[i-1]<=j:
                dp_t[i][j] = max(price[i-1]+dp_t[i-1][j-weight[i-1]],dp_t[i-1][j])
            else:
                dp_t[i][j] = dp_t[i-1][j]
    print(np.matrix(dp_t))
    return dp_t[len(weight)][container_weight]
    
    
# print(find_max_price(weight, price, len(weight), k_weight))
print(find_max_price_using_dp(weight, price, len(weight), k_weight))
print(np.matrix(memo))