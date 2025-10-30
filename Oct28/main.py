# # - Vowel Extractor  
# #   Write a program to extract only the vowels from a given word and store them in a list.  
# #   Print the list at the end.

# # ```python
# # Input: word = "education"
# # Output: ['e', 'u', 'a', 'i', 'o']
# # ```
# def word(n):



# - Find Word with Maximum Vowels
#   Given a list of words, find which word has the highest number of vowels and print that word.

# ```python
# Input: words = ["cat", "eagle", "umbrella", "sky"]
# Output: umbrella
# ```

# - Given an array of integers, count how many numbers are even and how many are odd.

# ```python
# Example Input: [1, 2, 3, 4, 5, 6, 7]
# Example Output: { even: 3, odd: 4 }
# ```

# - Given an array of integers and a target element, find the indices of its first and last occurrence.
#   (Bonus point: Try to return the output in a dictionary format)

# ```python
# Example: numbers = [5, 2, 3, 5, 7, 5, 8] key= 5
# Example Output: { firstIndex: 0, lastIndex: 5 }
# ```

# - Combine Two Lists Alternately
#   Write a Python program to combine two lists by picking elements alternately.
#   (Assume both lists are of the same length.)

# ```python
# Input:
# list1 = [10, 20, 30]
# list2 = [1, 2, 3]
# Output: [10, 1, 20, 2, 30, 3]

# ```


class RestarantOrder:
    def __init__(self,order_id,rest_id,bill_amount):
        # order_id -> list
        # rest_id -> list
        # bill_amount -> list
        self.order_id = order_id
        self.rest_id = rest_id
        self.bill_amount = bill_amount
    
    def get_order_id(self): 
        pass
