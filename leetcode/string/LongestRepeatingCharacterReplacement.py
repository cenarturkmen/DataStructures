# https://leetcode.com/problems/longest-repeating-character-replacement/
def characterReplacement(s: str, k: int):
    dic = defaultdict(int)
    maxFreq = 0
    maxLength = 0
    start = 0
    end = 0
    while end < len(s):
        dic[s[end]] += 1
        maxFreq = max(maxFreq, dic[s[end]])
        if ((end-start + 1) - maxFreq) > k:
            dic[s[start]] -= 1
            start += 1
        else:
            maxLength = max(maxLength, end-start+1)
        end = end + 1
    return maxLength


print(characterReplacement("ABABA", k=2))


# i think its better
def characterReplacement2(self, s: str, k: int) -> int:
    left = 0
    right = 0
    countTable = {}
    result = 0

    while right < len(s):
        countTable[s[right]] = 1 + countTable.get(s[right], 0)
        if(right - left + 1) - max(countTable.values()) <= k:
            result = max((right - left + 1), result)
            right += 1
        else:
            countTable[s[left]] -= 1
            left += 1

    return result
