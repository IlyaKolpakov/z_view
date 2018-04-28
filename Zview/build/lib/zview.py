#! /usr/bin/env python
import os
import shutil
import glob
from Tkinter import *
import tkFileDialog
import numpy as np

save_path="zview"
qumark = "'"
#dir = "/zview"
root = Tk()
#print os.path

def openfile():
    file = tkFileDialog.askdirectory() # Tkinter open file

    dir = os.path.join(file, save_path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        shutil.rmtree(dir)  # removes all the subdirectories!
        os.makedirs(dir)

    for filename in glob.glob(os.path.join(file,"*.txt")):

        data = np.loadtxt(filename, dtype=np.str, skiprows=1)
        if len(data[1])==8 :
            data = np.loadtxt(filename, dtype=np.str, skiprows=1)
        else:
            data = np.loadtxt(filename, dtype=np.str, skiprows=1,delimiter=';')
        l=len(data[1])

        while True:
            if l==8 :
                #print "we are cool"
                size= len(data[:, 2])
                mat = np.zeros((size, 9))
                z_prime = np.copy(data[:, 1])
                z_dprime = np.copy(data[:, 2]).astype(np.float)
                #print type(data[:, 2])
                #print z_dprime[9]>0
                if z_dprime.any>0:
                    z_dprime=-z_dprime
                else:
                    z_dprime=z_dprime
                #if z_dprime.any() >0:
                #    print "Trues"
                #else:
                #    print "False"
                #print (z_dprime > 0).all()
                # and (a < 0).all()

                #if z_dprime < 0:
                    #z_dprime = z_dprime.astype(object)
                    #z_dprime = "-" + z_dprime
                #else:
                    #z_dprime= z_dprime
                #    print "negative"
                #"-"
                freq = np.copy(data[:, 0])
                data[:, 0] = mat[:, 0]
                data[:, 1] = mat[:, 4]
                data[:, 2] = mat[:, 5]

                mat[:, 0] = freq
                mat[:, 4] = z_prime
                mat[:, 5] = z_dprime

                filename1 = "Z view appendix " + os.path.basename(filename)
                filename2 = "Z view data " + os.path.basename(filename)

                cm = os.path.join(os.path.dirname(filename), save_path)
                completeName = os.path.join(cm, os.path.basename(filename))

                cm1 = os.path.join(os.path.dirname(filename), save_path)
                completeName1 = os.path.join(cm1, filename1)

                cm2 = os.path.join(os.path.dirname(filename), save_path)
                completeName2 = os.path.join(cm2, filename2)

                with open(completeName1, 'w') as f:

                    f.write('"Z60W Data File: Version 1.1" \n' + '"" \n'
                            + '"" \n' + '"" \n' + '"" \n' + '"" \n' + '"" \n' + '"" \n'
                            + '0.2.0.1.1.100000 \n' + '150\n' +  "' Freq (Hz) Ampl Time(Sec); Z'(a) Z''(b) GD Err Range '" +' \n')
                    f.close()
                    np.savetxt(completeName2, mat, fmt='%.5f', newline=os.linesep)

                    filenames = [completeName1, completeName2]
                    for fm in glob.glob('*.txt'):
                        fm = os.path.basename(fm)
                        with open(completeName, 'w') as outfile:

                            for fm in filenames:
                                with open(fm) as infile:

                                    outfile.write(infile.read())

                os.remove(completeName1)
                os.remove(completeName2)
                break
            else:

                size = len(data[:, 2])
                #print "new version of autolab"
                mat = np.zeros((size, 9))
                z_prime = np.copy(data[:, 2])
                z_dprime = np.copy(data[:, 3]).astype(np.float)
                #z_dprime = z_dprime.astype(object)
                #z_dprime= "-" + z_dprime
                if z_dprime.any>0:
                    z_dprime=-z_dprime
                else:
                    z_dprime=z_dprime
                #print z_dprime
                freq = np.copy(data[:, 1])
                data[:, 1] = mat[:, 0]
                data[:, 2] = mat[:, 4]
                data[:, 3] = mat[:, 5]

                mat[:, 0] = freq
                mat[:, 4] = z_prime
                mat[:, 5] = z_dprime

                filename1 = "Z view appendix " + os.path.basename(filename)
                filename2 = "Z view data " + os.path.basename(filename)

                cm = os.path.join(os.path.dirname(filename), save_path)
                completeName = os.path.join(cm, os.path.basename(filename))

                cm1 = os.path.join(os.path.dirname(filename), save_path)
                completeName1 = os.path.join(cm1, filename1)

                cm2 = os.path.join(os.path.dirname(filename), save_path)
                completeName2 = os.path.join(cm2, filename2)

                with open(completeName1, 'w') as f:

                    f.write('"Z60W Data File: Version 1.1" \n' + '"" \n'
                            + '"" \n' + '"" \n' + '"" \n' + '"" \n' + '"" \n' + '"" \n'
                            + '0.2.0.1.1.100000 \n' + '150\n' + "Freq (Hz) Ampl Time(Sec); Z'(a) Z''(b) GD Err Range \n")
                    f.close()
                    np.savetxt(completeName2, mat, fmt='%.5f', newline=os.linesep)

                    filenames = [completeName1, completeName2]
                    for fm in glob.glob('*.txt'):
                        fm = os.path.basename(fm)
                        with open(completeName, 'w') as outfile:

                            for fm in filenames:
                                with open(fm) as infile:

                                    outfile.write(infile.read())

                os.remove(completeName1)
                os.remove(completeName2)
                break

            break


Button(text='Open file', command=openfile).pack(fill=X)

root.mainloop()