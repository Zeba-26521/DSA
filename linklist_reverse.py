# 1: Reverse
# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#main code 
def reverseList(head):

    temp = head
    prev = None

    while temp:

        next_node = temp.next   # store next node
        temp.next = prev        # reverse pointer

        prev = temp             # move prev forward
        temp = next_node        # move temp forward

    return prev


#2: Reverse first K nodes

def reverseFirstK(head, k):

    temp = head
    prev = None
    count = 0            # to track how many nodes reversed

    if head is None or k <= 1:
        return head

    while temp and count < k:   # stop after k nodes

        next_node = temp.next
        temp.next = prev

        prev = temp
        temp = next_node

        count += 1      # increase counter

    head.next = temp    #connect reversed part to remaining list

    return prev


#3: Reverse K Group

def reverseKGroup(self, head, k):

    if head is None or k <= 1:
        return head

    temp = head
    prev = None
    count = 0

    while temp and count < k:

        next_node = temp.next
        temp.next = prev

        prev = temp
        temp = next_node

        count += 1

    head.next = self.reverseKGroup(temp, k)

    return prev
