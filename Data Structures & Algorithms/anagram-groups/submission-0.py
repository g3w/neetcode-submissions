from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for each in strs:
            sorted_each = ''.join(sorted(each))
            store[sorted_each].append(each)

        return list(store.values())
