class Solution():
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i


s1 = Solution()

n = int(input())
inp = list(map(int, input().split()))

print(s1.twoSum(inp, 10))