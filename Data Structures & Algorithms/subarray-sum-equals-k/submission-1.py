class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        prefix_sum =0
        result = 0
        count[0] = 1

        for num in nums:
            prefix_sum += num

            result += count[prefix_sum-k]

            count[prefix_sum] += 1
        
        return result