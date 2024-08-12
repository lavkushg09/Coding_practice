def get_longest_sub_array(arr, target):
    s_inx =e_inx =0
    sum =0
    max_size = 0
    while e_inx < len(arr):
        if sum<=target:
            sum += arr[e_inx]
            if sum == target:
                max_size = max(max_size, e_inx-s_inx+1)
            e_inx +=1
        else :
            while sum >= target:
                sum -= arr[s_inx]
                s_inx +=1
    return max_size


a=[4,1,1,1,2,3,5,0,1,1,2,0,1]
target = 5
print(get_longest_sub_array(a,target))