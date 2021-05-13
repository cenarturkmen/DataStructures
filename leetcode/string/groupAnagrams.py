#https://leetcode.com/problems/group-anagrams
def groupAnagrams(strs):
    dic = {}
    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str not in dic:
            dic[sorted_str] = [str]
        else:
            dic[sorted_str].append(str)

    output= []
    for value in dic.values:
        output.append(value)
    return output
