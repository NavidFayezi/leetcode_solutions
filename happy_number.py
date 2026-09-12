class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        num = n
        seen = set()
        seen.add(num)
        rc = True
        while num > 0:
            
            sum += (num % 10)**2
            num = num // 10
            if num == 0 and sum != 1:
                num = sum
                sum = 0
                if num in seen:
                    rc = False
                    break
                else:
                    seen.add(num)
                    
            elif num == 0 and sum == 1:
                break
        
        return rc
