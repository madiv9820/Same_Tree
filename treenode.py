"""
🌳 TreeNode — Binary Tree Building Block

A binary tree is made up of nodes, where each node stores a value and
can point to at most two children: a left child and a right child.

This TreeNode class provides that basic structure for building binary
trees used by the test suite. 🌱
"""

from typing import Optional

class TreeNode:
    """🧩 Represents a single node in a binary tree."""

    def __init__(
        self,
        val  : int = 0,
        left : Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        # 🔢 Store the value held by the current node.
        self.val: int = val

        # ◀️ Reference the left child, if present.
        self.left: Optional[TreeNode] = left

        # ▶️ Reference the right child, if present.
        self.right: Optional[TreeNode] = right
