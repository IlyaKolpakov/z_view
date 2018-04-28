import os
import shutil
import glob
from Tkinter import *
import tkFileDialog
import numpy as np
save_path="zview/"
qumark = "'"
dir = 'zview'
root = Tk()
if not os.path.exists(dir):
    os.makedirs(dir)
else:
    shutil.rmtree(dir)           #removes all the subdirectories!
    os.makedirs(dir)

def openfile():
    file = tkFileDialog.askdirectory() # Tkinter open file

    for filename in glob.glob(os.path.join(file,'*.txt')):
        filename_cut=os.path.basename(filename)
        print filename_cut
        data = np.loadtxt(filename_cut, dtype=np.str, skiprows=1, delimiter=';')
        print data



Button(text='Open file', command=openfile).pack(fill=X)

root.mainloop()