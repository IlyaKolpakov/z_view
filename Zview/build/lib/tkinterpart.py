import os
import shutil
import glob
from Tkinter import *
import tkFileDialog
import numpy as np

save_path="zview/"
qumark = "'"
dir = "zview"
root = Tk()

#if not os.path.exists(os.path.join(file, dir)):
#    os.makedirs(os.path.join(file, dir))

#else:
#    shutil.rmtree(os.path.join(file, dir))  # removes all the subdirectories!
#    os.makedirs(os.path.join(file, dir))


def openfile():
    file = tkFileDialog.askdirectory() # Tkinter open file
    #print file
    for filename in glob.glob(os.path.join(file,"*.txt")):


        str=filename
        zview_path= os.path.basename(
            os.path.dirname(filename))



        data = np.loadtxt(filename, dtype=np.str, skiprows=1, delimiter=';')

        size = len(data[:, 2])

        mat = np.zeros((size, 9))
        z_prime = np.copy(data[:, 2])
        z_dprime = np.copy(data[:, 3])
        freq = np.copy(data[:, 1])
        data[:, 1] = mat[:, 0]
        data[:, 2] = mat[:, 4]
        data[:, 3] = mat[:, 5]

        mat[:, 0] = freq
        mat[:, 4] = z_prime
        mat[:, 5] = z_dprime

        filename1 = "Z view appendix " + os.path.basename(filename)
        filename2 = "Z view data " + os.path.basename(filename)

        cm=os.path.join(os.path.dirname(filename),save_path)
        completeName=os.path.join(cm,os.path.basename(filename))

        cm1=os.path.join(os.path.dirname(filename),save_path)
        completeName1=os.path.join(cm1,filename1)

        cm2=os.path.join(os.path.dirname(filename),save_path)
        completeName2=os.path.join(cm2,filename2)
        #completeName = os.path.join(save_path,os.path.basename(filename))
        #completeName1 = os.path.join(save_path,filename1)
        #completeName2 = os.path.join(save_path,filename2)

        with open(completeName1,'w') as f:
            if not os.path.exists(dir):
                os.makedirs(dir)
            else:
                shutil.rmtree(dir)  # removes all the subdirectories!
                os.makedirs(dir)
            f.write('"Z60W Data File: Version 1.1" \n' + '"" \n'
                    + '"" \n' + '"" \n' + '"" \n' + '"" \n' + '"" \n' + '"" \n'
                    + '0.2.0.1.1.100000 \n' + '150\n' + "Freq (Hz) Ampl Time(Sec); Z'(a) Z''(b) GD Err Range \n")
            f.close()

            np.savetxt(completeName2, mat, fmt='%.5f', newline=os.linesep)

            filenames = [completeName1, completeName2]
            for fm in glob.glob('*.txt'):
                fm=os.path.basename(fm)
                with open(completeName, 'w') as outfile:
            #print completeName
                    for fm in filenames:
                        with open(fm) as infile:
                            print fm
                            outfile.write(infile.read())

            os.remove(completeName1)
            os.remove(completeName2)

Button(text='Open file', command=openfile).pack(fill=X)

root.mainloop()
