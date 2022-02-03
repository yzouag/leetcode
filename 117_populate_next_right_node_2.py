# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left # in this step, both curr and dummy is equal to node.left (only for first iteration)
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next # now the node is point to one of the child, the left most next layer node
        
        return root

if __name__ == "__main__":
    root = [1,2,3,4,5,None,7]
    # Output: [1,#,2,3,#,4,5,7,#]