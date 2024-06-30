class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstring = ''.join(e for e in s if e.isalnum()).lower()
        revstring=newstring[::-1]
        print(newstring)
        print(revstring)

        if newstring == revstring:
            return True
        else:
            return False
        