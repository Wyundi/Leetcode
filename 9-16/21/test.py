# Definition for singly-linked list.

l1 = [1,2,4]
l2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 == None:
        return l2
    
    if l2 == None:
        return l1
    
    List_head = ListNode(val = None, next = l1)
    l1 = List_head

    while l1.next != None and l2.next != None:
        if l1.next.val > l2.val:
            temp = l2
            temp.next = l1.next
            l1.next = temp
            l1 = l1.next
            l2 = l2.next
        else:
            l1 = l1.next

    

    return List_head.next

List = mergeTwoLists(l1, l2)
while List != None:
    print(List.val)
    List = List.next
                