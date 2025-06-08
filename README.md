# Test

1.optimize the time complexity -- check if it exists the redundant compute in algorithm

2.exhaustion search :

1) how to do it
   backtrace
   dynamic process
   DFS/BFS
2) how to do it with smart
   double pointer
   fast-low pointer
   binary search
   slide window
   preSum array
   diff array
   greedy(贪心) test

3.General binary thinking method:

1) If it can get all results by traversing the tree one time.()
2) If it can define a recursion(递归) function then resolve sub-problem(子问题) to get the last result(分治)
3) Whatever use which mode, you should know what node should do and when node do it.

   前序位置的代码只能从函数参数中获取父节点传递来的数据。
   中序位置的代码不仅可以获取参数数据，还可以获取到左子树通过函数返回值传递回来的数据。
   后序位置的代码最强，不仅可以获取参数数据，还可以同时获取到左右子树通过函数返回值传递回来的数据。
   If this problem is related the sub-tree, it is high probability to use postorder.
   Encountering subtree issues, it should consider the function return value firstly.

   Divide and conquer thinking!!!!!!!!!!!!!!!!:
   In the recursion function, it often returns (left tree result + right tree result + constant such as 1)

   动归/DFS/回溯算法都可以看做二叉树问题的扩展，只是它们的关注点不同：

   动态规划算法属于分解问题（分治）的思路，它的关注点在整棵「子树」。
   回溯算法属于遍历的思路，它的关注点在节点间的「树枝」。
   DFS 算法属于遍历的思路，它的关注点在单个「节点」。

// 回溯算法框架
void backtrack(...) {
// base case
if (...) return;

    for (int i = 0; i < ...; i++) {
        // 做选择
        ...

        // 进入下一层决策树
        backtrack(...);

        // 撤销刚才做的选择
        ...
    }

}