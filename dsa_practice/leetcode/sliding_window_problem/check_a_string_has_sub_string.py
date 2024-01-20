a="sdskhhfdfldfldforndlfdjffqwer"
sub = "fdjffqs"

def find_sub_string(s, sub_str):
    s_i=0
    e_i=0
    while e_i < len(s):
        if e_i-s_i+1 <= len(sub_str):
            e_i +=1
        else:
            if sub_str == s[s_i:e_i]:
                return True
            e_i += 1
            s_i += 1
    return False

# print(find_sub_string(a, sub))



def find_count_of_sub_strings_of_anagrams(s, sub):
    s_i=0
    e_i=0
    checker_map = count_char_map(sub)
    counter = len(checker_map.keys())
    count = 0
    print(f"{s_i=} {e_i=} {count=} {counter=} {checker_map=} {len(s)=}")
    print("================================================================")
    while e_i < len(s):
        # print(checker_map,counter)
        if e_i-s_i+1 <= len(sub):
            if s[e_i] in checker_map and checker_map[s[e_i]] != 0:
                checker_map[s[e_i]] -= 1
                if checker_map[s[e_i]] == 0:
                    counter -= 1
            elif s[e_i] in checker_map and checker_map[s[e_i]] == 0:
                checker_map[s[e_i]] -= 1
                counter +=1

            if counter == 0:
                count += 1

            e_i +=1
        else:
            if s[s_i] in checker_map:
                print(s[s_i], checker_map[s[s_i]])
                if checker_map[s[s_i]] == 0:
                    print("Checker")
                    counter += 1
                checker_map[s[s_i]] += 1
                print(checker_map,"Checker0000")
            s_i += 1
            if s[e_i] in checker_map and checker_map[s[e_i]] != 0:
                checker_map[s[e_i]] -= 1
                if checker_map[s[e_i]] == 0:
                    counter -= 1
            if counter == 0:
                count += 1
            # if counter == 0:
            #     count += 1
            # print(e_i,"=====",len(s))
            # get_ch = count_char_map(s[s_i:e_i])
            # if checker_map == get_ch:
            #     print(s[s_i:e_i])
            #     count += 1
            # if sub == s[s_i:e_i]:
            #     return True
                
            # v = s[e_i]
            e_i += 1
        print(f"{s_i=} {e_i=} {count=} {counter=} {checker_map=}")
        
            # s_i += 1
        
    return count

def count_char_map(st):
    map_ins = {}
    for i in range(len(st)):
        if st[i] in map_ins:
            map_ins[st[i]] += 1
        else:
            map_ins[st[i]] = 1
    return map_ins


a = "forxdorfedforsdefrofroffro"
# a="aabaabaa"
# sub = "aaba"
# a="aaba"
# sub = "ab"
sub = "for"

# print(find_count_of_sub_strings_of_anagrams(a, sub))


def find_count_of_sub_strings_of_anagrams_2(s, sub):
    st_inx = 0
    en_inx = 0
    checker_map = count_char_map(sub)
    counter = len(checker_map.keys())
    count = 0
    while en_inx < len(s):
        if en_inx-st_inx+1 <= len(sub):
            if s[en_inx] in checker_map:
                checker_map[s[en_inx]] -= 1
                if checker_map[s[en_inx]] == 0:
                    counter -= 1
            if counter == 0:
                count += 1
        else:
            if s[st_inx] in checker_map:
                checker_map[s[st_inx]] += 1
                counter +=1
                if checker_map[s[st_inx]] == 0:
                    counter -= 1
            st_inx += 1
            if s[en_inx] in checker_map:
                checker_map[s[en_inx]] -= 1
                if checker_map[s[en_inx]] == 0:
                    counter -= 1
            if counter == 0:
                count += 1
        en_inx += 1
    return count

print(find_count_of_sub_strings_of_anagrams_2(a, sub))