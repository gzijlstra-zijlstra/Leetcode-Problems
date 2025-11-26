class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # problem statement:
        # Given two strings s and t, return true if t is an anagram of s
        # and false otherwise.

        # We are given two string (s and t), we have to return true if t is an anagram of s, and false otherwise.
        # order does not matter
        # Example: s = "anagram", t = "nagaram" -> true
        # I will have to check if the 2 words are anagrams with: do they contain the same letters
        
        # if the strings have different lengths, they can not be anagrams
        # that is why I first will check the amount of letters in both strings
    
        # Defining my function
        def isAnagram(s, t):
            # using len() to see if length of both strings is the same
            if len(s) != len(t):
                return False

            
        # dictionary for both strings, to count letters
        # will store letter as key, and count as value
        CountS, CountT = {}, {}

        # counting letters in s
        for ch in s:
            # if letter already in dict, add 1 to count, else set count to 1
            CountS[ch] = CountS.get(ch, 0) + 1

        # counting letters in t
        for ch in t:
            # Counting letters in t and storing in dict
            CountT[ch] = CountT.get(ch, 0) + 1

        # comparing both dicts, if they are the same, return true
        return CountS == CountT
    