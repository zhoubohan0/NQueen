import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
import numpy as np

# sample=[np.array([2, 4, 1, 7, 5, 3, 6, 0]),
# np.array([2, 4, 6, 0, 3, 1, 7, 5]),
# np.array([5, 4, 7, 3, 0, 6, 1, 2]),
# np.array([6, 5, 1, 4, 7, 0, 2, 3]),
# np.array([1, 5, 2, 6, 0, 3, 7, 4]),
# np.array([3, 5, 1, 6, 4, 0, 7, 2])]
#
# sample_length=len(sample)          #结果个数，就是num
# n1=len(sample[0])                  #棋盘边长
# n2=len(sample[0][sample[0]>=0])    #皇后数量
#
# #绘制棋盘并保存求解结果
# def plot_chess(sample):
#     global num
#     mat=np.zeros((8,8))
#     for i in range(8):
#         for j in range(8):
#             if sample[i]==j:
#                 mat[i,j]=1
#             elif (i+j)%2==0:
#                 mat[i,j]=-1
#             else:
#                 mat[i,j]=0
#     my_cmap=matplotlib.colors.LinearSegmentedColormap.from_list('my_camp',['white','blue','deeppink'],3)
#     plt.imshow(mat,cmap=my_cmap)
#     # plt.title("第"+str(num)+"种解法",fontsize=16)
#     plt.xticks([])
#     plt.yticks([])
#     plt.show()
#     plt.cla()  # 清除掉之前的所有图
#     # plt.close('all')  # 关闭图
#     # plt.savefig('./result/'+str(num)+'.png') #保存图片的路径,自行修改
#
# for each in sample:
#     plot_chess(each)


#滚动播放图片
# sample=[[1,5,8,6,3,7,2,4],
# [1,6,8,3,7,4,2,5],
# [1,7,4,6,8,2,5,3],
# [1,7,5,8,2,4,6,3],
# [2,4,6,8,3,1,7,5],
# [2,5,7,1,3,8,6,4],
# [2,5,7,4,1,8,6,3],
# [2,6,1,7,4,8,3,5],
# [2,6,8,3,1,4,7,5],
# [2,7,3,6,8,5,1,4],
# [2,7,5,8,1,4,6,3],
# [2,8,6,1,3,5,7,4],
# [3,1,7,5,8,2,4,6],
# [3,5,2,8,1,7,4,6],
# [3,5,2,8,6,4,7,1],
# [3,5,7,1,4,2,8,6],
# [3,5,8,4,1,7,2,6],
# [3,6,2,5,8,1,7,4],
# [3,6,2,7,1,4,8,5],
# [3,6,2,7,5,1,8,4],
# [3,6,4,1,8,5,7,2],
# [3,6,4,2,8,5,7,1],
# [3,6,8,1,4,7,5,2],
# [3,6,8,1,5,7,2,4],
# [3,6,8,2,4,1,7,5],
# [3,7,2,8,5,1,4,6],
# [3,7,2,8,6,4,1,5],
# [3,8,4,7,1,6,2,5],
# [4,1,5,8,2,7,3,6],
# [4,1,5,8,6,3,7,2],
# [4,2,5,8,6,1,3,7],
# [4,2,7,3,6,8,1,5],
# [4,2,7,3,6,8,5,1],
# [4,2,7,5,1,8,6,3],
# [4,2,8,5,7,1,3,6],
# [4,2,8,6,1,3,5,7],
# [4,6,1,5,2,8,3,7],
# [4,6,8,2,7,1,3,5],
# [4,6,8,3,1,7,5,2],
# [4,7,1,8,5,2,6,3],
# [4,7,3,8,2,5,1,6],
# [4,7,5,2,6,1,3,8],
# [4,7,5,3,1,6,8,2],
# [4,8,1,3,6,2,7,5],
# [4,8,1,5,7,2,6,3],
# [4,8,5,3,1,7,2,6],
# [5,1,4,6,8,2,7,3],
# [5,1,8,4,2,7,3,6],
# [5,1,8,6,3,7,2,4],
# [5,2,4,6,8,3,1,7],
# [5,2,4,7,3,8,6,1],
# [5,2,6,1,7,4,8,3],
# [5,2,8,1,4,7,3,6],
# [5,3,1,6,8,2,4,7],
# [5,3,1,7,2,8,6,4],
# [5,3,8,4,7,1,6,2],
# [5,7,1,3,8,6,4,2],
# [5,7,1,4,2,8,6,3],
# [5,7,2,4,8,1,3,6],
# [5,7,2,6,3,1,4,8],
# [5,7,2,6,3,1,8,4],
# [5,7,4,1,3,8,6,2],
# [5,8,4,1,3,6,2,7],
# [5,8,4,1,7,2,6,3],
# [6,1,5,2,8,3,7,4],
# [6,2,7,1,3,5,8,4],
# [6,2,7,1,4,8,5,3],
# [6,3,1,7,5,8,2,4],
# [6,3,1,8,4,2,7,5],
# [6,3,1,8,5,2,4,7],
# [6,3,5,7,1,4,2,8],
# [6,3,5,8,1,4,2,7],
# [6,3,7,2,4,8,1,5],
# [6,3,7,2,8,5,1,4],
# [6,3,7,4,1,8,2,5],
# [6,4,1,5,8,2,7,3],
# [6,4,2,8,5,7,1,3],
# [6,4,7,1,3,5,2,8],
# [6,4,7,1,8,2,5,3],
# [6,8,2,4,1,7,5,3],
# [7,1,3,8,6,4,2,5],
# [7,2,4,1,8,5,3,6],
# [7,2,6,3,1,4,8,5],
# [7,3,1,6,8,5,2,4],
# [7,3,8,2,5,1,6,4],
# [7,4,2,5,8,1,3,6],
# [7,4,2,8,6,1,3,5],
# [7,5,3,1,6,8,2,4],
# [8,2,4,1,7,5,3,6],
# [8,2,5,3,1,7,4,6],
# [8,3,1,6,2,5,7,4],
# [8,4,1,3,6,2,7,5]]


sample=[[1,10,5,8,6,3,9,7,2,4],[8,4,10,1,3,6,2,7,9,5]]

def displayBoard(locations, shape,num):
    """Draw a chessboard with queens placed at each position specified
    by the assignment.

    Parameters
    ----------
    locations : list
        The locations list should contain one element for each queen
        of the chessboard containing a tuple (r, c) indicating the
        row and column coordinates of a queen to draw on the board.

    shape : integer
        The number of cells in each dimension of the board (e.g.,
        shape=3 indicates a 3x3 board)

    Returns
    -------
    matplotlib.figure.Figure
        The handle to the figure containing the board and queens
    """
    r = c = shape
    cmap = mpl.colors.ListedColormap(['#f5ecce', '#614532'])
    img = mpl.image.imread('queen.png').astype(np.float)    #matplotlib.image.imread()在读取图像的时候顺便归一化了，所以可能显示出小数；cv2.imread()正常显示了RGB整数的分布
    boxprops = {"facecolor": "none", "edgecolor": "none"}

    x, y = np.meshgrid(range(c), range(r))  #plt作图也可以输入网格矩阵，x、y分别对应着网格中所有点的横纵坐标
    plt.matshow(x % 2 ^ y % 2, cmap=cmap)
    plt.axis("off")  # eliminate borders from plot
    #
    fig = plt.gcf()
    fig.set_size_inches([r, c])
    scale = fig.get_dpi() / max(img.shape)
    ax = plt.gca()

    #之前的x和y只是为了创建棋盘,任务已经完成，接下来的x和y转义了
    for y, x in set(locations):
        box = mpl.offsetbox.OffsetImage(img, zoom=0.72/scale)    #将图片放在OffsetBox容器中
        ab = mpl.offsetbox.AnnotationBbox(box, (y, x), bboxprops=boxprops)
        ax.add_artist(ab)
    plt.title("第" + str(num) + "种解法", fontsize=36)
    # plt.show()  #注意：如果这里画了图后面就保存不了了，不知道为啥
    plt.savefig(f'./result/结果图像/{shape}皇后结果/结果图像/{num}.png')
    return fig

def draw_checkboard(shape):
    r = c = shape
    boxprops = {"facecolor": "none", "edgecolor": "none"}
    cmap = mpl.colors.ListedColormap(['#f5ecce', '#614532'])
    x, y = np.meshgrid(range(c), range(r))  # plt作图也可以输入网格矩阵，x、y分别对应着网格中所有点的横纵坐标
    plt.matshow(x % 2 ^ y % 2, cmap=cmap)
    plt.axis("off")  # eliminate borders from plot

    fig = plt.gcf()
    ax = plt.gca()
    fig.set_size_inches([r, c])
    # scale = fig.get_dpi() / max(img.shape)
    plt.title(f'{shape}皇后问题',fontsize=20)
    # plt.show()
    plt.savefig(f'./result/结果图像/{shape}皇后结果/棋盘图像/{shape}阶棋盘.png')
    return fig




if __name__ == '__main__':


    count=0
    for each in sample:
        locations = []
        sample_length=len(each)
        for i in range(sample_length):
            locations.append((i, each[i]-1))
        displayBoard(locations,sample_length,num=count+1)
        count += 1
