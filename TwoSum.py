class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # hash
        '''map = {}
        for i, value in enumerate(nums):
            if target - value in map:
                return map[target-value], i
            else:
                map[value] = i'''

        # sort
        nums = [3, 2, 3]
        target = 6
        nums_sorted = sorted(nums)
        # print nums_sorted
        left = 0
        right = len(nums) - 1

        while True:
            if nums_sorted[left] + nums_sorted[right] == target:
                post1 = nums.index(nums_sorted[left])
                post2 = nums.index(nums_sorted[right])
                if post1 == post2:
                    post2 = nums[
                        post1 + 1:].index(nums_sorted[right]) + post1 + 1
                    print post1, post2
                return min(post1, post2), max(post1, post2)
            elif nums_sorted[left] + nums_sorted[right] > target:
                right = right - 1
            elif nums_sorted[left] + nums_sorted[right] < target:
                left = left + 1
