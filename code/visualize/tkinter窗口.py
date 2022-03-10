import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from nQueens_version3 import NQueen
from draw_picture import *

'''设置常数'''
# 分辨率
resolution = (960, 600)
# 播放间隔.单位:s
Interval = 1
# 当前照片计数
count = 0
#统计结果个数
cnt=0
#结果
res=[]
result = []

nqueen=0

img_TK=0
numIdx=0
after_id='after#1'
# while True:


#无效代码
# class App(Frame):
#     def __init__(self,master=None):
#         super(App,self).__init__(master)
#         self.master=master
#         self.pack()
#         self.createWidget()



'''窗体长宽'''
scaler = Image.ANTIALIAS
#图像进行img.resize((width, height),Image.ANTIALIAS)的时候的第二参数：
# Image.NEAREST ：低质量
# Image.BILINEAR：双线性
# Image.BICUBIC ：三次样条插值
# Image.ANTIALIAS：高质量

win = tk.Tk()
win_width = 1150
win_height = 670
# 将窗口设置在屏幕居中位置
sw = win.winfo_screenwidth()    #屏幕宽    #1836
sh = win.winfo_screenheight()   #屏幕高    #864
x = (sw - win_width) / 2
y = (sh - win_height) / 2

img_box_x = 0
img_box_y = 0
img_box_w = win_width
img_box_h = win_height - 50
img_box_bg = '#ffffff'

win.title("八皇后问题可视化")
win.iconbitmap('./icon/queen.ico')
win.resizable(0,0)  #窗口不允许放大
win.geometry("%dx%d+%d+%d" % (win_width, win_height, x, y)) #注意第一组是窗口大小，第二组是距离屏幕左上角偏移量

# '''定义方法'''


def start_func(shape):
    #画出棋盘，并且屏蔽掉label框内的组件
    global root,count,panel,s1,one_step_Radiobutton,continue_Radiobutton,ax,nqueen,entry
    choice=['连续执行','单步执行']
    entry.delete(0, END)
    entry.insert(0,f'现在展示的是{shape}皇后问题的'+choice[v.get()]+'!' )
    root=f'./result/结果图像/{shape}皇后结果/'
    checkbroad_savedir=os.path.join(root,'棋盘图像/')
    result_savedir=os.path.join(root,'结果图像/')
    if not os.path.exists(checkbroad_savedir):
        os.makedirs(checkbroad_savedir)
    if not os.path.exists(result_savedir):
        os.makedirs(result_savedir)
    draw_checkboard(shape)
    img=os.path.join(root,f'棋盘图像/{shape}阶棋盘.png')
    img_in = Image.open(img)
    w, h = img_in.size  # 640*480
    size_new = ((int)(w * resolution[1] / h), resolution[1])  # size_new(800,600)
    img_out = img_in.resize(size_new, scaler)
    img = ImageTk.PhotoImage(img_out)
    #更新panel棋盘
    panel.configure(image=img)
    panel.image=img #不可缺少
    #禁用滑块和单选框
    s1.configure(state=DISABLED)
    one_step_Radiobutton.configure(state=DISABLED)
    continue_Radiobutton.configure(state=DISABLED)
    # win.update()
    nqueen = NQueen(N=s1.get())


def reset_func(shape):
    #label框里面的组件恢复使用，棋盘清空
    global s1,one_step_Radiobutton,continue_Radiobutton,root,cnt,res
    entry.delete(0, END)
    entry.insert(0, '版权所有：ZBH')
    img = os.path.join(root, f'棋盘图像/{shape}阶棋盘.png')
    img_in = Image.open(img)
    w, h = img_in.size  # 640*480
    size_new = ((int)(w * resolution[1] / h), resolution[1])  # size_new(800,600)
    img_out = img_in.resize(size_new, scaler)
    img = ImageTk.PhotoImage(img_out)
    # 更新panel棋盘
    panel.configure(image=img)
    panel.image = img  # 不可缺少
    #将label栏里面的东西解锁
    s1.configure(state=NORMAL)
    one_step_Radiobutton.configure(state=NORMAL)
    continue_Radiobutton.configure(state=NORMAL)
    #cnt置零
    cnt=0
    #res初始化
    res=[]
    # reset_event.set(0)
    # print('复位',reset_event.get())
def single_step_execution():
    global cnt,res,result,root
    # print('single_step_execution')
    if res is None:
        return
    res = nqueen.next(res)
    if res is None:
        return
    # result.append(res)
    cnt += 1
    locations = []
    sample_length = len(res)
    for i in range(sample_length):
        locations.append((i, res[i]))
    #存图片到文件夹
    displayBoard(locations, sample_length,cnt)
    img = os.path.join(root, f'结果图像/{cnt}.png')
    img_in = Image.open(img)
    w, h = img_in.size  # 640*480
    size_new = ((int)(w * resolution[1] / h), resolution[1])  # size_new(800,600)
    img_out = img_in.resize(size_new, scaler)
    img = ImageTk.PhotoImage(img_out)
    # 更新panel棋盘
    panel.configure(image=img)
    panel.image = img  # 不可缺少

# '''失败。。。直接循环没用'''
# def multiple_execution():
#
#     global cnt,res,result,root,win
#     print('multiple_execution')
#     res = nqueen.next(res)
#     while res :
#         print(res)
#         res = nqueen.next(res)
#         # result.append(res)
#         cnt += 1
#         locations = []
#         sample_length = len(res)
#         for i in range(sample_length):
#             locations.append((i, res[i]))
#         # 存图片到文件夹
#         displayBoard(locations, sample_length, cnt)
#         time.sleep(1000)
#         img = os.path.join(root, f'结果图像/{cnt}.png')
#         img_in = Image.open(img)
#         w, h = img_in.size  # 640*480
#         size_new = ((int)(w * resolution[1] / h), resolution[1])  # size_new(800,600)
#         img_out = img_in.resize(size_new, scaler)
#         img = ImageTk.PhotoImage(img_out)
#         # 更新panel棋盘
#         panel.configure(image=img)
#         panel.image = img  # 不可缺少
#         win.update()
#         win.after(1000)
#         input()
def update(idx):  # 定时器函数
    global frame,panel,img_TK,numIdx,after_id
    # print('开始update')

    img = img_TK[idx]
    idx += 1  # 下一帧的序号：在0,1,2,3,4,5...之间循环(共*帧)
    panel.configure(image=img)  # 显示当前帧的图片
    after_id=frame.after(1000, update, idx % numIdx)  # 1秒(1000毫秒)之后继续执行定时器函数(update)
    # print(after_id)
def multiple_execution():
    # print('开始多部执行')
    global root,frame,img_TK,numIdx
    res_dir = os.path.join(root,  '结果图像')
    length = len(os.listdir(res_dir))

    files = [os.path.join(res_dir, f'{i}.png') for i in range(1,length+1)]
    numIdx = length  # 帧数
    dealed_files=[]
    for img in files:
        img_in = Image.open(img)
        w, h = img_in.size  # 640*480
        size_new = ((int)(w * resolution[1] / h), resolution[1])  # size_new(800,600)
        img_out = img_in.resize(size_new, scaler)
        dealed_files.append(img_out)
    img_TK = [ImageTk.PhotoImage(each) for each in dealed_files]
    frame.after(1000, update, 0)  # 立即启动定时器函数(update)



def continue_func(flag):
    if flag:
        single_step_execution()
    else:
        multiple_execution()

def stop(event):
    # reset_event.set(event.num)
    frame.after_cancel(after_id)
# def continue_(event):
#     frame.after(1000, update,0)

'''这东西没用上。。。destory报错。。。'''
def exit_program():
    global entry
    entry.delete(0,END)
    entry.insert(0,'如果觉得还不错，记得一键三连哦！')
    win.after(1000,win.quit,0)
'''设置组件、绑定方法'''
bg = tk.Label(win, bg='#DDDDDD')    #设置背景颜色为灰色
bg.place(height=win_height, width=win_width, x=0, y=0)

# 选择文件夹内的第一张图片名称
img_in = Image.open("8阶棋盘.png")
w, h = img_in.size  #640*480
size_new = ((int)(w * resolution[1] / h), resolution[1])    #size_new(800,600)
img_out = img_in.resize(size_new, scaler)
img = ImageTk.PhotoImage(img_out)

#图片面板
frame=Frame(win,height=img_box_h,highlightcolor='yellow')
frame.pack(padx=30,pady=30,fill='x')

panel = tk.Label(frame, image=img)
# # panel.place(x=0,y=0)
# # panel.pack(expand="no",anchor="w")    #expend表示是不是剩余空间的中心
panel.grid(row=0,column=0,rowspan=5)    #rowspan表示跨度为5行

# #构建框架
# frame=Frame(win,highlightcolor='yellow',relief=SUNKEN)
# frame.pack(expand=1,side='right',padx=10,pady=10)

#鼠标悬浮到上面的图案
cursor_list=["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek","watch"]

#设定基准位置
standard_x=0.6
standard_y=0.13

#突出强调调整棋盘大小与执行方式的frame
emphasis_frame=Frame(frame,width=420,height=180)
emphasis_frame.place(relx=standard_x-0.02,rely=standard_y-0.04)
label = tk.Label(emphasis_frame, relief="sunken",width=57,height=8,bd=4)
label.grid(row=0,column=0)

#棋盘大小标签
checkerboard_size=Label(emphasis_frame,text='大小:',font=('微软雅黑',20))
# checkerboard_size.grid(row=0,column=0,ipadx=0,sticky=tk.E+tk.W)
checkerboard_size.place(relx=0.07,rely=0.13)
#调整棋盘阶数滑动条
s1=Scale(emphasis_frame,from_=4,to_=11,length=250,tickinterval=1,orient=HORIZONTAL)
s1.set(8)   #初始值
# s1.grid(row=0,column=1,sticky=tk.W)
s1.place(relx=0.28,rely=0.07)


#单步执行单选框
v = tk.IntVar()    # 设置关联变量
v.set(1)
one_step_Radiobutton=Radiobutton(emphasis_frame,text='单步执行',variable=v,value=1,bd=10,width=8,cursor="arrow",font=('微软雅黑',18))
# one_step_Radiobutton.grid(row=1,column=1)
one_step_Radiobutton.place(relx=0.1,rely=0.5)
#连续执行单选框
continue_Radiobutton=Radiobutton(emphasis_frame,text='连续执行',variable=v,value=0,bd=10,width=8,cursor="arrow",font=('微软雅黑',18))
# continue_Radiobutton.grid(row=1,column=2,padx=10)
continue_Radiobutton.place(relx=0.5,rely=0.5)


#开始按钮
start=tk.PhotoImage(file="./icon/开始.png")
start_button=Button(frame,text='开始',image=start,bd=3,padx=1,pady=1,cursor="arrow",font=('微软雅黑',10),command=lambda:start_func(s1.get()))
# start_button.bind("<Button-1>",continue_func(frame,s1.get()))
# start_button.grid(row=2,column=1,padx=18)
start_button.place(relx=standard_x+0.05,rely=standard_y+0.27)

#复位按钮
# reset_event = tk.IntVar()    # 设置关联变量
# reset_event.set(0)
reset=tk.PhotoImage(file="./icon/复位.png")
reset_button=Button(frame,text='复位',image=reset,bd=3,padx=1,pady=1,cursor="arrow",font=('微软雅黑',10),command=lambda:reset_func(s1.get()))
reset_button.bind("<Button-1>",stop)

# reset_button.grid(row=2,column=2)
reset_button.place(relx=standard_x+0.2,rely=standard_y+0.27)


#继续按钮
continue_png=tk.PhotoImage(file="./icon/继续.png")
continue_button=Button(frame,text='继续',image=continue_png,bd=3,cursor='arrow',font=('微软雅黑',18),command=lambda:continue_func(v.get()))
# if v.get():
#     continue_button.bind('<Button-1>',single_step_execution)
# else:
#     continue_button.bind('<Button-1>',multiple_execution)
# continue_button.grid(row=3,column=2)
continue_button.place(relx=standard_x+0.05,rely=standard_y+0.45)

#结束按钮
end=tk.PhotoImage(file="./icon/结束.png")
end_button=Button(frame,text='结束',image=end,bd=3,cursor="arrow",font=('微软雅黑',18),command=win.destroy)
# end_button.bind('<Button-1>',win.destroy)
# end_button.grid(row=3,column=1,padx=18)
end_button.place(relx=standard_x+0.2,rely=standard_y+0.45)

#文本框
entry=tk.Entry(bd=3,width=30,font=('微软雅黑',15),fg='black',justify=CENTER,relief=SUNKEN)
entry.insert(0,'别忘记先点击开始按钮呦！')
entry.place(relx=standard_x,rely=standard_y+0.67)



# #版权所有
# copyright=tk.PhotoImage(file="./icon/版权.png")
# copyright_button=Button(frame,text='版权所有',image=copyright,bd=3,cursor="man",font=('微软雅黑',18))
# # copyright_button.grid(row=4,column=1)
# copyright_button.place(relx=standard_x+0.2,rely=standard_y+0.63)

win.mainloop()


'''zbh写的类'''
# nqueen = NQueen(N=8)
# res = []
# cnt=-1
# while True:
#     res = nqueen.next(res)
#     cnt+=1
#     if res:
#         print(np.array(res)+1)
#     else:
#         break
# print(cnt)