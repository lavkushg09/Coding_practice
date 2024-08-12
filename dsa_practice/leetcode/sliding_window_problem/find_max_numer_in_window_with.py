def find_max_number_in_window(arr, window):
    s_inx = e_inx = 0
    calculation_list = []
    res = []
    while e_inx < len(arr):
        if e_inx-s_inx+1 < window:
            if len(calculation_list)==0:
                calculation_list.append(arr[e_inx])
            else:
                if arr[e_inx] > calculation_list[0]:
                    calculation_list.pop(0)
                    calculation_list.append(arr[e_inx])
            e_inx += 1
        else:
            print(f"{arr[s_inx]} {e_inx=}")
            print(len(calculation_list) and arr[s_inx] == calculation_list[0] , (e_inx-s_inx+1 > window))
            # if len(calculation_list) and arr[s_inx] == calculation_list[0]:
            #     calculation_list.pop(0)
            while len(calculation_list)>0:
                if arr[e_inx] >= calculation_list[0]:
                    calculation_list.pop(0)
                    # calculation_list.append(arr[e_inx])
                else:
                    calculation_list.append(arr[e_inx])
                    break
            if len(calculation_list)==0:
                calculation_list.append(arr[e_inx])
            res.append(calculation_list[0])
            if len(calculation_list) and arr[s_inx] == calculation_list[0]:
                calculation_list.pop(0)
            s_inx += 1
            e_inx += 1
        print("Calculation list", calculation_list)
    return res
a=[1,3,-1,-3,5,3,6,7,1,-2,-11,3,6,9]

window = 3

print(find_max_number_in_window(a,window))