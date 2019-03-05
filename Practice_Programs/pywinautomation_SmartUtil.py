from pywinauto import application
from pywinauto.application import Application
import time
import subprocess
import os

#os.startfile("C:\\Program Files (x86)\\Orange Business Service\\SmartUtil v1.4\\SmartUtil.exe")

#os.startfile("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")
#app = Application(backend="uia").start("C:\\Program Files (x86)\\Orange Business Service\\SmartUtil v1.4\\SmartUtil.exe")
app = Application(backend="win32").start("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")
val = app.Properties.child_window(title="edit", auto_id="1001", control_type="Edit")
print(val)
app.Properties.print_control_identifiers()