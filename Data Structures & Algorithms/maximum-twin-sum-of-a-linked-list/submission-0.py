# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = float('-inf')
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        
        for i in range(len(arr)):
            twin = len(arr)- 1-i
            twin_sum = arr[i] + arr[twin]
            maxSum = max(maxSum, twin_sum)
        
        return maxSum if maxSum != float('-inf') else 0