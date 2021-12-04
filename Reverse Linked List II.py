 # https://leetcode.com/problems/reverse-linked-list-ii/
  
  '''iven the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
  iven the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
  '''
  class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        curr=head
        L=left-1
        while(L):
            curr=curr.next
            L=L-1
        pointer1=curr
        demo=pointer1
        
        curr1=head
        R=right-1
        while(R):
            curr1=curr1.next
            R=R-1
        pointer2=curr1
        
        
        stack=[]
        while(pointer1!=pointer2):
            stack.append(pointer1.val)
            pointer1=pointer1.next
        stack.append(pointer1.val)
        #print(stack)
        
        while(len(stack)):
            demo.val=stack.pop()
            demo=demo.next
        return head
