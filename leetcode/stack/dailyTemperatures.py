# brute force o(n^2)

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        days = [0] * len(temp)
        x = temp[1] - temp[0]
        
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                if temp[i] < temp[j] and days[i] == 0:
                    days[i] = j - i
        return days

# with stack o(n)

class Solution:
    def dailyTemperatures(self, temp):
        days = [0] * len(temp)
        stack = [] # pair [temp, index]
        
        for i, t in enumerate(temp):
            while stack and t> stack[-1][0]:
                stackTemperature, stackIndex = stack.pop();
                days[stackIndex] = i - stackIndex
            stack.append([t, i])
