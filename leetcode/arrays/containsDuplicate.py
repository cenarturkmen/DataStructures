# https://leetcode.com/problems/contains-duplicate/
#o(n) time complexity o(n) space complexity
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            return True
    return False
        