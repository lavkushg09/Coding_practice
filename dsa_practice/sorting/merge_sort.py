def merge_sort(array_ins):
    """
    Time complexity for merge sort is O(n(logn)) in average, best and worst case
    Space complexity would be O(n)
    """

    # Start point of array
    start = 0

    # End Point of array
    end  = len(array_ins)

    # Base condition to break infinite loop
    if len(array_ins) == 1:
        return array_ins
    
    # calculating mid of the array index to split array in two part
    mid = (start+end)//2

    # Recursively calling for both part left and right
    left = merge_sort(array_ins[:mid])
    right = merge_sort(array_ins[mid:])
    return merge_two_list(left, right)

    

def merge_two_list(left, right):
    # Time complexity for this function is O(n+m). 
    # Where n and m is the respective length of the array

    # Initializing index for the array
    i=j=0

    # taking a variable to store sorted list
    res = []

    # Sorting both of the list and adding element in result list
    while i<len(left) and j< len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j +=1

    # This loop is running to copy remaining element if not added for left list
    while i<len(left):
        res.append(left[i])
        i+=1

    # This loop is running to copy remaining element if not added for right list
    while j<len(right):
        res.append(right[j])
        j+=1

    return res


input_arr = [4,6,1,5,3,7,2]
print(merge_sort(input_arr))
