def linear_search(array_ins, target):
    for i in range(len(array_ins)):
        if array_ins[i] == target:
            return i
    return -1

res = linear_search([1,5,6,8,9], 9)
print(res)


# Time complexity for this function is 
# O(n) in worst
#O(1) in best
#O(n) in avarage

# Space Conplexity
# O(1)