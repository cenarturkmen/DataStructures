
# https://leetcode.com/problems/two-sum/

# o(n^2) time complexity, o(1) space complexity
def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)-1):
            if nums[i] + nums[j] == target:
                return i,j
# o(n) time, o(n) space      hashmap solution
def two_sum(nums, target):
    dic = {}
    for i, n in enumerate(nums):
        desired = target - n
        if desired in dic:
            return [dic[desired], i]
        else:
            dic[n] = i