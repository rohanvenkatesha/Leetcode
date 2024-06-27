# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l=list()
        k=list()
        i=l1
        j=l2
        a=1
        while i is not None:
            l.append(i.val)
            i=i.next
        while j is not None:
            k.append(j.val)
            j=j.next
        l=l[::-1]
        k=k[::-1]
        num1 = int(''.join(map(str,l)))
        num2 = int(''.join(map(str,k)))
        num3=num1+num2
        output = list(str(num3))[::-1]
        output = [eval(i) for i in output]
        print(output)
        head = ListNode(output[0])
        tail=head
        while a <len(output):
            tail.next=ListNode(output[a])
            tail=tail.next
            a=a+1
        return head
        