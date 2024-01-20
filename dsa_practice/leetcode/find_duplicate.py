def find_duplicate_items(nums):
    dict_map ={}
    duplicate_items = []
    for num in nums:
        if num in dict_map:
            dict_map[num] +=1
            duplicate_items.append(num) 
        else:
            dict_map[num] = 1
    return duplicate_items


a =[1, 2, 3, 6, 3, 6, 1]
print(find_duplicate_items(a))

    
