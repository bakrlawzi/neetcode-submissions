from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result :List[List[str]] =  []
        a = defaultdict(dict)
        for word in strs:
            new_word = ''.join(sorted(word))
            if new_word in a:
                a[new_word].append(word)
            else:
                a[new_word] = [word]
        for key,value in a.items():
            result.append(value)
        return result
        


   