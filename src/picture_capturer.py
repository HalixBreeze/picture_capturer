# -*- coding: utf-8 -*-
"""
Name: Picture Capturer
Description: 使用網路爬蟲來抓取網頁上的圖片

Version: v1.0
Date: 2017-10-01
Author: Felix Breeze
Changed Items:
    1. Add an app_gui file, which has a git class.
    2. Modify this main file, let it run with GUI.

Version: v1.1
Date: 2018-01-01
Author: Felix Breeze
Changed Items: (not yet to do)
    1. When downloading was completed, change work directory to upper one.
    2. Show the downloading message on the interface.
    3. Beautify the interface.
"""

import requests
from bs4 import BeautifulSoup
import shutil
import os
import tkinter as tk
import app_gui # 引用我的GUI類別

# 用來下載圖片的方法
def downloadPictures(event, app, directory='./'):
    os.chdir(directory)

    url = app.url_input.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pic_num = 0 # 用來計算總共抓了幾張圖

    # 取得網頁的標題當作是資料夾的名稱
    pics_title = soup.title.string.encode('latin1', 'ignore').decode('big5').replace('\n', '')
    showMsgOnApp(app, pics_title)

    # 以資料夾名稱來建立圖片下載的資料夾，並切換到該資料夾底下
    os.mkdir(pics_title)
    os.chdir(pics_title)

    showMsgOnApp(app, '圖片抓取中...')

    for img in soup.select('img'): # 取得網頁內所有img元素
        img_src = img['src']
        img_src_no_parameter = img['src'].split('?')[0] # 將原來的scr去掉參數
        img_name = img_src_no_parameter.split('/')[-1] # 取得圖片的名稱

        # 假如img檔名為jpg，就將其抓取下來
        try:
            if img_name[-3:] == 'jpg':
                print(img_name) # 測試用，用來確認下載的檔案

                img_stream = requests.get(img_src, stream = True)
                with open(img_name, 'wb') as img_file:
                    shutil.copyfileobj(img_stream.raw, img_file) # 將網頁圖片的資料串流複製到本地檔案串流
                pic_num += 1

                del img_stream
        except Exception as ex:
            showMsgOnApp(app, ex)
        
    showMsgOnApp(app, '總共' + str(pic_num) + '張圖片，抓取完成!!')
    app.url_input.delete(0, 'end')
    os.chdir('../')

# 用來顯示目前下載的狀況
def showMsgOnApp(app, msg):
    app.status_viewer.insert('end', msg)
    print(msg)

root = tk.Tk()
app = app_gui.AppGUI(root)
app.ok_btn.bind('<Button-1>', lambda event: downloadPictures(event, app))

app.mainloop()