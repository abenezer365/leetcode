class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            count[num] += 1
        max_key = max(count, key=count.get)
        return max_key