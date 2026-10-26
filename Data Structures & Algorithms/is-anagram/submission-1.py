from collections import Counter , defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        map_s = Counter(s)
        map_t = Counter(t)
        return map_s == map_t

        