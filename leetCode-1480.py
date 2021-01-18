class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_elements = 0
        running_sum = []
        for index in range(len(nums)):
            sum_elements += nums[index]
            running_sum.append(sum_elements)
        return running_sum