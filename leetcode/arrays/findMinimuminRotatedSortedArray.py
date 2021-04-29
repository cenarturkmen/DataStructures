#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#o(n) time comlexity o(1) space comlexity
def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return nums[i+1]
    else:
        return nums[0]
#o(logn)
def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        
        while start<end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
            
        return nums[start]