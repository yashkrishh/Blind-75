# Steps to Tackle the Problem: "Best Time to Buy and Sell Stock"

## 1. Understand the Problem
### Key Questions:
- **What are the inputs and outputs?**  
  - Example: Input is a list of prices, output is the maximum profit.
- **What constraints are given?**  
  - Example: Buy once and sell once, selling must be after buying.
- **What is the goal?**  
  - Example: Maximize profit while adhering to the constraints.

### Tip:
Reframe the problem in plain language.  
For this problem:  
*"Track the smallest price so far and calculate the maximum profit by selling after that."*

---

## 2. Identify Key Patterns
### Single Pass Patterns:
Problems like this often involve tracking a "best so far" value while iterating through the input.

### Key Observations:
- You want to maximize profit, which is `price - min_price`.
- `min_price` must be the smallest price seen before the current day.
- Iterating once while tracking these values is efficient.

---

## 3. Decide on Variables
### Why Use Extra Variables?
To keep track of intermediate results needed for your calculation. In this case:
- `min_price`: Tracks the smallest price so far.
- `max_profit`: Tracks the maximum profit seen so far.
- `potential_profit` (optional): Used to calculate profit for each day.

### Key Questions to Ask:
1. **What do I need to calculate the result?**  
   Example: To calculate the maximum profit, I need both the `min_price` and the profit for the current price.
2. **What do I need to remember as I iterate?**  
   Example: Keep updating `min_price` and `max_profit` at each step.

---

## 4. Optimize Your Approach
### Iterate Once (Linear Scan):
Problems like this often boil down to finding a way to iterate through the input in one pass, keeping track of key values.

### Think Greedy:
- Make the best decision at each step based on the values you’ve tracked so far.
- For this problem, it's about:
  - **Updating `min_price`** when a smaller price is found.
  - **Updating `max_profit`** when a higher profit can be achieved.

---

## 5. Practice Common Patterns
### Problems like these often fall into familiar categories:
1. **Sliding Window**: Track subarrays or ranges.
2. **Greedy Algorithms**: Make the best decision step-by-step.
3. **Dynamic Programming**: Track state across iterations.

### By solving similar problems, you’ll recognize when to use extra variables:
- **Example Problems**:
  - *Kadane’s Algorithm (Maximum Subarray)*: Track the current sum and global maximum.
  - *Trapping Rain Water*: Track left and right maximum heights.

---

## 6. Writing the Solution
### Break It Down:
1. **What is the smallest task I can solve here?**  
   For this problem:
   - Track the smallest price (`min_price`).
   - Calculate the profit (`current price - min_price`).
   - Keep track of the maximum profit (`max_profit`).

### Write Step-by-Step:
1. Initialize variables (`min_price`, `max_profit`).
2. Loop through the prices.
3. Update `min_price` and calculate `max_profit`.

---
