# given code
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # I am given an integer x, 
        # I have to return true if x is a palindrome, false if not.
        # Palidrome is a number that reads sane backwards.
        # Example: x = 121 -> true
        # Example: x = -121 -> false

        # So i know that negative number have to return false, as they can't be palindromes
        #  I am going to convert the integer to a string, 
        # because strings are easier to reverse and check.

        # int to string
        str_x = str(x) 

        # logic for checking if the string is the same forwards and backwards.
        # my number as a string
        # looked up on slicing operations and using [::-1] to reverse the string/order
        # this condition checks if the original string is the same as the reverse string
        if str_x == str_x[::-1]:
            # return true if they are the same
            return True
        # else I will return false
        else:
            return False
        
        # all the test cases passed on leetcode.