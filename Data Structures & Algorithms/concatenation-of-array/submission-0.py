class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        shallow_copy = nums.copy()
        ans = nums + shallow_copy
        return ans