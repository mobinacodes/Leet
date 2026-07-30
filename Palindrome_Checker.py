# Finds a Palindrome returns true if a passed number is one. 
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        my_list = list(str(x))

        if my_list == my_list[::-1]:
            return True
        else:
            return False
          
          
