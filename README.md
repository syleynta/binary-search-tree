# Binary Search Tree & Sorted Linked List Merge

A Python project demonstrating binary search trees, recursive and iterative insertion, tree traversal, and merging sorted linked lists. Created for a Data Structures course.

## Features

### Binary Search Tree

Builds a binary search tree from 20 user-entered integers.

- Includes recursive and iterative insertion methods.
- Displays an inorder traversal with each node’s level, starting at level 0 for the root.
- Counts leaf nodes, nodes with one child, and nodes with two children.
- Uses a custom `__str__` method to display the tree in a nested, parenthesized format.

The main program uses recursive insertion. The iterative method is available as an alternative.

### Sorted Linked List Merge

Builds two linked lists from user input and merges them into one sorted list.

- Accepts three integers per list.
- Validates input and prompts again when a non-integer is entered.
- Sorts each set of values before building its linked list.
- Merges the lists by comparing node values and updating links between existing nodes.

**Example:**
```text
List 1 (sorted): 1 -> 4 -> 7
List 2 (sorted): 2 -> 3 -> 8

Merged Final List:
1 -> 2 -> 3 -> 4 -> 7 -> 8
```

## How to Run

Requires Python 3. No additional packages are needed.

Run the following command from the folder containing the source file:

```bash
python bst_and_linked_list_merge.py
```

If your system uses `python3`:

```bash
python3 bst_and_linked_list_merge.py
```

### Program Flow

1. Enter 20 integers for the binary search tree, pressing Enter after each value.
2. Review the inorder traversal, node counts, and tree structure.
3. Enter three integers for the first linked list.
4. Enter three integers for the second linked list.
5. Review the sorted lists and merged result.

## Concepts Practiced

- Object-oriented programming and custom node classes
- Binary search trees
- Recursive and iterative algorithms
- Inorder traversal and node depth
- Singly linked lists and node references
- Merging sorted data
- Input validation and exception handling

## Implementation Notes

- Recursive insertion places duplicate values in the right subtree; iterative insertion skips duplicates.
- The tree is not self-balancing, so its shape depends on insertion order.
- Tree input expects valid integers; non-integer input causes an error.
- Linked list input includes validation for non-integer values.
- Merging two sorted lists takes O(n + m) time, where n and m are their lengths. Sorting the user-entered values happens separately before merging.
