from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.font import Font

class ppui():
    def __init__(self):
        root=Tk()
        root.title('地毯提花图片导入窗口')
        tabstrip=ttk.Notebook(root)
        tabstrip.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=1)
        tab1=Frame(tabstrip)
        # tab2=Frame(tabstrip)
        self.ui_content1(tab1,tabstrip)
        # self.ui_content2(tab2,tabstrip)
        self.ui_menu(root)
        root.update()
        root.geometry("600x400")
        root.resizable(False,False)
        root.mainloop()

    def ui_menu(self,root):
        menu=Menu(root)
        menu.add_cascade(label="帮助")
        menu.add_cascade(label="关于")
        root["menu"]=menu

    def ui_content1(self,root,parents):
        cont1_btn1=Button(root,text="选择图片",font=("Time New Rome", 9),width=10,height=1)
        cont1_label=Label(root,bg='white',width=45,height=18)
        cont1_label1=Label(root,text="圈高1：")
        self.search_key1=StringVar()
        cont1_entry1=Entry(root,textvariable=self.search_key1,bd=1 ,font=("Time New Rome", 11),width=6)
        self.search_key2=StringVar()
        cont1_label2=Label(root,text="圈高2：")
        cont1_entry2=Entry(root,textvariable=self.search_key2,bd=1 ,font=("Time New Rome", 11),width=6)
        self.search_key3=StringVar()
        cont1_label3=Label(root,text="圈高3：")
        cont1_entry3=Entry(root,textvariable=self.search_key3,bd=1 ,font=("Time New Rome", 11),width=6)
        self.search_key4=StringVar()
        cont1_label4=Label(root,text="圈高4：")
        cont1_entry4=Entry(root,textvariable=self.search_key4,bd=1 ,font=("Time New Rome", 11),width=6)
        self.search_key5=StringVar()
        cont1_label5=Label(root,text="圈高5：")
        cont1_entry5=Entry(root,textvariable=self.search_key5,bd=1 ,font=("Time New Rome", 11),width=6)
        self.search_key6=StringVar()
        cont1_label6=Label(root,text="针密：")
        cont1_entry6=Entry(root,textvariable=self.search_key6,bd=1 ,font=("Time New Rome", 11),width=6)
        self.search_key7=StringVar()
        cont1_label7=Label(root,text="地毯宽度：")
        cont1_entry7=Entry(root,textvariable=self.search_key7,bd=1 ,font=("Time New Rome", 11),width=6)
        cont1_btn2=Button(root,text="开始",font=("Time New Rome", 11),width=6,height=1)
        cont1_btn3=Button(root,text="停止",font=("Time New Rome", 11),width=6,height=1)
        cont1_btn1.place(relx=0.02,rely=0.05)
        cont1_label.place(relx=0.02,rely=0.14)
        cont1_label1.place(relx=0.6,rely=0.2)
        cont1_entry1.place(relx=0.68,rely=0.205)
        cont1_label2.place(relx=0.8,rely=0.2)
        cont1_entry2.place(relx=0.88,rely=0.205)
        cont1_label3.place(relx=0.6,rely=0.3)
        cont1_entry3.place(relx=0.68,rely=0.305)
        cont1_label4.place(relx=0.8,rely=0.3)
        cont1_entry4.place(relx=0.88,rely=0.305)
        cont1_label5.place(relx=0.6,rely=0.4)
        cont1_entry5.place(relx=0.68,rely=0.405)
        cont1_label6.place(relx=0.6,rely=0.6)
        cont1_entry6.place(relx=0.68,rely=0.605)
        cont1_label7.place(relx=0.6,rely=0.7)
        cont1_entry7.place(relx=0.72,rely=0.705)
        cont1_btn2.place(relx=0.62,rely=0.805)
        cont1_btn3.place(relx=0.78,rely=0.805)
        parents.add(root,text="提花设置")

    def ui_content2(self,root,parents):
        l2=Label(root,text='label2')
        l2.pack(fill=BOTH)
        parents.add(root,text="tab2")

if __name__ == '__main__':
    ppui()