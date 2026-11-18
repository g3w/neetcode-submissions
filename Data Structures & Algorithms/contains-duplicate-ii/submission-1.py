class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = set()
        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            else:
                duplicate.add(nums[i])
            
            if len(duplicate) > k:
                duplicate.remove(nums[i-k])
        
        return False