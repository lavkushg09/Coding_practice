def find_product_of_array_except_itself(nums):
    product =1
    pre_product = [1]*len(nums)
    for i in range(1,len(nums)):
        product *= nums[i-1]
        pre_product[i] = product
    print(pre_product)
    product =1
    post_product = [1]*len(nums)
    for i in range(len(nums)-2, -1, -1):
        product *= nums[i+1]
        post_product[i] = product
    print(post_product)
    res = []
    for i in range(len(nums)):
        res.append(pre_product[i]*post_product[i])

    return res
        

a = [10, 3, 5, 6, 2]
print(find_product_of_array_except_itself(a))