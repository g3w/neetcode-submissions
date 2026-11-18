class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = sum(arr[:k])
        n = len(arr)

        if window_sum / k >= threshold:
            count += 1

        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]

            if window_sum / k >= threshold:
                count += 1

        return count

