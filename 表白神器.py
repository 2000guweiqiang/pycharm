#引用tkinter工具包
from tkinter import *   # all = [a,b]
#from tkinter import messagebox

#定义关闭窗口提示
from tkinter import messagebox


def closeWindow():
    messagebox.showinfo(title="警告",message="回去，必须选一个")
    return

#定义喜欢的提示按钮
def Love():
    love = Toplevel(window)
    love.geometry("300x100+250+260")
    love.title("我也喜欢你")
    label=Label(love,text="我也喜欢你!",font=("微软雅黑",20))
    label.pack()
    btn=Button(love,text="好呀",width=10,height=2,command=closeallwindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW",closelove)
def closelove():
    return

#关闭所有窗口
def closeallwindow():
    window.destroy()

#定义不喜欢按钮
def noLove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+250+260")
    no_love.title("重新选")
    label = Label(no_love, text="乖乖回去重新选!", font=("微软雅黑", 25))
    label.pack()
    btn = Button(no_love, text="好呀", width=10, height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", closelove)

#窗口不能关
def closenolove():
    #messagebbox.showinfo("放弃吧回去重选- -")
    #renturn
    noLove()

#创建窗口
window=Tk()
#窗口标题
window.title("求爱小姐姐")
#窗口大小
window.geometry("380x420+500+240")
#love.title("哈哈")
btn=Button(text="确定")
#窗口位置
window.geometry("+500+240")
window.protocol("WM_DELETE_WINDOW",closeWindow)
#标签控件
label=Label(window,text="hey,小姐姐",font=("微软雅黑",25),fg="red")
label.grid(row=0,column=0)

label=Label(window,text="喜欢我吗?",font=("微软雅黑",35))
label.grid(row=3,column=1,sticky=E)

#插入图片
photo=PhotoImage(file=r"./666.png")
imageLable=Label(window,image=photo)
imageLable.grid(row=2,columnspan=3)


#喜欢按钮插件
btn=Button(window,text="喜欢",width=15,height=2,command=Love)
btn.grid(row=4,column=0,sticky=W)

#不喜欢按钮插件
btn=Button(window,text="不喜欢",command=noLove)
btn.grid(row=4,column=1,sticky=E)
#显示窗口
window.mainloop()

