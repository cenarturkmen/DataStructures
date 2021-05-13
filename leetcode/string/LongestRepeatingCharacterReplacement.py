#https://leetcode.com/problems/longest-repeating-character-replacement/
def characterReplacement(s: str, k: int):
    dic = defaultdict(int)
    maxFreq = 0
    maxLength = 0
    start = 0
    end = 0
    while end<len(s):
        dic[s[end]] += 1    
        maxFreq = max(maxFreq, dic[s[end]])    
        if ((end-start + 1) - maxFreq) > k:
            dic[s[start]] -= 1
            start +=1
        else:
            maxLength = max(maxLength, end-start+1)
        end = end + 1 
    return maxLength
    
print(characterReplacement("ABABA", k= 2))