class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # problem statement:
        # Write a function to find the longest common prefix string 
        # amongst an array of strings.
        # If there is no common prefix, return an empty string "".
        
        # I have to write a function to find the longest common prefix string amongst an array of strings.
        # it says that if there is no common prefix, return an empty string "".
        # and if the array is empty it has to return a empty string 
        # I have flower, flow, and flight as a example
        # so fl must be the longest common prefix.

        # returning empty string if input is empty
        if not strs:
            return ""

        # baseline, I will comampare all next string to this one
        first_word = strs[0]

        # for storing the prefix
        prefix = ""

        # looping through all strings in the list
        for i in range(len(first_word)):
            # getting the character at index i
            char = first_word[i]

            # now I have to check the character with all other strings
            for word in strs:
                # if the word is too short or the character does not match
                if i >= len(word) or word[i] != char:
                    return prefix  # return the prefix found so far
                
            # if character matched in all words, add to prefix
            prefix += char
        return prefix  # return the full prefix if all characters matched