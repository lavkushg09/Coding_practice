
# Brute-force Method solution
# Time complexity is O(n2)
# Space complexity is O(1)
def find_pair_of_element_equal_to_target_brute_force(array_inst, target):
    if len(array_inst)<2:
        return [-1]
    for inx in range(len(array_inst)-1):
        for internal_inx in range(inx+1, len(array_inst)):
            if array_inst[inx]+array_inst[internal_inx] == target:
                return [inx, internal_inx]
    return [-1]


input_ar = [2,7,11,15]
target = 18

# print(find_pair_of_element_equal_to_target_brute_force(input_ar, target))


# Hash map approach to find out the index of the pair
# Time complexity of O(n)
# Space complexity is O(n)
# def find_pair_of_element_equal_to_target_hash_map(array_inst, target):
#     has_map = {}

#     for inx in range(len(array_inst)):
#         value = array_inst[inx]
#         try:
#             index = has_map[str(value)]
#             return [index, inx]
#         except KeyError:
#             has_map[str(target-value)] = inx
#     return [-1]

# print(find_pair_of_element_equal_to_target_hash_map(input_ar, target))



# we can use binary search for achieving solution in sorted array
# """


def find_pair_of_element_equal_to_target_binary_search(array_ins, target):
    for inx in range(len(array_ins)):
        value = array_ins[inx]
        find_inx = find_element_in_binary_search(array_ins[inx+1:], target-value)
        if find_inx != -1:
            return [inx, find_inx+1]
    return [-1]

def find_element_in_binary_search(array, element):
    array.sort()
    start = 0
    end = len(array)-1
    print(array, element)
    while start<=end:
        print(start, end)
        mid = (start+end)//2
        print(mid)
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            end = mid-1
        else:
            start = mid+1
    return -1

print(find_element_in_binary_search([11,5,7,6,9], 11))
print(find_pair_of_element_equal_to_target_binary_search(input_ar, target))


# """
# There are multiple ways we can achieve this using two pinter approach for sorted array