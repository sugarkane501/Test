# Test

1.optimize the time complexity -- check if it exists the redundant compute in algorithm

2.exhaustion search :

   how to do it

      backtrace
      dynamic process
      DFS/BFS
   how to do it with smart

      double pointer
      fast-low pointer
      binary search
      slide window
      preSum array
      diff array
      greedy(贪心)

3.General binary thinking method:

      If it can get all results by traversing the tree one time.()
      
      If it can define a recursion(递归) function then resolve sub-problem(子问题) to get the last result(分治)
      
      Whatever use which mode, you should know what node should do and when node do it.
   
      前序位置的代码只能从函数参数中获取父节点传递来的数据。
      
      中序位置的代码不仅可以获取参数数据，还可以获取到左子树通过函数返回值传递回来的数据。
      
      后序位置的代码最强，不仅可以获取参数数据，还可以同时获取到左右子树通过函数返回值传递回来的数据。
      
      If this problem is related the sub-tree, it is high probability to use postorder.
   
   

4.experience


      Encountering subtree issues, it should consider the function return value firstly.
   
      Divide and conquer thinking!!!!!!!!!!!!!!!!:
      
      In the recursion function, it often returns (left tree result + right tree result + constant such as 1)
   
      动归/DFS/回溯算法都可以看做二叉树问题的扩展，只是它们的关注点不同：
   
      动态规划算法属于分解问题（分治）的思路，它的关注点在整棵「子树」。
      
      回溯算法属于遍历的思路，它的关注点在节点间的「树枝」。
      
      DFS 算法属于遍历的思路，它的关注点在单个「节点」。

// 回溯算法框架

    void backtrack(...) 

    {

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
//0609

    1、算法的本质是穷举，递归是一种重要的穷举手段，递归的正确理解方法是从「树」的角度理解。


    2、编写递归算法，有两种思维模式：一种是通过「遍历」一遍树得到答案，另一种是通过「分解问题」得到答案。

    如果你想用「分解问题」的思维模式来写递归算法，那么这个递归函数一定要有一个清晰的定义，说明这个函数参数的含义是什么，返回什么结果。

    如果你想用「遍历」的思维模式来写递归算法，那么你需要一个无返回值的遍历函数，在遍历的过程中收集结果。

    !!!!!!!!思维步骤：
    
    1、首先，这个问题是否可以抽象成一棵树结构？如果可以，那么就要用递归算法了。

    2、如果要用递归算法，那么就思考「遍历」和「分解问题」这两种思维模式，看看哪种更适合这个问题。

    3、如果用「分解问题」的思维模式，那么一定要写清楚这个递归函数的定义是什么，然后利用这个定义来分解问题，利用子问题的答案推导原问题的答案；如果用「遍历」的思维模式，那么要用一个无返回值的递归函数，单纯起到遍历递归树，收集目标结果的作用。





















