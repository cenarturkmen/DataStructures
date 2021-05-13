def isAnagram(self, s: str, t: str) -> bool:
    dic = {}
    for i in s:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
        
    for j in t:
        if j in dic:
            dic[j] = dic[j] - 1
        else:
            return False
            
    for key in dic:
        if dic[key] > 0:
            return False
            
    return True