
# o(n* n^1/2)
import queue


class Solution:
    def numSquares(self, n: int) -> int:

        cache = [n] * (n + 1)
        cache[0] = 0

        for i in range(1, n + 1):
            for s in range(1, i + 1):
                square = s * s
                if i - square < 0:
                    break
                if 1 + cache[i - square] < cache[i]:
                    cache[i] = 1 + cache[i - square]

        return cache[n]


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = []
        for i in range(1, int(n**0.5)+1):
            square_nums.append(i*i)
       
        level = 0
        queue = {n}
        
        while queue:
            level += 1
            # use set to avoid duplicate possibilities
            next_queue = set()
            
            for remainder in queue:
                for square_num in square_nums:
                    # check if the remainding number in queue is perfect square
                    # if so return the level
                    if remainder == square_num:
                        return level
                    # check if the remainding number in queue is square_num meaning if it has become negative or it can't be subtracted anymore
                    # break the loop
                    elif remainder < square_num:
                        break
                    # else add the next number to queue by calculating remainder-prefect_square number
                    else:
                        next_queue.add(remainder-square_num)
                        
            queue = next_queue
            
        return level


