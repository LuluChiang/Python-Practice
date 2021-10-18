from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class SingleLinklist:
    def __init__(self):
        self.head = ListNode(None)
        
    def addNode(self, data):
        cur = self.head
        if cur.val == None:
            self.head = ListNode(data)
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = ListNode(data)
    
    def addNodes(self, *args):
        for arg in args:
            self.addNode(arg)
    
    def Printlist(self):
        cur = self.head
        list_val = [cur.val]
        list_next = [cur.next]
        while cur.next != None:
            cur = cur.next
            list_val.append(cur.val)
            list_next.append(cur.next)
        print(list_val)  
        # print(list_next)    



class Solution:
# 237. Delete Node in a Linked List
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.
    def deleteNode(self, node:ListNode):
        node.val = node.next.val
        node.next = node.next.next

# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = head
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            head = head.next
         
        return output

# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmplist = ListNode()
        
        return