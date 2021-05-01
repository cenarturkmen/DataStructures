#https://leetcode.com/problems/3sum/
# o(n^2) time complexity
def threeSum(nums):
    nums.sort()
    output= []
    for i in range(len(nums)-2):
        print(i)
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while l<r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l = l + 1
            elif s > 0:
                r = r - 1
            else:
                if i!=l and i!=r and l!=r:
                    output.append([nums[i], nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l<r and nums[r] == nums[r-1]:
                        r = r - 1 
                l = l + 1
                r = r - 1
    return output

