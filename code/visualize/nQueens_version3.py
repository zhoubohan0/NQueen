import numpy as np


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
            with open(f'../result/N={self.N}.txt', 'w') as f:
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
                # 绘图
                self.result.append(cur.copy())  # 这里一定要保存当前解的copy，否则会被析构
            return
        for i in range(0, self.N):
            if i not in cur:  # 剪枝排除掉一些列重复的情况
                cur.append(i)
                self.dfs(cur)
                cur.pop()

    def search(self, display):
        self.dfs([])
        if display:
            self.outputresult(tofile=True)

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

        return None
if __name__ == '__main__':
    nqueen = NQueen(N=8)
    res = []
    cnt=-1

    while True:
        res = nqueen.next(res)
        cnt+=1
        if res:
            print(np.array(res)+1)
        else:
            break
    print(cnt)