# -*- coding: utf-8 -*-
"""
這個檔案是用來產生程式所需要用到的GUI
"""
import tkinter as tk

class AppGUI(tk.Frame):
    def __init__(self, master=None):
        master.minsize(500, 400)
        master.resizable(False, False)
        super().__init__(master)
        self.pack(fill='both', expand=True) # 將這個frame放到parent widget中
        self.createWidgets() # 建立在這個frame中的widget 

    def createWidgets(self):
        self.url_title = tk.Label(self, text='請輸入來源網址：')
        self.url_title.config(font=(16))
        self.url_title.pack()

        self.url_input = tk.Entry(self)
        self.url_input.config(font=(16))
        self.url_input.pack(fill='x')
        
        self.ok_btn = tk.Button(self, text='確認', fg='blue')
        self.ok_btn.config(font=(16))
        self.ok_btn.pack()

        self.status_viewer= tk.Listbox(self)
        self.status_viewer.config(font=(16))
        self.status_viewer.pack(fill='both', expand=True)