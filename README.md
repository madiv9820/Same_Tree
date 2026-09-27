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