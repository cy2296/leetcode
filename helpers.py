from typing import List
from entities.TreeNode import TreeNode
from entities.LinkedList import LinkedList

def list_to_linked_list(l: List[int]):
    if not l:
        return None
    return LinkedList(l[0]) if len(l) == 1 else LinkedList(l[0], list_to_linked_list(l[1:]))


def list_to_binary_tree(l: List[int]):
    q = []
    head = list_to_linked_list(l)
    if not head:
        return None
    root = TreeNode(head.val)
    q.append(root)
    head = head.next

    while head:
        parent = q.pop(0)
        left, right = None, None

        # Take the next two nodes from the linked list
        # Add them as children of the current parent node
        left = TreeNode(head.val)
        q.append(left)
        head = head.next

        if head:
            right = TreeNode(head.val)
            q.append(right)
            head = head.next

        parent.left = left
        parent.right = right

    return root


