from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list `nums` that add up to `target`.
        Returns their indices as a list.
        """
        # Dictionary to store numbers and their indices
        seen = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in seen:
                # If found, return the indices
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            seen[num] = i

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]  # Input list
    target = 9             # Target sum
    
    solution = Solution()  # Create an instance of the Solution class
    result = solution.twoSum(nums, target)  # Call the method
    
    print("Indices of numbers that add up to target:", result)
