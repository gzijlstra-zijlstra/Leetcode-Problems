# given code
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # problem statement:
        # Given an integer array nums, return true if any value appears
        # at least twice in the array, and return false if every element is distinct.

        # I am given an integer array (nums), I have to return
        # true if any value appears atleast twice in the array, and have 
        # to return false if every element is distinct.
        # 
        #  nums array example [1,2,3,1] -> true
        # nums array example [1,2,3,4] -> false
        # 
        # I will use a set to store these nums, since sets
        # do not allow duplicate values.
        # using set() since it allows me to have it empty at first
        nums_set = set()

        # looping through all numbers in the nums array
        for num in nums:
            # checking if the number is already in the set
            if num in nums_set:
                # I it finds a duplicate, I will have return be true
                return True  
            else:
                # if not, I will add the number to the set
                nums_set.add(num)  # adding number to the set

        # if no duplicates were found, I will return false
        return False
    
    # all the test cases passed on leetcode.