from pywinauto import application, keyboard
from pywinauto.application import Application
import time
import subprocess
import os
import docx2txt
import tkinter as tk
from tkinter import simpledialog, messagebox

#pip install pywinauto
#pip install docx2txt
#pip install tkintertable
#pip install win32gui

#os.startfile("C:\\Program Files (x86)\\Orange Business Service\\SmartUtil v1.4\\SmartUtil.exe")
#os.startfile("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")

#app = Application(backend="win32").start("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")
#val = app.Properties.testingchild_window(title="edit", auto_id="1001", control_type="Edit")

"""time.sleep(5)
keyboard.send_keys('testing6')
keyboard.send_keys("{TAB 1}")
keyboard.send_keys("{ENTER}")"""

#code to open a txt file read the content and store in list.
#f = open("C:\\Users\\moham\\Desktop\\FGBBDATA-9-001.docx","r")
#content = f.read()
#my_text = docx2txt.process("C:\\Users\\moham\\Desktop\\FGBBDATA-9-001 (1).txt")

application_window = tk.Tk()
app = application.Application()

def Start_Automate():    
    content = simpledialog.askstring("Input", "What is your first name?",parent=application_window)
    if content != None:
        MultiSpace = ["               ", "              ", "             ", "            ", "           ", "          ", "         ", "        ", "       ", "      ","     ","    ","   ","  "]

        while "  " in content:
            for i in MultiSpace:
                content = content.replace(i,"\t")

        content = content.replace("\n", " ")        
        Contant_Lst = content.split("	")
        print(Contant_Lst)
        print(len(Contant_Lst))
        app.start("C:\\Program Files (x86)\\Lenovo\\SHAREit\\Shareit.exe")
        app.window()
        Start_Automate()
    else:
        messagebox.showinfo("Information","Automation has stopped, Thank You")


"""time.sleep(5)

k=0
for i in range(40):
    keyboard.send_keys(Contant_Lst[k])
    keyboard.send_keys("{TAB 1}")
    k += 1
"""

Start_Automate()