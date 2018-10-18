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
        tab2=Frame(tabstrip)
        self.ui_content1(tab1,tabstrip)
        self.ui_content2(tab2,tabstrip)
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
        cont1_btn1=Button(root,text="选择图片",font=("Microsoft YaHei", 7),width=10,height=1)
        cont1_label=Label(root,bg='white',width=45,height=18)
        cont1_label1=Label(root,text="圈高1：")
        self.search_key=StringVar()
        cont1_entry1=Entry(root,textvariable=self.search_key,bd=1 ,font=("Time New Rome", 11),width=6)
        cont1_btn1.place(relx=0.02,rely=0.05)
        cont1_label.place(relx=0.02,rely=0.14)
        cont1_label1.place(relx=0.6,rely=0.2)
        cont1_entry1.place(relx=0.68,rely=0.205)
        parents.add(root,text="圈高设置")

    def ui_content2(self,root,parents):
        l2=Label(root,text='label2')
        l2.pack(fill=BOTH)
        parents.add(root,text="tab2")

if __name__ == '__main__':
    ppui()