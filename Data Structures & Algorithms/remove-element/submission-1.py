class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_target = [index for index, value in enumerate(nums) if value == val]
        for index in sorted(index_target, reverse=True):
            nums.pop(index)
        return len(nums)
