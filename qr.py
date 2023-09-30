import pyqrcode 
import os
import shutil
title=input("Enter title for QRCode : ")
text=input("what does the QRCode have to say? : ")
file_name_svg=title+".svg"
file_name_png=title+".png"
py=pyqrcode.create(text)

py.svg(file_name_svg,scale=8)
py.png(file_name_png,scale=10)
os.makedirs(f"./QRs/")

shutil.move(file_name_svg,"./QRs/")
shutil.move(file_name_png,"./QRs/")
