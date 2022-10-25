# -*- coding:utf-8 -*-
'''
@Time : 2022/10/25  14:23
@File : mian.py
@Sofeware : PyCharm 
@author : Chen
'''

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Style, PanedWindow, Button, LabelFrame, Treeview
import pandas as pd
from PIL import Image, ImageTk
from tkinter import Frame
import time

# 先定义几个可能用到的常量
user_name = "kkyyds"
password = "123456"
LEFT = "left"
RIGHT = "right"
TOP = "top"
BOTTOM = "bottom"
Song = '宋体'
Microsoft = '微软雅黑'


class Root:  # 这是第一个页面
    def __init__(self, window):
        self.window = window
        self.window.title("登录页面")
        self.window.geometry("1000x600+250+100")
        self.window.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.frame = Frame(self.window)
        self.frame.config(bg="#C9C9C9")
        self.frame.pack()
        self.img_lable()
        self.lable()
        self.clock()
        self.login()

    def lable(self):
        tk.Label(self.frame, text="新版教学管理系统", font=(Song, 20), bg="#C9C9C9").place(relx=0.73, rely=0.45, relheight=0.05,
                                                                                   relwidth=0.25)

        tk.Label(self.frame, text="清华大学", font=("楷体", 30), bg="#C9C9C9").place(relx=0.73, rely=0.35, relheight=0.08,
                                                                               relwidth=0.25)

        tk.Label(self.frame, text="作者: CSDN@星空的你", font=("楷体", 10), bg="#C9C9C9").place(relx=0.73, rely=0.85,
                                                                                        relheight=0.08, relwidth=0.25)

    def img_lable(self):
        # photo1=tk.PhotoImage(file = '大学.png')#仅支持png和gif
        img2 = Image.open("背景图片.jpg")
        img1 = Image.open("背景图片.jpg")
        img2 = img2.resize((700, 600))  # 规定图片大小
        img1 = img1.resize((300, 200))  # 规定图片大小
        photo2 = ImageTk.PhotoImage(img2)  # 使用神器PIL库可以设置照片大小并且可以支持jpg格式等
        photo1 = ImageTk.PhotoImage(img1)  # 使用神器PIL库可以设置照片大小并且可以支持jpg格式等
        label2 = tk.Label(self.frame, image=photo2, borderwidth=0)
        label1 = tk.Label(self.frame, image=photo1, borderwidth=0)
        label2.img = photo2  # to keep the reference for the image.不保存会显示空白
        label1.img = photo1  # to keep the reference for the image.不保存会显示空白
        label2.grid(row=0, column=0)
        label1.grid(row=0, column=1, sticky="n")  # n就是北North表示最上方

    def login(self):

        # 将俩个标签分别布置在第一行、第二行
        tk.Label(self.frame, text="账号:", font=(Song, 15), bg="#C9C9C9").place(relx=0.7, rely=0.55, relheight=0.04,
                                                                              relwidth=0.1)
        tk.Label(self.frame, text="密码:", font=(Song, 15), bg="#C9C9C9").place(relx=0.7, rely=0.62, relheight=0.04,
                                                                              relwidth=0.1)
        # 创建输入框控件
        self.e1 = tk.Entry(self.frame)
        # 以 * 的形式显示密码
        self.e2 = tk.Entry(self.frame, show='*')
        self.e1.place(relx=0.8, rely=0.55, relheight=0.04, relwidth=0.18)
        self.e2.place(relx=0.8, rely=0.62, relheight=0.04, relwidth=0.18)
        tk.Button(self.frame, text="登录", width=20, command=self.check).place(relx=0.7, rely=0.7, relheight=0.06,
                                                                             relwidth=0.1)
        tk.Button(self.frame, text="退出", width=20, command=self.window.quit).place(relx=0.9, rely=0.7, relheight=0.06,
                                                                                   relwidth=0.1)

    def check(self):
        if self.e1.get() == user_name and self.e2.get() == password:
            messagebox.showinfo(title="登陆成功", message=f"欢迎回来，{user_name}!")
            self.frame.destroy()
            Home(self.window)
            return True
        else:
            messagebox.showwarning(title="登录失败", message="账号或密码错误")
            self.e2.delete(0, tk.END)
            return False

    def clock(self):
        # 获取时间的函数
        def gettime():
            # 获取当前时间
            dstr.set(time.strftime("%H:%M:%S"))
            # 每隔 1s 调用一次 gettime()函数来获取时间
            self.frame.after(1000, gettime)

        # 生成动态字符串
        dstr = tk.StringVar()
        # 利用 textvariable 来实现文本变化
        tk.Label(self.frame, textvariable=dstr, fg='green', font=("微软雅黑", 10), bg="#C9C9C9").place(relx=0.9, rely=0.93,
                                                                                                   relheight=0.08,
                                                                                                   relwidth=0.1)

        tk.Label(self.frame, text="time:", fg='green', font=("微软雅黑", 10), bg="#C9C9C9").place(relx=0.875, rely=0.93,
                                                                                              relheight=0.08,
                                                                                              relwidth=0.05)

        # 调用生成时间的函数
        gettime()


class Home:
    def __init__(self, window):
        self.window = window
        self.window.title(f"当前管理员为{user_name}")
        self.setup_UI()
        self.readExcel()
        self.query_result_list = []

    def readExcel(self):

        df = pd.read_excel("学生信息.xlsx", usecols="A:G", dtype=str)
        self.all_student_list = df.values.tolist()  # 把每一行存入一个列表再把每个列表存入列表

    def del_Entry_content(self):
        self.Entry_sno.delete(0, tk.END)
        self.Entry_name.delete(0, tk.END)
        self.Entry_profess.delete(0, tk.END)
        self.Entry_class.delete(0, tk.END)

    def show_all(self):
        self.clear_Tree()
        # 把所有条件文本框清空
        self.Entry_sno.delete(0, tk.END)
        self.Entry_name.delete(0, tk.END)
        self.Entry_profess.delete(0, tk.END)
        self.Entry_class.delete(0, tk.END)
        self.load_treeview(self.all_student_list)

    def load_treeview(self, current_list):
        for index in range(len(current_list)):
            self.Tree.insert("", index, values=(current_list[index][0],
                                                current_list[index][1],
                                                current_list[index][2],
                                                current_list[index][3],
                                                current_list[index][4],
                                                current_list[index][5],
                                                current_list[index][6]))

    def get_query_result(self):
        query_condition = []
        query_condition.append(self.Entry_sno.get().strip())  # 采集学号信息
        query_condition.append(self.Entry_name.get().strip())  # 采集姓名信息
        query_condition.append(self.Entry_profess.get().strip())
        query_condition.append(self.Entry_class.get().strip())

        # 遍历List获取符合条件的学生信息
        for item in self.all_student_list:
            if query_condition[0] in item[0] and query_condition[1] in item[3] and \
                    query_condition[2] in item[1] and query_condition[3] in item[2]:
                # 满足条件的学生
                self.query_result_list.append(item)
        # 把结果加载的TreeView中
        self.clear_Tree()
        self.load_treeview(self.query_result_list)
        self.query_result_list.clear()

    def clear_Tree(self):
        for i in self.Tree.get_children():
            self.Tree.delete(i)

    def setup_UI(self):
        # 设定Style
        self.Style01 = Style()
        self.Style01.configure("TPanedwindow", background="#C9C9C9")
        self.Style01.configure("TButton", width=10, font=(Song, 15,))
        # 上边：labe
        self.Pane_top = PanedWindow(width=980, height=85, style="TPanedwindow").place(x=10, y=5)
        tk.Label(self.Pane_top, text="学生信息管理系统", bg='#C9C9C9', font=("微软雅黑", 40), width=30).place(x=15, y=10)
        # 左边：按钮区域,创建一个容器
        self.Pane_left = PanedWindow(width=195, height=500, style="TPanedwindow").place(x=10, y=95)  # 这种写法下方是使用绝对距离
        self.Pane_right = PanedWindow(width=780, height=500, style="TPanedwindow")
        self.Pane_right.place(x=210, y=95)  # 这种写法下方是相对距离，明明写法含义都一样，结果却不一样简直莫名其妙。。。不是frame的原因，因为你把它挪上去在结尾添加下方frame位置会改变
        # 添加左边按钮
        self.Button_add = Button(self.Pane_left, text="添加学生", style="TButton").place(x=50, y=120)
        self.Button_update = Button(self.Pane_left, text="修改学生", style="TButton").place(x=50, y=160)
        self.Button_delete = Button(self.Pane_left, text="删除学生", style="TButton").place(x=50, y=200)
        self.Button_modify = Button(self.Pane_left, text="更改密码", style="TButton").place(x=50, y=260)
        # 添加右边按钮
        # LabelFrame
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生信息查询", width=770, height=40)
        self.LabelFrame_query.place(x=5, y=5)
        # 添加控件
        y1 = 1
        y2 = -2
        self.Label_sno = tk.Label(self.LabelFrame_query, text="学号:")
        self.Label_sno.place(x=5, y=y1)
        self.Entry_sno = tk.Entry(self.LabelFrame_query, width=12)
        self.Entry_sno.place(x=40, y=y2)

        self.Label_name = tk.Label(self.LabelFrame_query, text="姓名:")
        self.Label_name.place(x=125, y=y1)
        self.Entry_name = tk.Entry(self.LabelFrame_query, width=12)
        self.Entry_name.place(x=160, y=y2)

        self.Label_profess = tk.Label(self.LabelFrame_query, text="专业:")
        self.Label_profess.place(x=245, y=y1)
        self.Entry_profess = tk.Entry(self.LabelFrame_query, width=14)
        self.Entry_profess.place(x=280, y=y2)

        self.Label_class = tk.Label(self.LabelFrame_query, text="班级:")
        self.Label_class.place(x=380, y=y1)
        self.Entry_class = tk.Entry(self.LabelFrame_query, width=14)
        self.Entry_class.place(x=415, y=y2)

        self.Button_query = tk.Button(self.LabelFrame_query, text="查询", width=4, command=self.get_query_result)
        self.Button_query.place(x=520, y=y1 - 9)
        self.Button_query = tk.Button(self.LabelFrame_query, text="清除", width=4, command=self.del_Entry_content)
        self.Button_query.place(x=560, y=y1 - 9)
        self.Button_all = tk.Button(self.LabelFrame_query, text="清空全部", width=8, command=self.clear_Tree)
        self.Button_all.place(x=630, y=y2 - 8)
        self.Button_all = tk.Button(self.LabelFrame_query, text="显示全部", width=8, command=self.show_all)
        self.Button_all.place(x=700, y=y2 - 8)
        # 添加TreeView控件
        self.Tree = Treeview(self.Pane_right, columns=("sno", "专业", "班级", "names",
                                                       "gender", "绩点", "mobile"),
                             show="headings", height=21)

        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=120, anchor="center")
        self.Tree.column("names", width=100, anchor="center")
        self.Tree.column("gender", width=70, anchor="center")
        self.Tree.column("mobile", width=125, anchor="center")
        self.Tree.column("专业", width=140, anchor="center")
        self.Tree.column("班级", width=140, anchor="center")
        self.Tree.column("绩点", width=70, anchor="center")

        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("names", text="姓名")
        self.Tree.heading("gender", text="性别")
        self.Tree.heading("mobile", text="手机号码")
        self.Tree.heading("专业", text="专业")
        self.Tree.heading("班级", text="班级")
        self.Tree.heading("绩点", text="绩点")
        self.Tree.place(x=5, y=50)


if __name__ == '__main__':
    root = tk.Tk()
    Root(root)

    root.mainloop()