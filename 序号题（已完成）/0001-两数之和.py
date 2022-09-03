"""
题目：
    给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

最后一次逝一逝
"""



# 枚举法
"""
枚举法解题思想：
用枚举的方法把list中对应的index和value传入字典中，
判断target-value的值是否也在dict中，
存在则返回dict中的索引记录和当前索引
"""
class Solution01(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]  # 存在则返回dict中的索引记录和当前索引


# 两层循环暴力破解（不推荐）
class Solution02(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):  # i是下标
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j


test01 = Solution01()
print(test01.twoSum([5, 9, 8, 7, 6], 13))


test02 = Solution02()
print(test02.twoSum([5, 9, 8, 7, 6], 13))