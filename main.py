import uiautomation as auto
import tkinter.font as tkFont
import tkinter as tk
from time import sleep
import _thread
import random
import os


def gc(obj,whi):
    i = 0
    ob = obj.GetChildren()
    for o in ob:
        i += 1
        if i == whi:
            return o


def tk_move(txt,y):
    w = tk.Tk()
    lam = lambda x:w.destroy()
    #fonta = tkFont.Font(family="微软雅黑", size=12)
    wi = w.winfo_screenwidth() - 155
    hi = w.winfo_screenheight()
    w.wm_attributes("-alpha", 0.4)
    w.wm_attributes("-toolwindow", True)
    w.wm_attributes("-topmost", True)
    w.overrideredirect(True)
    w.bind('<Enter>',lam)
    a = str(len(txt)*18)
    b = str(random.randint(30,500))
    w.geometry(a+"x35+"+str(wi)+"+"+ b)
    l = tk.Label(w,font=('microsoft yahei', 12, 'bold'))
    l.grid()
    l.configure(text=txt.replace('\n', ' '))
    #w.mainloop()
    for i in range(0,w.winfo_screenwidth(),2)[::-1]:
        try:
            w.geometry('+'+str(i)+'+'+ b)
            #print("moving")
            sleep(0.008)
            w.update()
        except:
            print("鼠标移入弹幕或tkinter故障（一般是前者）")
            break
    
def startup():
    print("V0.0.1")
    print("本程序使用Apache License 2.0开源协议")
    print("GitHub项目地址:https://github.com/QLchedan/QQ-message-show")
    print("BUG反馈及改进建议:https://github.com/QLchedan/QQ-message-show/issues/1")
    print("由于使用uiautomation开发，QQ不同版本间结构差异很大，兼容性极差，目前仅支持TIM（QQ的适配在做了！！）")
    print("用法详见README.md")
    print("3s后自动关闭")
    sleep(3)
    os.system("cls")


'''
    def using_mage():
        tmp = [0,0,0]
        tmp1 = []
        qq_win_mag = auto.WindowControl(ClassName='TXGuiFoundation', Name='消息管理器')

        tmp[0] = gc(qq_win_mag.GetChildren(),2)
        tmp[1] = gc(qq_win_mag.GetChildren(),1)
        tmp[2] = gc(qq_win_mag.GetChildren(),2)
        tmp[3] = gc(qq_win_mag.GetChildren(),1)
        tmp[4] = gc(qq_win_mag.GetChildren(),3)
        tmp[5] = gc(qq_win_mag.GetChildren(),1)
        tmp[6] = gc(qq_win_mag.GetChildren(),2)
        tmp[7] = gc(qq_win_mag.GetChildren(),2)

        for t in tmp:
            #tmp1.append(gc)
            pass
        print(tmp)
'''
#!使用消息管理器↑ （暂未开发完成）

startup()
st = input("群名（窗口名）:")
try:
    qq_win = auto.WindowControl(ClassName='TXGuiFoundation', Name=st)
    msg = qq_win.ListItemControl()
except LookupError:
    print("找不到该窗口。若输入无误，请检查窗口是否打开以及界面是否正确。若检查无误，请反馈。（这也有可能是版本问题！）")
    print("将在3s后退出程序")
    sleep(3)
    os._exit()

while True:
    msg1 = qq_win.ListItemControl(searchDepth=15,Name="Cytoid 官方 2 群 （看公告）")
    if msg.GetValuePattern().Value != msg1.GetValuePattern().Value:
        msg = msg1
        print(msg.GetValuePattern().Value)
        _thread.start_new_thread(tk_move,(msg.GetValuePattern().Value,1))
    else:
        pass
      #time.sleep(0.05)
#!普通方法↑（会有部分信息接收不到）


