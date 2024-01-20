def find_sub_array_which_have_max_sum(arr, wind_size):
    if len(arr)<wind_size:
        return []
    
    wid_start = 0
    wid_end= 0
    max_sum = 0
    sub_array = []
    sum=0
    while wid_end<len(arr):
        if wid_end-wid_start+1 <= wind_size:
            sum += arr[wid_end]
            wid_end +=1
            sub_array = arr[wid_start:wid_end]
        else:
            print(sum)
            if max_sum < sum:
                max_sum = sum
                sub_array=arr[wid_start:wid_end]
            sum -= arr[wid_start]
            sum += arr[wid_end]
            wid_start +=1
            wid_end +=1
    return sub_array, max_sum

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [2,3,4,6,11,2,6,3,7,8,9,6]


print(find_sub_array_which_have_max_sum(a, 3))

    

