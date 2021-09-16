nums = [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

for i in range(len(nums)):
    nums[i] = ListNode(nums[i])
    if i == 0:
        continue
    else:
        nums[i-1].next = nums[i]

for i in range(len(nums)):
    print(nums[i].val)
    
print('\n')

deleteNode(nums[2])

for i in range(len(nums)):
    print(nums[i].val)