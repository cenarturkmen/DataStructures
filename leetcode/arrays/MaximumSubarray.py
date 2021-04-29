#https://leetcode.com/problems/maximum-subarray/
# o(n) time complexity 
def MaximumSubarray(nums):
    curSum = nums[0]
    maxSum = nums[0]
    for num in nums:
        curSum = max(num, num+curSum)
        maxSum = max(curSum, maxSum)

    return maxSum


