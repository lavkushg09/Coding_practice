def get_first_negate_number_from_sub_array(arr, window_size):
    w_s = 0
    w_e = 0
    negative_res = []
    res = []
    while w_e < len(arr):
        if w_e-w_s+1 < window_size:
            if arr[w_e]<0:
                negative_res.append(arr[w_e])
            w_e +=1
        else:
            if len(negative_res)>0:
                res.append(negative_res[0])
                print(negative_res)
                if arr[w_s] == negative_res[0]:
                    negative_res.pop(0)
            else:
                res.append(0)
            if arr[w_e]<0:
                negative_res.append(arr[w_e])
            w_s +=1
            w_e +=1
    return res

a= [12,-1,-7,8,-15,10,11,13,14]

print(get_first_negate_number_from_sub_array(a, 3))


