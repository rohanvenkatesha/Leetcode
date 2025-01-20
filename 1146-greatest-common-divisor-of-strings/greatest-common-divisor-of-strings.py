class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        new=str1+str2
        rev=str2+str1

        if new != rev:
            return ""
        if len(str1)==len(str2):
            return str2
        if len(str1)>len(str2):
            return self.gcdOfStrings(str1[len(str2):],str2)
        return self.gcdOfStrings(str2[len(str1):],str1)