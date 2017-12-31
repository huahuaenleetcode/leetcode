class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in xrange(len(nums)):
            curr = nums[i]
            remain = target - curr;
            if remain in dict:
                return (dict[remain], i)
            dict[curr] = i
        
