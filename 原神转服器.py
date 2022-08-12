import webbrowser
import shutil
import time
import tkinter
import os
import requests
import winreg
import threading
from PIL import Image
import filedialogs


data文件缺失提示="""您在最开始下载的时候，压缩包里有一个data文件
请将那个文件与此程序放在同一文件夹,否则无法打开"""
更新提示="""更新内容:{}
""".format(requests.get("http://8.142.28.115/新版本更新内容").text)








字体大小=10

def 下载(url,保存位置):
    def 写入url(url):
        a=open("data/下载url","w",encoding="utf-8")
        a.write(url)
        a.close()
    def 写入保存位置(保存位置):
        a=open("data/下载后保存的位置","w",encoding="utf-8")
        a.write(保存位置)
        a.close()
    def 启动下载():
        path = os.getcwd()
        命令一 = "cd {}".format(系统路径转换(path))
        os.system("{}:&".format(path[:1]) + 命令一 + "&.\{}".format("下载"))

    写入url(url)
    写入保存位置(保存位置)
    threading.Thread(group=None,args=(),kwargs={},daemon=None,target=启动下载).start()

def 下载新版本():
    webbrowser.open("http://8.142.28.115/惠惠原神转服器安装包.exe")

def 创建新线程(函数):
    threading.Thread(group=None,args=(),kwargs={},daemon=None,target=函数).start()

def 提示(title,data):
    错误提示=tkinter.Tk()
    错误提示.title(title)
    错误提示.iconbitmap("data/图标.ico")
    tkinter.Label(错误提示,font=字体大小,text=data).pack()
    错误提示.resizable(False, False)
    错误提示.mainloop()

def 获取目录下的文件(rootdir):
    import os
    _files = []
	# 列出文件夹下所有的目录与文件
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
		# 构造路径
        path = os.path.join(rootdir, list[i])
		# 判断路径是否为文件目录或者文件
		# 如果是目录则继续递归
        if os.path.isdir(path):
            _files.extend(获取目录下的文件(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

def 获取桌面路径():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]

def 获取路径():
    data=open("data/config").read()
    return data

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
    print("正在自动获取路径")
    磁盘=["C","D","E","F","G",'H',"A","B"]
    for a in 磁盘:
        try:
            路径=search(a+r":\\","Genshin Impact Game")
            if 路径==-1:
                pass
            else:
                保存路径(路径.replace(r"\\",r"\惠惠惠惠惠惠").replace(r"惠惠惠惠惠惠",r"")+"\Genshin Impact Game")
                提示("可爱の惠惠の提示","路径保存成功")
                break
        except:
            提示("可爱の惠惠の提示", "没...没有找到路径...(一脸失落)")

def 启动(文件名):
    path=获取路径()
    命令一="cd {}".format(系统路径转换(path))
    os.system("{}:&".format(path[:1])+命令一+"&.\{}".format(文件名))

def 官转国():
    try:
        os.rename(获取路径() + "\YuanShen_Data", 获取路径() + "\GenshinImpact_Data") #先改名
        os.remove(获取路径() + "\YuanShen.exe")  #删除其他原神服主程序
    except Exception as err:
        pass
    shutil.unpack_archive("data/官转国.zip", extract_dir=获取路径(), format=None) #再解压

def 国转官():
    try:
        os.rename(获取路径() + "\GenshinImpact_Data", 获取路径() + "\YuanShen_Data") #先改名
        os.remove(获取路径() + "\GenshinImpact.exe")  #删除其他原神服主程序
    except Exception as err:
        pass
    shutil.unpack_archive("data/国转官.zip", extract_dir=获取路径(), format=None) #再解压

def 官转b():
    try:
        os.rename(获取路径() + "\GenshinImpact_Data", 获取路径() + "\YuanShen_Data") #先改名
    except Exception as err:
        pass
    shutil.unpack_archive("data/官转b.zip", extract_dir=获取路径(), format=None) #再解压

def b转官():
    shutil.unpack_archive("data/b转官.zip", extract_dir=获取路径(), format=None) #先解压
    try:
        os.remove(获取路径()+"\YuanShen_Data\Plugins\PCGameSDK.dll")
    except Exception as err:
        print(err)

def 启动(服="官服"):
    if 服=="官服":
        文件名="YuanShen"
    if 服=='b服':
        文件名 = "YuanShen"
    if 服=="国际服":
        文件名="GenshinImpact"
    path=获取路径()
    命令一="cd {}".format(系统路径转换(path))
    os.system("{}:&".format(path[:1])+命令一+"&.\{}".format(文件名))

def 获取当前服(是否返回未选择=True):
    try:
        config=open(获取路径()+"\config.ini","r").read()
    except:
        if 是否返回未选择:
            return ""
        else:
            自动获取路径按钮命令()
    if "channel=1" in config:
        if "sub_channel=1" in config:
            return "官服"
    if "channel=14" in config:
        if "sub_channel=0" in config:
            return "b服"
    if "channel=1" in config:
        if "sub_channel=0" in config:
            return "国际服"

def 官服启动():
    当前服=str(获取当前服())
    print(当前服+" ----- 官服")
    if 当前服=="官服":
        pass
    if 当前服=="b服":
        b转官()
    if 当前服=="国际服":
        国转官()
    当前服显示信息.set(获取当前服())
    启动("官服")

def 国际服启动():
    try:
        open("data/官转国.zip")
    except:
        下载("http://8.142.28.115/官转国.zip","data/官转国.zip")
    time.sleep(1)
    try:
        open("data/国转官.zip")
    except:
        下载("http://8.142.28.115/国转官.zip","data/国转官.zip")
    当前服=str(获取当前服())
    print(当前服+" ----- 国际服")
    if 当前服=="官服":
        官转国()
    if 当前服=="b服":
        b转官()
        time.sleep(1)
        官转国()
    if 当前服=="国际服":
        pass
    当前服显示信息.set(获取当前服())
    启动("国际服")

def b服启动():
    当前服=str(获取当前服())
    print(当前服+" ----- b服")
    if 当前服=="官服":
        官转b()
    if 当前服=="b服":
        pass
    if 当前服=="国际服":
        国转官()
        官转b()
    当前服显示信息.set(获取当前服())
    启动("b服")

def 选择路径():
    路径 = filedialogs.open_folder_dialog('选择"Genshin Impact Game"路径', 'gbk')
    print(路径)
    if "Genshin Impact Game" in 路径[-19:]:
        保存路径(路径)
        当前路径.set("当前路径:   " + open("data/config", "r").read())
        当前服显示信息.set(获取当前服())
        提示("可爱の惠惠の提示","路径保存成功")
    else:
        提示("可爱の惠惠の提示","请选择'Genshin Impact Game'文件夹哟~")

def 系统路径转换(data):
    return data.replace(" ",'" "')

def search(path, name):
    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in dirs or name in files:
            flag = 1  # 判断是否找到文件
            root = str(root)
            dirs = str(dirs)
            return os.path.join(root)
    return -1

def 查找原神数量():
    list=[r"C:/",r"D:/",r"E:/",r"F:/",r"G:/"]
    data=[]
    for i in list:
        a=search(i,"Genshin Impact Game")
        if a != -1:
            a=a.replace("\\","/")
            data.append(a+"/Genshin Impact Game")
    root=tkinter.Tk()
    tkinter.Label(root,text=data).pack()
    root.title("可爱の惠惠の占卜")
    root.mainloop()
    print(data)
    return data

def 给惠惠打赏按钮():
    im = Image.open('data/打赏.png')
    im.show()

def 更换背景():
    from tkinter import filedialog
    file_path = filedialog.askopenfilename(title='请选择一个文件', filetypes = [(('图片', ' .png'))])
    shutil.copy(file_path,"data/自定义背景图片.png")

def 帮助命令():
    提示("可爱の惠惠の帮助","""购买加速器请加QQ2198850363
如果点击转服后无响应，请检查杀毒软件是否关闭（包括windows安全中心）""")

def 检查更新(是否提示已是最新版本=False):
    最新版本=requests.get("http://8.142.28.115/4版本").text
    当前版本=open("data/当前转服器版本").read()
    print(float(当前版本), float(最新版本))
    if float(当前版本)<float(最新版本):
        更新窗口=tkinter.Tk()
        更新窗口.title("是否更新新版本")
        更新窗口.iconbitmap("data/图标.ico")
        tkinter.Label(更新窗口,text=更新提示, font=字体大小).pack()
        更新窗口.resizable(False, False)
        更新按钮=tkinter.Button(更新窗口,text="更新",command=lambda :创建新线程(下载新版本)).pack()
        更新窗口.mainloop()
    else:
        if 是否提示已是最新版本:
            提示("系统提示","目前已是最新版本，无需更新")

def 联系惠惠():
    提示("惠惠QQ","惠惠QQ1621320515")










if __name__ == '__main__':
    tk=tkinter.Tk()
    当前服显示信息=tkinter.Variable()
    当前服显示信息.set(获取当前服(True))
    当前路径=tkinter.Variable()
    当前路径.set(获取路径())
    """---------------------------------  窗口配置  ----------------------------------------"""
    tk.title("原神转服器  持续更新  作者--惠惠  bilibili:是惠惠不是惠惠 QQ群号:788395240")
    tk.geometry("1000x618")
    tk.resizable(False, False)
    tk.iconbitmap("data/图标.ico")
    threading.Thread(target=检查更新).start()
    路径=获取路径()
    """---------------------------------  背景设置  ---------------------------------------------"""
    try:
        背景图片 = tkinter.PhotoImage(file="data/自定义背景图片.png")
    except:
        背景图片 = tkinter.PhotoImage(file="data/背景.png")
    背景=tkinter.Label(tk,image=背景图片).pack()
    """---------------------------------  控件设置  ---------------------------------------------"""
    当前路径显示=tkinter.Label(tk,font=字体大小,textvariable=当前路径, anchor="w")
    当前服显示框 = tkinter.Label(tk, font=字体大小, textvariable=当前服显示信息)
    当前转服器版本显示=tkinter.Label(tk,font=字体大小,text="目前转服器版本:"+open("data/当前转服器版本","r").read(), justify='left')
    路径输入框=tkinter.Entry(tk)
    自动获取路径按钮=tkinter.Button(tk,text="自动获取路径",font=字体大小,command=自动获取路径按钮命令)
    转B服按钮=tkinter.Button(tk,text='B服启动',font=字体大小,command=b服启动)
    转官服按钮=tkinter.Button(tk,text='官服启动',font=字体大小,command=官服启动)
    转国际服按钮=tkinter.Button(tk,text='国际服启动',font=字体大小,command=国际服启动)
    启动按钮=tkinter.Button(tk,text='启动！！！',font=字体大小,command=启动)
    查找原神数量按钮=tkinter.Button(tk,text='查找原神数量',font=字体大小,command=lambda :创建新线程(查找原神数量))
    帮助按钮=tkinter.Button(tk,text='帮助',font=字体大小,command=lambda :创建新线程(帮助命令))
    选择路径按钮 = tkinter.Button(tk, text="选择路径", font=字体大小, command=lambda: 创建新线程(选择路径))
    检查更新按钮=tkinter.Button(tk,text="检查更新",font=字体大小, command=lambda: 创建新线程(检查更新(True)))
    给惠惠打赏按钮=tkinter.Button(tk,text="给惠惠打赏",font=字体大小, command=给惠惠打赏按钮)
    想和惠惠做朋友按钮=tkinter.Button(tk,text="想联系惠惠",font=字体大小, command=联系惠惠)
    更换背景按钮=tkinter.Button(tk,text="更换背景",font=字体大小, command=更换背景)
    """---------------------------------  布局设置  ---------------------------------------------"""
    当前路径显示.place(x=150,y=50,width=800,height=50)
    当前服显示框.place(x=50,y=50,width=100,height=50)
    选择路径按钮.place(x=850, y=50, width=100, height=50)
    """--------------------------------     行配置     -------------------------------------------"""
    第一行=350
    第二行=420
    第三行=490
    第四行=560
    第一个=20
    第二个=270
    第三个=520
    第四个=770
    """--------------------------------     第一行     -------------------------------------------"""
    转B服按钮.place(x=第二个,y=第一行,width=230,height=50)
    转官服按钮.place(x=第一个,y=第一行,width=230,height=50)
    转国际服按钮.place(x=第三个,y=第一行,width=230,height=50)
    查找原神数量按钮.place(x=第四个,y=第一行,width=200,height=50)
    """--------------------------------     第二行     -------------------------------------------"""
    检查更新按钮.place(x=第一个,y=第二行,width=230,height=50)
    给惠惠打赏按钮.place(x=第二个,y=第二行,width=230,height=50)
    帮助按钮.place(x=第四个,y=第二行,width=200,height=50)
    想和惠惠做朋友按钮.place(x=第三个,y=第二行,width=230,height=50)
    """--------------------------------     第三行     -------------------------------------------"""
    更换背景按钮.place(x=第一个,y=第三行,width=230,height=50)

    当前转服器版本显示.place(x=0,y=595)
    """---------------------------------  窗口启动  ---------------------------------------------"""
    tk.mainloop()
