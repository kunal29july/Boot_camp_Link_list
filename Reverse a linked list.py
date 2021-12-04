# https://leetcode.com/problems/reverse-linked-list/
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        curr=head
        pointer=head
        while(curr):
            stack.append(curr.val)
            curr=curr.next
        #print(stack)
        while(pointer):
            pointer.val=stack.pop()
            pointer=pointer.next
        return head
   ###############################
  
  class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr=head
        prev=None
        while(curr):
            save=curr.next
            curr.next=prev
            prev=curr
            curr=save
        curr=prev
        return(curr)
        
