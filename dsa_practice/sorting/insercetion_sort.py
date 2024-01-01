def insercion_sort(array_ins):
    start_inx = 1
    for inx in range(start_inx, len(array_ins)):
        key=array_ins[inx]
        last = inx-1
        while last>=0 and key < array_ins[last]:
            array_ins[last+1] = array_ins[last]
            last  = last - 1
        array_ins[last+1] = key
    return array_ins
    
input_arr = [20,-5,10,15,12,2,-8,-6]
print(insercion_sort(input_arr))