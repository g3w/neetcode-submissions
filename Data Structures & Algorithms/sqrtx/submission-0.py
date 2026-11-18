class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            mid = (left+right)//2

            root = mid**2

            if root == x:
                return mid
            
            elif root > x:
                right = mid -1
            
            else:
                left = mid +1
        
        return right
        