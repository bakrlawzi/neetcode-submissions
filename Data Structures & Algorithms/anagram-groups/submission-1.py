from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        groups = defaultdict(list)
        for words in strs:
            key = ''.join(sorted(words))
            groups[key].append(words)
        return list(groups.values())