from pywinauto import application, keyboard
from pywinauto.application import Application
import time
import subprocess
import os
import docx2txt
import tkinter as tk
from tkinter import simpledialog, messagebox
import sys

#pip install pywinauto
#pip install docx2txt
#pip install tkintertable
#pip install win32gui

#os.startfile("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")

#app = Application(backend="win32").start("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")
#val = app.Properties.testingchild_window(title="edit", auto_id="1001", control_type="Edit")

#code to open a txt file read the content and store in list.
#f = open("C:\\Users\\moham\\Desktop\\FGBBDATA-9-001.docx","r")
#content = f.read()

#my_text = docx2txt.process("C:\\Users\\moham\\Desktop\\FGBBDATA-9-001 (1).txt")

application_window = tk.Tk()
app = application.Application()

def Start_Automate():    
    content = simpledialog.askstring("Input", "Enter you Data here",parent=application_window)
    if content != None:
        MultiSpace = ["               ", "              ", "             ", "            ", "           ", "          ", "         ", "        ", "       ", "      ","     ","    ","   ","  "]

        while "  " in content:
            for i in MultiSpace:
                content = content.replace(i,"\t")

        while " " in content:
            content = content.replace(" ","{SPACE}") 

        content = content.replace("\n", " ")       

        Specialchar = ['(', ')', '/', '-']
        for i in Specialchar:
            content = content.replace(i, "{" + i + "}")
        
        Contant_Lst = content.split("	")
        
        Contant_Lst = [x for x in Contant_Lst if x]

        if len(Contant_Lst) != 40:
            messagebox.showerror("Error","Please Check the data entered as the splitted data does not have 40 feilds")
        else:       
            #app.start("C:\\Program Files (x86)\\Orange Business Service\\SmartUtil v1.4\\SmartUtil.exe")
            #app.window()

            time.sleep(5)
            k=0
            for i in range(40):
                keyboard.send_keys(Contant_Lst[k])
                keyboard.send_keys("{TAB 1}")
                k += 1

        Start_Automate()
    else:
        messagebox.showinfo("Information","Automation Tool has stopped, Thank You")


"""time.sleep(5)

k=0
for i in range(40):
    keyboard.send_keys(Contant_Lst[k])
    keyboard.send_keys("{TAB 1}")
    k += 1
"""

Start_Automate()