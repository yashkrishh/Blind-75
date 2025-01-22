from typing import List  # Required for type hinting

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]  # Input list
    target = 9  # Target sum
    solution = Solution()  # Create an instance of the Solution class
    result = solution.twoSum(nums, target)  # Call the method
    print(result)  # Print the result
