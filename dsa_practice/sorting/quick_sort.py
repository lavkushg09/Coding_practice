def merge_sort(array):
    merge_sort_helper(0, len(array)-1, array)
    return array


def merge_sort_helper(start, end, array):
    piov = start
    left = start+1
    right = end
    if start >= end:
        return
    while left <= right:
        if array[piov] < array[left] and array[piov] > array[right]:
            array[left], array[right] = array[right], array[left]

        if array[piov] >= array[left]:
            left+=1
        
        if array[piov] <= array[right]:
            right -=1

    array[piov], array[right] = array[right], array[piov]
    merge_sort_helper(start, right-1, array)
    merge_sort_helper(right+1, end, array)


# input_arr = [4,6,1,5,3,7,2]
# merge_sort(input_arr)
# print(input_arr)



def quick_sort_implementing(array):
    """
    This quick sort implementation time complexity would be O(n(logn)) in best case for worst case is O(n2)

    Args:
        array 
    """

    start = 0
    end = len(array)-1
    quick_sort_helper(start, end, array)

def quick_sort_helper(start, end, array):
    # Taking pivot point at start of the array
    pi=start

    # Taking left pointer of next of pivot
    le=start+1

    # Taking right pointer last of array
    re=end

    # This is the base condition where if start and end is same it is indicating single element
    if start >=end:
        return 
    
    # Looping till the le is less or equal to the re
    while le<=re:
        # This condition we swap value from left and right because we want to move 
        # all less value before pivot and greater after pivot
        if array[pi]<array[le] and array[re]<array[pi]:
            swap_array(le, re, array)

        # condition for moving left pointer if less than pivot value 
        if array[pi]>array[le]:
            le += 1

        # condition for moving right pointer if greater than pivot value
        if array[pi] < array[re]:
            re -=1

        # once right cross the left this while loop got exit
        # after that we swap pivot with right in line number 69

    # swap pivot with right
    swap_array(pi, re, array)

    # calling again same method with left and right part of array to sort
    quick_sort_helper(start, re-1, array)
    quick_sort_helper(re+1, end, array)

def swap_array(le, re, array):
    array[le], array[re] = array[re], array[le]

input_arr = [4,6,1,5,3,7,2]
quick_sort_implementing(input_arr)
print(input_arr)