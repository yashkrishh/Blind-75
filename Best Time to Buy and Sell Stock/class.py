class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        min_price = float('inf')  # Set to a very large value
        max_profit = 0  # Maximum profit so far
        
        # Loop through prices
        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price
            
            # Calculate potential profit if sold at the current price
            potential_profit = price - min_price
            
            # Update maximum profit
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit
