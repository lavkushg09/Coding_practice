

def bubble_sort(array_inst):
    for it in range(len(array_inst)):
        for i in range(len(array_inst)-1-it):
            if array_inst[i]> array_inst[i+1]:
                array_inst[i], array_inst[i+1] = array_inst[i+1], array_inst[i]

    return array_inst


    
