#Checking Off
def anagram_solution(s1,s2):
    s2_list = list(s2)
    location_s1 = 0
    still_oke = True
    while location_s1 < len(s1) and still_oke:
        location_s2 = 0
        found = False
        while location_s2 < len(s2_list) and not found:
            if s1[location_s1] == s2[location_s2]:
                found = True
            else:
                location_s2 += 1
        if found:
            s2_list[location_s2] = None
            #print(s2_list)
        else:
            still_oke = False
        location_s1 += 1
    return still_oke
print(anagram_solution("abcd","dbca"))

#Sort and Compare
def anagram_solution2(s1,s2):
    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort()
    s2_list.sort()

    location = 0
    result = True

    while location < len(s1) and result:
        if s1_list[location] == s2_list[location]:
            location += 1
        else:
            result = False
    return result
print(anagram_solution2("heart","earth"))

#Count and Compare 𝑇(𝑛) = 2𝑛 + 26 steps. That is 𝑂(𝑛).
def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        print(pos)
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok
print(anagram_solution4('apple','pleap'))