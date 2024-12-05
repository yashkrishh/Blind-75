class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop the top of the stack or use a dummy value
                if mapping[char] != top_element:  # Check if it matches the expected opening bracket
                    return False
            else:
                stack.append(char)  # If it's an opening bracket, push to the stack
        
        return not stack  # If the stack is empty, the string is valid


def main():
    solution = Solution()
    test_cases = [
        "()",    # True
        "()[]{}",  # True
        "(]",    # False
        "([)]",  # False
        "{[]}",  # True
    ]
    
    for s in test_cases:
        print(f"Input: {s} -> Output: {solution.isValid(s)}")


if __name__ == "__main__":
    main()
