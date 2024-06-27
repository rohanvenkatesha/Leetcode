class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        output=0
        flag = 0
        i=1
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        while(i<=len(s)-1):
            if roman[s[i-1]]<roman[s[i]]:
                output=output+(roman[s[i]]-roman[s[i-1]])
                i=i+2
                flag=0
                print("aa",output)
                print(i)
            else:
                output=output+roman[s[i-1]]
                i=i+1
                flag=1
                print("bb",output)
                print("q",i)
        if flag == 1 or i == len(s):
            output = output + roman[s[-1]]
        return output