"""
Array should be sorted
Time complexity in worst case is O(logn)
like 8 it should in 3 
16 ---> 4 steps
32 --- 5 steps
"""
import time

def binary_search(array_inst, target):
    if len(array_inst)==0:
        return -1

    left = 0
    right = len(array_inst) - 1
    while left<=right:
        mid_index = (right+left) // 2
        if array_inst[mid_index] == target:
            return mid_index
        elif array_inst[mid_index] > target:
            right = mid_index-1
        else:
            left = mid_index+1

    return -1

    


# recursion Method

def binary_search_using_recursion(array_inst, target):
    if len(array_inst)==0:
        return -1

    left = 0
    right = len(array_inst) - 1
    return binray_helper(left, right, array_inst, target)


def binray_helper(left, right, array_inst, target):
    
    if left>right:
        return -1
    mid = (left + right) // 2
    if array_inst[mid] == target:
        return mid
    elif array_inst[mid] > target:
        right = mid-1
    else:
        left = mid+1
    return binray_helper(left, right, array_inst, target)


input_array = [2,4,5,7,8,9,15,20,25,30,32,35]
target = 30
t1 = time.time()
res = binary_search_using_recursion(input_array, target)
r_t = time.time()-t1
print(f"Using recursion method index of element {res}. time taken to complate {r_t} second")

t_w = time.time()
res = binary_search(input_array, target)
r_t_w = time.time()-t_w
print(f"Using while loop method index of element {res}. time taken to complate {r_t_w} second")