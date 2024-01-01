def selection_sort(array_ins):
    for j in range(len(array_ins)):
        min_value_index = j
        for i in range(j+1,len(array_ins)):
            if array_ins[i]<array_ins[min_value_index]:
                min_value_index = i
            
        array_ins[j] , array_ins[min_value_index] = array_ins[min_value_index], array_ins[j]
        print(array_ins, j,min_value_index, array_ins[min_value_index])
        
    print(array_ins)
    return array_ins
input_arr = [20,-5,10,15,12,2,-8,-6]
print(selection_sort(input_arr))