class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head=list3=ListNode()

        while list1 and list2:
            if list1.val<=list2.val:
                list3.next=list1
                list1=list1.next
            else:
                list3.next=list2
                list2=list2.next
            list3=list3.next
        if list1:
            list3.next=list1
            list1=list1.next
        if list2:
            list3.next=list2
            list2=list2.next
        
        return head.next