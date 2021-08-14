#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/15 0:35
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_tk.py
#  ===========================
import tkinter as tk

# ______________________________________________________________
# 主窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x800')

# ______________________________________________________________
# 标签
# 写死标签显示
# l=tk.Label(window,text='just test',bg='green',font=('Arial',12),width=15,height=2)
# 写活标签显示
text1 = tk.StringVar()  # 设置字符串变量
l1 = tk.Label(window, textvariable=text1, bg='green', font=('Arial', 12), width=15, height=1)
l1.pack()  # 放置部件

# ______________________________________________________________
# 按钮
# 按钮点击函数
on_click = True


def hit_me():
    global on_click
    if on_click:
        text1.set('你点击我了！')
        on_click = False
    else:
        text1.set('')
        on_click = True


# command,点击调用函数
b1 = tk.Button(window, text='点  我', width=15, height=1, command=hit_me)
b1.pack()

# ______________________________________________________________
# 输入框
# 明文显示
e1 = tk.Entry(window, show=None, width=16)
e1.pack()
# 暗文显示
e2 = tk.Entry(window, show='*', width=16)
e2.pack()


# 插入至光标位置函数
def insert_point():
    insert_text = e1.get()
    t.insert('insert', insert_text)


# 插入至文末位置函数
def insert_end():
    insert_text = e2.get()
    t.insert('end', insert_text)


# 插入按钮
b2 = tk.Button(window, text='插入至光标处', width=15, height=1, command=insert_point)
b2.pack()
b3 = tk.Button(window, text='插入至末尾', width=15, height=1, command=insert_end)
b3.pack()

# 文本
t = tk.Text(window, height=2)
t.pack()

# ______________________________________________________________
# 标签部件
text2 = tk.StringVar()
l2 = tk.Label(window, textvariable=text2, bg='blue', font=('Arial', 12), width=10, height=1)
l2.pack()


# 选择函数
def print_select():
    value = lb.get(lb.curselection())
    text2.set(value)


b4 = tk.Button(window, text='显示你的选择', width=15, height=1, command=print_select)
b4.pack()

# 列表部件
text3 = tk.StringVar()
# 设置列表部件初始值
text3.set([11, 22, 33, 44])
lb = tk.Listbox(window, listvariable=text3)
# 往列表部件里插入值
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'First')
lb.insert(2, 'second')
# 删除列表部件的值
lb.delete(2)
lb.pack()

# ______________________________________________________________
# 单选框
text4 = tk.StringVar()
l3 = tk.Label(window, text='请选择！', bg='yellow', font=('Arial', 12), width=10, height=1)
l3.pack()


# 选择函数
def your_select():
    l3.config(text='你选择了' + text4.get())  # 更改标签的text配置


# 选择后，会把value值赋值给variable指定的对象text4
r1 = tk.Radiobutton(window, text='选项 A', variable=text4, value='A', command=your_select)
r1.pack()
r2 = tk.Radiobutton(window, text='选项 B', variable=text4, value='B', command=your_select)
r2.pack()
r3 = tk.Radiobutton(window, text='选项 C', variable=text4, value='C', command=your_select)
r3.pack()

# ______________________________________________________________
#尺度
window.mainloop()
