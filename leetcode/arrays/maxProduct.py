# https://leetcode.com/problems/maximum-product-subarray/
#  o(n*2) time complexity

def maxProduct(nums):
    prevMin = nums[0]
    prevMax = nums[0]
    curMax = nums[0]
    curMin = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        curMin = min(min(prevMin*nums[i], prevMax*nums[i]), nums[i])
        curMax = max(max(prevMin*nums[i], prevMax * nums[i]), nums[i])
        prevMin = curMin
        prevMax = curMax
        ans = max(prevMax, ans)
    return ans
