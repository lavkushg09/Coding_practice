def revers_string(str_ins):
    length = len(str_ins)-1
    res = ""
    while length>=0:
        res = res + str_ins[length]
        length -=1
    return res

def revers_str_using_O_of_n(str_ins):
    last = len(str_ins)-1
    start = 0

    while last>start:
        str_ins[start], str_ins[last]  =  str_ins[last], str_ins[start]
        start +=1
        last -=1
    return str_ins

print(revers_string("i am lavkush."))
print(revers_str_using_O_of_n(['a', 'b','c','d', 'e']))