class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = 0
        l=[]
        for i in range(len(nums)):
            num = num + nums[i]
            l.append(num)
            
        return l
