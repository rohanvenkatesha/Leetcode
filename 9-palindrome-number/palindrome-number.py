class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = str(x)[::-1]
        if str(x) == rev:
            return True
        else:
            return False