class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pointer = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_pointer] = nums[i]
                write_pointer += 1
        
        return write_pointer
