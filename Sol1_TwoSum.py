class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # we are given an array of integers nums and an integer target,
        # have to return indices of the two numbers such that they add up to target.
        # I am allowed to return the answer in any order.  
        #       
        # I want to find which two number that add up to the target.
        # For that: I have loop through the list and check each number.
        # A dictionary fits this problem the best, 
        # since I will needs its Key: value structure, to store these numbers in their respective index.  
        # which index the valid nums that together match target are

        # dict for storing the number and which index it belongs to
        seen = {}

        # I want to look through every number in the list, I loop through with a for loop
        for i, num in enumerate(nums):
            # for every number get needed
            needed = target - num
            
            # looking if needed matches nums of needed matches any index in seen.
            if needed in seen:
                # we want to return 
                return [seen[needed], i]

            # of not, I want to store these values in the dict
            seen[num] = i