class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max=candies[0]
        output=list()
        for i in range(len(candies)):
            if candies[i] > max:
                max=candies[i]

        for j in range(len(candies)):
            if (candies[j]+extraCandies)>=max:
                output.append(True)
            else:
                output.append(False)
        return output

