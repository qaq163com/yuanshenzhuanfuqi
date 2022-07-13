import shutil
import tkinter
import os
import winreg
import requests
import win32com.client

字体大小=10

def 检查是否有新版本():
    当前版本=open("data/当前转服器版本","r").read()
    最新版本=requests.get(url="http://8.142.28.115/版本").text
    if 当前版本 != 最新版本:
        return True
    else:
        return False

def 提示(title,data):
    错误提示=tkinter.Tk()
    错误提示.title(title)
    错误提示.iconbitmap("data/图标.ico")
    tkinter.Label(错误提示,font=字体大小,text=data).pack()
    错误提示.geometry("400x50")
    错误提示.resizable(False, False)
    错误提示.mainloop()

def 获取桌面路径():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]

def 获取路径():
    data=open("data/config").read()
    return data

def 获取快捷方式指向的位置(path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    return shortcut.Targetpath

def 获取桌面原神快捷方式():
    path=获取桌面路径()+r"\原神.lnk"
    return path

def 保存路径(path):
    #对用户输入的路径进行修改
    path=path.replace("：",":")
    path=path.replace("/",r'\惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠')
    path=path.replace("惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠惠","")
    a=open("data/config", "w")
    a.write(path)
    a.close()
    当前路径.set("当前路径:   " + open("data/config", "r").read())

def 保存路径按钮命令():
    path=路径输入框.get()
    保存路径(path)

def 自动获取路径按钮命令():
    path = 获取快捷方式指向的位置(获取桌面原神快捷方式())
    path=path.replace(r"\launcher.exe",'')
    保存路径(path)
    提示("可爱の惠惠の提示","路径保存成功QAQ（快夸我）")

def 官转B():
    B_data=open("data/bilibili_config").read()
    try:
        a=open(获取路径()+ r"\Genshin Impact Game\config.ini","w")
    except:
        try:
            a = open(获取路径() + r"\ Game\config.ini", "w")
        except:
            提示(title='地址错误',data='请检查符号是否都是英文状态下输入')
    a.write(B_data)
    a.close()
    shutil.copy("data/PCGameSDK.dll", 获取路径() + r"\Genshin Impact Game\YuanShen_Data\Plugins\PCGameSDK.dll")

def B转官():
    G_data=open("data/官服_config").read()
    try:
        a=open(获取路径()+ r"\Genshin Impact Game\config.ini","w")
    except:
        try:
            a = open(获取路径() + r"\ Game\config.ini", "w")
        except:
            提示(title='地址错误',data='请检查符号是否都是英文状态下输入')
    a.write(G_data)
    a.close()
    os.remove(获取路径()+ r"\Genshin Impact Game\YuanShen_Data\Plugins\PCGameSDK.dll")

def 系统路径转换(data):
    return data.replace(" ",'" "')

def 启动():
    path=获取路径()
    盘符=path[:1]
    print(盘符)
    命令一='cd {}\Genshin" "Impact" "Game'.format(系统路径转换(path))
    os.system("{}:&".format(盘符)+命令一+"&.\YuanShen")

if __name__ == '__main__':

    tk=tkinter.Tk()
    当前路径=tkinter.Variable()
    当前路径.set("当前路径:   "+获取路径())
    """---------------------------------  窗口配置  ----------------------------------------"""
    tk.title("原神转服器  持续更新  作者--惠惠  qq:1621320515  bilibili:是惠惠不是惠惠 QQ群号:788395240")
    tk.geometry("1000x618")
    tk.resizable(False, False)
    tk.iconbitmap("data/图标.ico")
    路径=获取路径()
    """---------------------------------  背景设置  ---------------------------------------------"""
    背景图片 = tkinter.PhotoImage(file="data/背景.png")
    tkinter.Label(tk,image=背景图片).pack()
    """---------------------------------  控件设置  ---------------------------------------------"""
    示例图片 = tkinter.PhotoImage(file="data/路径查找示范.png")
    路径查找示范图片 = tkinter.Label(tk,font=字体大小, image = 示例图片)
    当前路径显示=tkinter.Label(tk,font=字体大小,textvariable=当前路径)
    路径输入框=tkinter.Entry(tk)
    保存路径按钮=tkinter.Button(tk,text="手动保存路径",font=字体大小,command=保存路径按钮命令)
    自动获取路径按钮=tkinter.Button(tk,text="自动获取路径",font=字体大小,command=自动获取路径按钮命令)
    官转B按钮=tkinter.Button(tk,text='官服转B服',font=字体大小,command=官转B)
    B转官按钮=tkinter.Button(tk,text='B服转官服',font=字体大小,command=B转官)
    启动按钮=tkinter.Button(tk,text='启动！！！',font=字体大小,command=启动)
    """---------------------------------  布局设置  ---------------------------------------------"""
    路径查找示范图片.place(x=50,y=50)
    当前路径显示.place(x=500,y=50,width=430,height=50)
    路径输入框.place(x=500,y=170,width=430,height=50)
    保存路径按钮.place(x=850,y=170,width=150,height=50)
    B转官按钮.place(x=500,y=350,width=430,height=100)
    官转B按钮.place(x=50,y=350,width=430,height=100)
    启动按钮.place(x=170,y=480,width=600,height=100)
    自动获取路径按钮.place(x=500,y=110,width=430,height=50)
    '''---------------------------------  检查版本更新---------------------------------------'''
    if 检查是否有新版本():
        提示("更新提醒","up主发布了新版本,请及时下载")
    """---------------------------------  窗口启动  ---------------------------------------------"""
    tk.mainloop()