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
        cont1_btn1=Button(root,text="选择图片",font=0.5)
        cont1_btn1.place(relx=0.02,rely=0.02)
        parents.add(root,text="圈高设置")

    def ui_content2(self,root,parents):
        l2=Label(root,text='label2')
        l2.pack(fill=BOTH)
        parents.add(root,text="tab2")

if __name__ == '__main__':
    ppui()