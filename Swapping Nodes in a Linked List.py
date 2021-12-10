'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr=head
        p=k
        while(curr):
            count=count+1
            curr=curr.next
        #print(count)
        n1=head
        while(k-1):
            n1=n1.next
            k=k-1
        #print(n1.val)
        n2=head
        jump=count-p
        print(jump)
        while(jump):
            n2=n2.next
            jump=jump-1
        #print(n2.val)
        n1.val,n2.val=n2.val,n1.val
        return head
        
            
