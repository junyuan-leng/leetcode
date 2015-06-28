class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return False
        else:
            return not len(set(nums)) == len(nums)