"""
🌳 Recursive approach for checking whether two binary trees are identical.

The comparison checks both the structure and values of corresponding nodes.
Recursion naturally handles this by comparing each pair of nodes and then
checking their left and right subtrees. 🔍
"""

from typing import Optional
from treenode import TreeNode

class Recursion:
    """🔄 Compares two binary trees recursively."""

    def check(
        self,
        firstTree: Optional[TreeNode],
        secondTree: Optional[TreeNode],
    ) -> bool:
        # 🌱 Two empty nodes represent identical subtrees.
        if not firstTree and not secondTree:
            return True

        # ❌ If only one node is empty, the tree structures differ.
        if not firstTree or not secondTree:
            return False

        # 🔢 Corresponding nodes must contain the same value.
        if firstTree.val != secondTree.val:
            return False

        # 🔍 Recursively compare both left and right subtrees.
        # ✅ Both sides must match for the trees to be identical.
        return (
            self.check(firstTree.left, secondTree.left)
            and self.check(firstTree.right, secondTree.right)
        )
