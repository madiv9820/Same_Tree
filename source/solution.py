"""
🌳 Entry point for checking whether two binary trees are identical.

The solution compares two trees based on two things:
1. 🧩 Their structure must be identical.
2. 🔢 Corresponding nodes must contain the same values.

The actual comparison logic is implemented by the selected approach.
"""

from typing import Optional
from treenode import TreeNode
from .approches import Recursion, Iteration

class Solution:
    """🎯 Provides the Same Tree solution interface."""

    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> bool:
        """🔍 Return True when both binary trees are identical."""

        # 🚧 Approach implementation will be connected here.
        recursion: Recursion = Recursion()
        iteration: Iteration = Iteration()
        
        return iteration.check(p, q)
