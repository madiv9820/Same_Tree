# [🌳 Same Tree — When Two Trees Tell the Same Story](https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150)

### 📖 A Little Story

Imagine two family trees standing side by side. 👨‍👩‍👧‍👦🌳
At first glance, they might look similar—but to call them **identical**, every family member must occupy the same position **and** have the same identity.

If one family member is missing, moved to another branch, or has a different name, the trees are no longer the same. 🔍

That is exactly what this problem asks us to determine!

### 🎯 Question Explanation

Given the roots of two binary trees, **`p`** and **`q`**, determine whether they represent the **same binary tree**.

Two trees are considered the same when:

- 🌱 Their **structure is identical**.
- 🔢 Corresponding nodes contain the **same value**.
- 🔄 Every left subtree matches its corresponding left subtree.
- 🔄 Every right subtree matches its corresponding right subtree.

In other words:

> **Same structure + Same corresponding values = Same Tree ✅**

If either the structure or any node value differs, the answer is **`false`**. ❌

#### 🧩 Examples

- **🟢 Example 1 — Perfect Match**

    ![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

    ```
    p = [1,2,3]
    q = [1,2,3]

         1              1
        / \            / \
       2   3          2   3
    ```

    Both trees have the **same structure** and the **same values** at every corresponding position.

    **Output: `true` ✅**

- **🟠 Example 2 — Shape Doesn't Match**

    ![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

    ```
    p = [1,2]
    q = [1,null,2]

        1       1
        /        \
       2          2
    ```

    The nodes contain the same values, but they are arranged differently.

    **`2`** is the **left child** in **`p`** but the **right child** in **`q`**.

    **Output: `false` ❌**

- **🔴 Example 3 — Values Don't Match**

    ![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

    ```
    p = [1,2,1]
    q = [1,1,2]

         1              1
        / \            / \
       2   1          1   2
    ```

    The structure is identical, but the corresponding nodes have different values.

    **Output: `false` ❌**

#### 📌 Constraints

- 🌳 Number of nodes in each tree: **0 to 100**
- 🔢 **`-10⁴ <= Node.val <= 10⁴`**
- 🧩 Both **structure and node values** must match exactly.

---

### 🌳 Approaches

Two binary trees are identical when they have the same structure and every pair of corresponding nodes contains the same value. Both approaches compare corresponding nodes and stop as soon as a structural or value mismatch is discovered. **Recursion** uses the call stack to explore both subtrees naturally, while **Iteration** uses an explicit stack to manage pending node pairs. Both achieve linear time complexity in the worst case.

- #### 1. 🔄 Recursion

    **Intuition:** A binary tree is identical to another if their roots match and their left and right subtrees are also identical. Recursion breaks this problem into smaller comparisons until it reaches empty nodes.

    **Steps:**
    1. 🌱 If both nodes are `None`, return `True`.
    2. ❌ If only one node is `None`, return `False`.
    3. 🔢 If their values differ, return `False`.
    4. 🔄 Recursively compare the left and right subtrees.
    5. ✅ Return `True` only if both comparisons succeed.

    **Pseudocode:**
    ```text
    CHECK(first, second):
        IF both are NULL:
            RETURN TRUE

        IF either is NULL:
            RETURN FALSE

        IF first.value != second.value:
            RETURN FALSE

        RETURN CHECK(first.left, second.left)
        AND CHECK(first.right, second.right)
    ```

    **Complexity:**
    - **Time:** \(O(n)\) — Each corresponding node is visited at most once.
    - **Auxiliary Space:** \(O(h)\) — The recursion stack depends on the maximum tree height \(h\); worst case \(O(n)\).

- #### 2. 📚 Iteration

    **Intuition:** Instead of relying on recursive calls, maintain a stack of corresponding node pairs. Process each pair, reject mismatches, and add their children for subsequent comparison.

    **Steps:**
    1. 📦 Initialize a stack with the two root nodes.
    2. 🔍 Pop a pair of nodes.
    3. 🌱 If both are `None`, continue.
    4. ❌ If only one is `None` or their values differ, return `False`.
    5. ◀️▶️ Push the corresponding left and right child pairs.
    6. ✅ If the stack becomes empty without a mismatch, return `True`.

    **Pseudocode:**
    ```text
    CHECK(first, second):
        stack = [(first, second)]

        WHILE stack is not empty:
            first, second = POP(stack)

            IF both are NULL:
                CONTINUE

            IF either is NULL:
                RETURN FALSE

            IF first.value != second.value:
                RETURN FALSE

            PUSH (first.left, second.left)
            PUSH (first.right, second.right)

        RETURN TRUE
    ```

    **Complexity:**
    - **Time:** \(O(n)\) — Each corresponding node is processed at most once.
    - **Auxiliary Space:** \(O(n)\) — The explicit stack can hold a linear number of node pairs in the worst case.

#### ⚖️ Comparison

| Feature | 🔄 Recursion | 📚 Iteration |
|---|---|---|
| Traversal mechanism | Call stack | Explicit stack |
| Worst-case time | \(O(n)\) | \(O(n)\) |
| Worst-case space | \(O(n)\) | \(O(n)\) |
| Readability | Concise and natural | More control over traversal |
| Deep trees | Recursion-depth risk | Avoids recursion-depth limits |

**Legend:** \(n\) is the number of nodes in the larger tree, and \(h\) is the maximum tree height.

#### 🏆 Verdict

Both approaches are optimal in worst-case time complexity. **Recursion** is the more natural and concise solution, while **Iteration** is a useful alternative when avoiding recursion-depth limitations matters. 🌳

---
