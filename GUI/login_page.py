# -*- coding:utf-8 -*-
'''
@Time : 2022/10/25  10:46
@File : login_page.py
@Sofeware : PyCharm 
@author : Chen
'''
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox


username ='chensd'
password = '123456'

class Login_Page:
    def __init__(self,master):
        self.master = master
        self.master.title('登录页面')
        self.master.geometry('720x480+40+40')
        self.master.resizable(0,0)   #窗体大小不允许变，两个参数分别代表x轴和y轴
        self.frame = Frame(self.master)
        self.frame.config(bg='#C9C9C9')
        self.frame.pack()

        self.img_label()
        self.login()

    #布置背景图片
    def img_label(self):
        img1 = Image.open('背景图片.jpg')
        img1 = img1.resize((720,480))  #定义图片的大小
        photo = ImageTk.PhotoImage(img1)
        label = Label(self.frame,image=photo,borderwidth=0)
        label.img=photo
        label.grid(row=0,column=0)

    #布置账号密码输入框
    def login(self):
        Label(self.frame, text=' 账号',font=('song','15'),bg='#00ffcc').place(relx=0.15,rely=0.3,relheight=0.05,relwidth=0.1)
        Label(self.frame, text=' 密码', font=('song', '15'), bg='#00ffcc').place(relx=0.15, rely=0.4, relheight=0.05,
                                                                              relwidth=0.1)
        #输入框
        self.e1 = Entry(self.frame)
        #密码以*显示
        self.e2 = Entry(self.frame,show='*')
        self.e1.place(relx=0.3,rely=0.3,relheight=0.05,relwidth=0.25)
        self.e2.place(relx=0.3, rely=0.4, relheight=0.05, relwidth=0.25)

        Button(self.frame,text='登录',width=20,bg='#7D9EC0',command = self.check_user).place(relx=0.25,rely=0.5,relheight=0.06,relwidth=0.1)
        # Button(self.frame, text='注册', width=20,bg='#7D9EC0').place(relx=0.4, rely=0.5, relheight=0.06, relwidth=0.1)




    def check_user(self):
        if self.e1.get()==username and self.e2.get() ==password:
            messagebox.showinfo(title='登录成功',message=f'欢迎回来 {username}')
            self.frame.destroy()
            File_System(self.master)
            return True


        else:
            messagebox.showwarning(title='登录失败',message='账号密码错误')
            self.e2.delete(0,END)
            return False

class File_System:
    def __init__(self,master):
        self.master = master
        self.master.title('文件系统')
        self.master.geometry('720x480+40+40')
        self.master.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.create_menu_bar()

    #创建菜单栏
    def create_menu_bar(self):
        menu_bar = Menu(self.master)
        self.master['menu'] = menu_bar

        #文件功能
        file_menu = Menu(menu_bar,tearoff=0)
        file_menu.add_command(label='新建',accelerator='Ctrl+N')
        file_menu,add_command(label='打开',accelerator='Ctrl+O')
        file_menu.add_command(label='保存',accelerator='Ctrl+S')
        file_menu.add_command(label='另存为',accelerator='Ctrl+Shift+S')
        file_menu.add_separaotr()
        file_menu.add_command(label='退出',accelerator='Alt+F4')
        menu_bar.add_cascade(label='文件',menu=file_menu)








if __name__ == '__main__':
    root = Tk()
    Login_Page(root)

    root.mainloop()