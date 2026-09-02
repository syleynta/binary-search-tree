# ==========================================
# PART I - Binary Search Tree Program
# Supports both recursive and iterative insertion
# Prints inorder traversal with level
# Counts:
#   leaves
#   one-child nodes
#   two-child nodes
# Includes a custom __str__ method for printing tree structure
# ==========================================

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---- Recursive insertion ----
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)

        if value < node.data:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    # ---- Iterative insertion (alternate approach) ----
    def insert_iterative(self, value):
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value == current.data:
                return  # skip duplicates
            if value < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # ---- Inorder traversal with level ----
    def inorder(self):
        self._inorder(self.root, 0)

    def _inorder(self, node, level):
        if node:
            self._inorder(node.left, level + 1)
            print(node.data, "(Level", level, ")")
            self._inorder(node.right, level + 1)

    # ---- Count leaves ----
    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)

    # ---- Count one-child nodes ----
    def count_one_child(self):
        return self._count_one_child(self.root)

    def _count_one_child(self, node):
        if node is None:
            return 0

        count = 0
        if (node.left is None and node.right is not None) or \
           (node.left is not None and node.right is None):
            count = 1

        return count + self._count_one_child(node.left) + self._count_one_child(node.right)

    # ---- Count two-child nodes ----
    def count_two_children(self):
        return self._count_two_children(self.root)

    def _count_two_children(self, node):
        if node is None:
            return 0

        count = 0
        if node.left is not None and node.right is not None:
            count = 1

        return count + self._count_two_children(node.left) + self._count_two_children(node.right)

    # ---- Custom string representation ----
    def __str__(self):
        return self._str_recursive(self.root)

    def _str_recursive(self, node):
        if node is None:
            return ""
        return f"({self._str_recursive(node.left)} {node.data} {self._str_recursive(node.right)})"


# ==========================================
# PART II - Merge Two Sorted Linked Lists
# Builds each list from user input
# ==========================================

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def merge_lists(head1, head2):
    dummy = ListNode()
    tail = dummy

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 else head2
    return dummy.next


def build_list_from_user(list_label, size=3):
    print(f"\nEnter {size} integers for {list_label}:")
    values = []
    for i in range(size):
        while True:
            try:
                val = int(input(f"  Value {i + 1}: "))
                values.append(val)
                break
            except ValueError:
                print("  Please enter a valid integer.")

    values.sort()

    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def print_list(head):
    if not head:
        print("Empty List")
        return
    while head:
        print(head.data, end=" -> " if head.next else "\n")
        head = head.next


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():
    # --- Part I: Binary Search Tree ---
    print("=== Part I: Binary Search Tree ===")
    tree = BST()

    print("Enter 20 integers:")
    for i in range(20):
        num = int(input())
        tree.insert(num)

    print("\nInorder Traversal:")
    tree.inorder()

    print("\nThere are", tree.count_leaves(), "leaf nodes")
    print("There are", tree.count_one_child(), "nodes with one child")
    print("There are", tree.count_two_children(), "nodes with two children")

    print("\nTree structure:")
    print(tree)

    # --- Part II: Merge Two Sorted Linked Lists ---
    print("\n=== Part II: Merging Two Sorted Linked Lists ===")
    list1 = build_list_from_user("List 1")
    list2 = build_list_from_user("List 2")

    print("\nList 1 (sorted):", end=" ")
    print_list(list1)
    print("List 2 (sorted):", end=" ")
    print_list(list2)

    merged_head = merge_lists(list1, list2)

    print("\nMerged Final List:")
    print_list(merged_head)


if __name__ == "__main__":
    main()