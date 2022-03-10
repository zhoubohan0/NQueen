import numpy as np

def displayresult(N1,N2):
    print(f'棋盘大小{N1}×{N1},皇后数量{N2},合格局面总数:{len(globalresult)}')#\n所有局面情况:{globalresult})
def judge(l):  # 每行列斜之和不超过1
    for each in l:
        if each>1:
            return False
    return True
def valid(cur, cond):
    boolMatrix = np.zeros((N1, N1))  # 转化成布尔矩阵
    for i in range(len(cur)):
        if cond[i]:
            boolMatrix[i, cur[i]] = 1
    flag = True  # 合格局面
    # 判列
    l = np.sum(boolMatrix, axis=0)
    flag &= judge(l)

    if not flag:
        return flag
    # 判行
    r = np.sum(boolMatrix, axis=1)
    flag &= judge(r)

    if not flag:
        return flag
    # 判左下右上斜线:i+j∈[0,2*(N1-1)]
    for tmpadd in range(0, 2 * (N1 - 1) + 1):
        tmp = [boolMatrix[i, tmpadd - i] for i in range(N1) if 0 <= tmpadd - i < N1]
        flag &= (sum(tmp)<=1)
        if not flag:
            return flag

    # 判左上右下斜线:i-j∈[-(N1-1),(N1-1)]
    for tmpminus in range(1 - N1, N1):
        tmp = [boolMatrix[i, i - tmpminus] for i in range(N1) if 0 <= i - tmpminus < N1]
        flag &= (sum(tmp)<=1)
        if not flag:
            return flag

    return flag  # 运行到这里一定是经过四大检验的合格局面
def dfs(cur, cond):
    # cur:现在搜索阶段，行先序，0~N1-1表示每行具体放的位置，-1表示此行不放
    # cond:cur中放皇后的情况

    if len(cur) >= N1:  # 递归出口
        if valid(cur, cond):
            globalresult.append(cur)
        return
    for i in range(-(N1 - len(cur) > N2 - sum(cond)), N1):
        if i==-1 or i not in cur:  # 剪枝排除掉一些列重复的情况
            cur.append(i)
            cond.append(i != -1)
            dfs(cur, cond)
            cur.pop()
            cond.pop()


if __name__ == '__main__':
    N1 = 8  # 方形棋盘边长
    N2 = 8  # 皇后数量
    globalresult = []  # 所有皇后合理安放局面
    if N1 >= N2:
        dfs([], [])
    displayresult(N1,N2)
