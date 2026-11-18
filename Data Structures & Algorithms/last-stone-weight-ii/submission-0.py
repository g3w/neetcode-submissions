class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        dp = {0}

        for stone in stones:
            next_dp = dp.copy()

            for s in dp:
                next_dp.add(s + stone)

            dp = next_dp

        res = float("inf")

        for s in dp:
            res = min(res, abs(total - 2 * s))

        return res
        