def extract_longest_palindrome(str_ins):
    res = ""
    for inx in range(len(str_ins)):
        w1 = check_and_get_palindrome(str_ins, inx, inx)
        w2 = check_and_get_palindrome(str_ins, inx, inx+1)
        longest = w1 if len(w1)>=len(w2) else w2

        res = longest if len(longest)>len(res) else res
    return res

def check_and_get_palindrome(str_ins, l, r):
    while l>=0 and r<len(str_ins) and str_ins[l] == str_ins[r]:
        l -=1
        r +=1
    return str_ins[l+1:r]
    
        
# print(extract_longest_palindrome())
print(extract_longest_palindrome("aabcdcbaxyzsdfgfdszyx"))