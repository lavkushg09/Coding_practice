def check_and_find_subset(arr, total_subset, index):
    if index == 0 and total_subset > 0:
        return False

    if index >=0 and total_subset == 0:
        return True

    if arr[index-1]<=total_subset:
        return check_and_find_subset(arr, total_subset-arr[index-1], index-1) or check_and_find_subset(arr, total_subset, index-1)
    else:
        return check_and_find_subset(arr, total_subset, index-1)
    
arr = [1,5,4,5]
total_subset = 13

print(check_and_find_subset(arr, total_subset, len(arr)))