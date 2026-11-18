class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        def dfs(i):

            if i >= len(days):
                return 0

            if i in memo:
                return memo[i]

            # 1-day pass
            cost1 = costs[0] + dfs(i + 1)

            # 7-day pass
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1

            cost7 = costs[1] + dfs(j)

            # 30-day pass
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1

            cost30 = costs[2] + dfs(j)

            memo[i] = min(cost1, cost7, cost30)

            return memo[i]

        return dfs(0)