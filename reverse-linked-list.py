class Solution(object):
    def reverseList(self, head):
        ret = None
        while head:
            temp = head.next
            head.next = ret
            ret = head
            head = temp

        return ret



            