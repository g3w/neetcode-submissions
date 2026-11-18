class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, zeros_left, ones_left):

            if i == len(strs):
                return 0

            if (i, zeros_left, ones_left) in memo:
                return memo[(i, zeros_left, ones_left)]

            zeros = strs[i].count('0')
            ones = strs[i].count('1')

            # Option 1: Skip current string
            res = dfs(i + 1, zeros_left, ones_left)

            # Option 2: Take current string (if possible)
            if zeros <= zeros_left and ones <= ones_left:
                res = max(
                    res,
                    1 + dfs(
                        i + 1,
                        zeros_left - zeros,
                        ones_left - ones
                    )
                )

            memo[(i, zeros_left, ones_left)] = res
            return res

        return dfs(0, m, n)