from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_hash = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in count_hash:
                count_hash[nums[i]] +=1
            else:
                return True
        print(count_hash)
        return False
    

        