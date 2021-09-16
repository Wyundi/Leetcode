head = [1,2,3,4,5]
n = 2

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
H = None
for i in range(len(head)):
    H = ListNode(head[-1-i], H)

def removeNthFromEnd(head, n):
    h_temp = head
    List = []
    i = 0

    while (h_temp != None):
        List.append(h_temp.val)
        h_temp = h_temp.next
        i += 1

    head = None
    for i in range(len(List)):
        if i == (n-1):
            continue
        head = ListNode(List[-1-i], head)

    return head
    
removeNthFromEnd(H, 2)