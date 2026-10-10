"""
📚 Iterative approach for checking whether two binary trees are identical.

A stack stores pairs of corresponding nodes for comparison. Each pair is
checked for matching structure and values before its children are added.
This avoids recursive function calls. 🔍
"""

from typing import List, Optional, Tuple
from treenode import TreeNode


class Iteration:
    """🔄 Compares two binary trees using an explicit stack."""

    def check(
        self,
        first_tree: Optional[TreeNode],
        second_tree: Optional[TreeNode],
    ) -> bool:
        # 📦 Store corresponding node pairs, starting with both roots.
        node_stack: List[
            Tuple[Optional[TreeNode], Optional[TreeNode]]
        ] = [(first_tree, second_tree)]

        while node_stack:
            # 🔍 Retrieve the next pair of nodes to compare.
            first_node, second_node = node_stack.pop()

            # 🌱 Two empty nodes represent identical subtrees.
            if not first_node and not second_node:
                continue

            # ❌ If only one node is empty, the structures differ.
            if not first_node or not second_node:
                return False

            # 🔢 Corresponding nodes must have matching values.
            if first_node.val != second_node.val:
                return False

            # ◀️ Queue the corresponding left children for comparison.
            node_stack.append((first_node.left, second_node.left))

            # ▶️ Queue the corresponding right children for comparison.
            node_stack.append((first_node.right, second_node.right))

        # ✅ Every corresponding node pair matched.
        return True
