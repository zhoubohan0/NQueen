#! https://zhuanlan.zhihu.com/p/478732443
# 浅谈N皇后问题解法

## 问题提出

一般地，${N}$​皇后问题描述如下：

在大小为${N×N}$的棋盘上摆放${N}$个皇后，使其两两之间不能互相攻击，即任意两个皇后都不能处于棋盘的同一行、同一列或同一斜线上，求出满足条件的所有棋局及局面总数。

特殊地，当${N=8}$​​时为著名的以国际象棋棋盘为背景的8皇后问题，易解得符合条件的局面总数为**92**。本实验主要探究${N×N}$​​的棋盘上摆放${N}$​​​个皇后的一般问题。

## 问题分析

${N}$​皇后问题可以维护一个长度为${N}$​的一维数组*q*表示局面情况。${q_i(i=0,…N-1)}$​表示第${i}$​行皇后放置位置所在列数${j(j=0,…N-1)}$​，每个局面可看作由${0}$​到${(N-1)}$​序列组成的一个排列，原问题可以转化成寻找所有不导致行/列/斜线冲突的排列。	

直观的想法是将${N}$​皇后问题看成组合问题，${N×N}$​的棋盘上每个格都有防放置皇后和空格两种情况，总情况数达${2^{N^2}}$​，指数爆炸在时间和空间复杂度上都难以负担。一种改进思路是考虑每列仅允许出现一个皇后，按照行先序顺序放置皇后，第一行有${N}$​种可能，第二行有${N-1}$​种可能…第${N}$​行有1种可能，总情况数缩减为${N!}$​略有改善。为进一步提高算法效率，考虑棋盘上每条斜线上仅允许出现一个皇后，在此联想到**回溯**和**剪枝**的算法。

## 算法描述

引入**N叉树**的数据结构，构建${N}$​​皇后问题的解空间树。排列长度${N}$​​为树的深度，据此判定递归的出口。初始状态将一维数组*q*置空，以行先序从第0行开始递归求解。遍历${i}$​​行每一列${j}$​​，若*q*中已有${j}$​​（即第${j}$​​列已经放置了皇后），则发生剪枝，继续遍历其他列；若*q*中没有${j}$​​，则${q[i]=j}$​​，递归式进入${i+1}$​​行的遍历，直到数组*q*中已经赋满${N}$​​个列号，则进入递归出口进行判定局面的合理性（即每个行/列/斜线最多仅有1个皇后）。若局面合理，将该合理局面保存在二维数组result中，继续回溯探索其他合理局面；若局面不合理，同样回溯探索其他合理局面。以此类推，直到遍历完解空间中所有情况，result中所保存的就是所有合理局面，result的长度就是${N}$​​皇后问题满足条件的所有局面总数。

其中判断局面合理性的方法具体如下：

> 由数组*q*可获得第${i}$​个皇后的位置记为${(x_i, y_i)}$​,$i=0,1,…N-1$​，一个合理的局面需要满足以下条件(${\forall j\ne i,j=0,1,…N-1}$​)：
>
> 1. ${x_j\ne x_i}$​(横行)
> 2. ${y_j\ne y_i}$​​(纵行)
> 3. ${x_j+y_j\ne x_i+y_i}$(主斜线)
> 4. ${y_j-x_j\ne y_i-x_i}$(反斜线)

以4皇后为例，下图为剪枝与回溯思想的示意图：(仅示意，不代表真实求解情况)

<center><img src="https://pic4.zhimg.com/80/v2-074892d362527c5a4db7abf1bb954db6.png"></center>

## 代码实现

### 核心算法代码

> [编译环境]
>
> Windows 系统|PyCharm 编译器|python 3.8.11

传统解决${N}$​皇后问题的算法都是基于递归的回溯算法，但单线程递归程序不易可视化。因此，我分别设计了用于求解${N}$​皇后所有解法数的递归函数`search()`和用于窗口可视化的基于栈实现的**非递归函数** `next()`，并将它们封装在类`NQueen`中。其中，`search()`通过调用`dfs()`方法递归求解所有${N}$​皇后问题的局面；`next()`输入一组${N}$​合理的${N}$​皇后排列返回下一组合理的${N}$​皇后排列，默认开始为空排列，默认最后一组合理的${N}$​皇后排列的下一组排列为空排列。

类`NQueen`代码如下：

```python
class NQueen:
    def __init__(self, N):
        self.N = N  # 方形棋盘边长=皇后数量
        self.result = []  # 所有皇后合理安放局面

    def check(self, cur):
        boolMatrix = np.zeros((self.N, self.N))  # 转化成布尔矩阵
        for i in range(len(cur)):
            boolMatrix[i, cur[i]] = 1
        flag = True  # 合格局面
        # 判列
        flag &= all(np.sum(boolMatrix, axis=0) == np.ones(self.N))
        if not flag:
            return flag
        # 判行
        flag &= all(np.sum(boolMatrix, axis=0) == np.ones(self.N))
        if not flag:
            return flag
        # 判左下右上斜线:i+j∈[0,2*(N1-1)]
        for tmpadd in range(0, 2 * (self.N - 1) + 1):
            tmp = [boolMatrix[i, tmpadd - i] for i in range(self.N) if 0 <= tmpadd - i < self.N]
            flag &= (sum(tmp) <= 1)
            if not flag:
                return flag
        # 判左上右下斜线:i-j∈[-(N1-1),(N1-1)]
        for tmpminus in range(1 - self.N, self.N):
            tmp = [boolMatrix[i, i - tmpminus] for i in range(self.N) if 0 <= i - tmpminus < self.N]
            flag &= (sum(tmp) <= 1)
            if not flag:
                return flag
        return flag  # 运行到这里一定是经过四大检验的合格局面

    def outputresult(self, tofile):
        count = len(self.result)
        print(f'{self.N}×{self.N}棋盘上放置{self.N}个皇后的可行局面总数:{count}')
        if tofile:
            with open(f'../../result/N={self.N}.txt', 'w') as f:
                f.write(f'{count}\n')
                for each in self.result:
                    for i in range(len(each)):
                        f.write(str(each[i] + 1))
                        if i != len(each) - 1:
                            f.write(',')
                        else:
                            f.write('\n')

    def dfs(self, cur):
        # cur:现在搜索阶段，行先序，0~N-1表示每行具体放的位置
        if len(cur) >= self.N:  # 递归出口
            if self.check(cur):
                self.result.append(cur.copy())  
            return
        for i in range(0, self.N):
            if i not in cur:  # 剪枝排除掉一些列重复的情况
                cur.append(i)
                self.dfs(cur)
                cur.pop()

    def search(self, tofile):
        self.dfs([])
        self.outputresult(tofile=tofile)

    def next(self,cur):# 输入一个状态返回下一个符合的状态，开始默认空状态，输入最后一个状态输出[]
        # 首位添加-1
        cur = [-1,*cur]
        # N进制加1
        if len(cur)>1:
            cur[-1]+=1
            for i in range(-1,-self.N,-1):
                if cur[i]==self.N:
                    cur[i]=0
                    cur[i-1]+=1
                else:
                    break
        # 用+1状态获得下一合理局面
        pop = -1
        flag = 0
        while len(cur):
            if len(cur)-1 == self.N:  # 递归出口
                tmp = cur[1:]
                if self.check(tmp):
                    return tmp
                else:# 长度满了但不符
                    pop = cur.pop()
                    flag = 1
            # 长度未满，直接加
            for i in range(flag*(pop+1), self.N):
                if i in cur:  # 剪枝排除掉一些列重复的情况
                    continue
                cur.append(i)
                flag = 0
                break
            else:
                # 子树遍历完了弹栈
                pop = cur.pop()
                flag=1
        return []
```

### 可视化

调用python中的`tkinter`库完成${N}$​​​皇后问题求解可视化呈现，代码详见附件。由于${N}$​​​较大时展示不便，在此取${N}$​​的调节范围为$[4,11]$​​​，部分界面可视化如下：

<center><img src="https://pic4.zhimg.com/80/v2-56b7ca4b36d414179a038d1b0c87e91a.png" alt="可视化展示 (2)" style="zoom: 41%;" /></center>

<center><img src="https://pic4.zhimg.com/80/v2-6f9c394f389fc6d4b579169e3892825f.png" alt="可视化展示 (4)" style="zoom:42%;" /></center>

具体界面操作见视频演示（连续执行是循环播放所有可能的局面）。

## 结果呈现

当${N\ge15}$​​时合理局面数已经超过两百万，程序运行时间较长，在此展示${N\le14}$​​​的N皇后问题合理局面总数。

<center><img src="https://pic4.zhimg.com/80/v2-27f1839594acac4a10fced754f01a9ee.png" alt="N皇后总情况数" style="zoom: 40%;" /></center>

观察结果，仅当${N=1}$​或${N\ge4}$​时${N}$​​皇后问题才有非零解。

## 评价总结

### 优点

- 本实验将传统的八皇后问题推广至${N}$​皇后问题，更具普遍性。
- 本实验采用剪枝+回溯算法避免了组合爆炸问题，在合理的时间空间复杂度内得到了准确的${N}$​​皇后问题的合理局面数。
- 本实验分别使用递归方法和非递归方法求解${N}$皇后问题，适用性强，灵活度高，便于可视化呈现

### 拓展

一种改进的思路是对于不同的皇后问题，使用不同的方法计算合理局面数。

对于${N\ne2/3/8/9/14/15/26/27/38/39}$​​的任意N皇后问题，可以采取**分治法**确定部分解。例如可以通过5皇后问题的解确定25皇后问题的部分解进而确定125皇后问题的部分解，示意图如下：

<center><img src="https://pic4.zhimg.com/80/v2-0d84a62aa0571e8fa9d10544037a4cde.png" alt="改进" style="zoom: 33%;" /></center>

以此类推，分治思路成倍向外扩展便能生成一个无穷皇后问题的解。

### 总结

本实验对传统的八皇后问题进行推广，在求解${N}$​皇后问题所有满足条件的棋局及局面总数的过程中掌握了回溯法避免**组合爆炸**的思想以及剪枝减少时间复杂度的优化算法，同时还设计**非递归**算法对${N}$​皇后问题的结果进行了清晰的可视化呈现，还进一步探究了**分治**法在${N}$​皇后问题中的应用，为生成无穷皇后问题的解提供了可行思路。

