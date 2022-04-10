import pyautogui as auto
import time
import os

def print_qr_for_me(item_code,item_name,item_rate,print_nos):
        product_code = item_code
        item_name = item_name
        price = item_rate
        nos = print_nos
        os.system("taskkill /f /im glabels-qt.exe")
        time.sleep(1)
        os.startfile("retail.glabels")
        # auto.rightClick(73,751)
        # time.sleep(2)
        # auto.click(76,630)
        # auto.hotkey("win","1")
        time.sleep(4)
        auto.click(393, 443)
        time.sleep(0.5)
        auto.click(507,333)
        time.sleep(0.25)
        auto.click(575,722)
        time.sleep(0.35)
        auto.tripleClick(771,399)
        auto.write(item_name)
        auto.hotkey("enter")
        time.sleep(0.5)
        auto.click(510,313)
        auto.click(575,722)
        time.sleep(0.35)
        auto.tripleClick(771,399)
        auto.write(product_code)
        auto.hotkey("enter")
        time.sleep(0.5)
        auto.click(490,274)
        auto.click(575,722)
        time.sleep(0.35)
        auto.tripleClick(771,399)
        auto.write(str(price))
        auto.hotkey("enter")
        auto.click(395, 512)
        time.sleep(0.5)
        auto.tripleClick(540,270)
        prints = int(nos)
        nose = round((int(prints)/2)/10*10)
        auto.write(str(nose))
        check = auto.confirm(text="Printing Order await",title="Do You Want to Print?",buttons=['OK','CANCEL'])
        if check == "OK":
            time.sleep(0.5)
            auto.click(526,462)
            time.sleep(1.50)
            auto.tripleClick(483,228)
            time.sleep(1)
            os.system("taskkill /f /im glabels-qt.exe")
        else:
            pass