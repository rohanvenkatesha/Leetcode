class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        appstring=""
        output=[]
        if len(word1)==len(word2):
            appstring=""
        elif len(word1)>len(word2):
            appstring=word1[len(word2):]
            word1=word1[:len(word2)]
        elif len(word2)>len(word1):
            appstring=word2[len(word1):]
            word2=word2[:len(word1)]
        for i,j in zip (word1, word2):
            output.append(i)
            output.append(j)
        output.append(appstring)
        output="".join(output)
        print(output)
        return output

        # print(word1, word2, appstring)
