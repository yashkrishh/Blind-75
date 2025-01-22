class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the index of each number
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in seen:
                return [seen[complement], i]
            # Store the current number's index in the dictionary
            seen[num] = i
