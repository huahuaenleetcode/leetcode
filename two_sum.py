class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            curr = nums[i]
            remain = target - curr;
            if curr in dict:
                return (dict[curr], i)
            dict[remain] = i
        
        
