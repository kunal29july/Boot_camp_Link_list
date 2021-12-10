'''
83. Remove Duplicates from Sorted List
Easy

3727

172

Add to List

Share
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # -2 --> -2 --> 1->2->2-->4->4->-5
        
        dummy=ListNode(-10000)
        prev=dummy
        prev.next=head
        curr=head
        
        while(curr):
            if prev.val==curr.val:
                prev.next=curr.next
                curr=curr.next
                
            else:
                prev=prev.next
                curr=curr.next
                
                
                
        return head
        
