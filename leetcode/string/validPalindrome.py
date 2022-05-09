    def isPalindrome(s):
        
        lowerCase = s.lower()
        lowerCase = ''.join(e for e in lowerCase if e.isalnum()) 
        left  = 0 
        right = len(lowerCase)-1
        
        while left<right:
            if(lowerCase[left] == lowerCase[right]):
                left += 1
                right -= 1
            else:
                return False
        
        return True