from pywinauto import application, keyboard
from pywinauto.application import Application
import time
import subprocess
import os
import PyPDF2
import docx2txt

#os.startfile("C:\\Program Files (x86)\\Orange Business Service\\SmartUtil v1.4\\SmartUtil.exe")
#os.startfile("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")

#app = Application(backend="win32").start("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")
#val = app.Properties.testingchild_window(title="edit", auto_id="1001", control_type="Edit")

#app = Application(backend="win32").start("C:\\Program Files (x86)\\Orange Business Service\\SmartUtil v1.4\\SmartUtil.exe")
#val = app.Properties.child_window(title="edit", auto_id="txtGetPOResponse", control_type="TextBox")

#code to enter password
#time.sleep(3)
#keyboard.send_keys('testing2')

"""time.sleep(5)
keyboard.send_keys('testing')
keyboard.send_keys("{TAB 1}")
keyboard.send_keys('testing2')
keyboard.send_keys("{TAB 1}")
keyboard.send_keys('testing3')
keyboard.send_keys("{TAB 1}")
keyboard.send_keys('testing4')
keyboard.send_keys("{TAB 1}")
keyboard.send_keys('testing5')
keyboard.send_keys("{TAB 1}")
keyboard.send_keys('testing6')
keyboard.send_keys("{TAB 2}")
keyboard.send_keys("{ENTER}")"""

#code to open a txt file read the content and store in list. (pip install docx2txt)
'''f = open("C:\\Users\\FU148MYQ\\Downloads\\FGBBDATA-9-001.docx","r")
content = f.read()
Contant_Lst = []
Contant_Lst = content.split("	")
print(Contant_Lst)
print(len(Contant_Lst))'''

my_text = docx2txt.process("C:\\Users\\FU148MYQ\\Downloads\\FGBBDATA-9-001.docx")
Contant_Lst = my_text.split("	")
#print(Contant_Lst)

if Contant_Lst[0] == '134014':
    print('Correct Data')

for i in range(40):
    NewData = Contant_Lst[i]

print(NewData)
