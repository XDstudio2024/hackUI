import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


root = tk.Tk()
root.title("hackUI v1")
root.geometry('500x500')

def b1():
    messagebox.showinfo("提示", "starting")
    os.system('connect.py')
def b2():
    messagebox.showinfo("提示", "starting")
    os.system('scan.py')
def b3():
    messagebox.showinfo("提示", "XD网络科技有限公司制作")
    Image.open("image/XD科创.png").show()

b1n = tk.Button(root, text="Connect工具", command=b1)
b2n = tk.Button(root, text="ip扫描工具", command=b2)
b3n = tk.Button(root, text="关于", command=b3)


b1n.pack()
b2n.pack()
b3n.pack()

root.mainloop()
