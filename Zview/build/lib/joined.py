import os
import shutil
import glob
from Tkinter import *
import tkFileDialog
import numpy as np

save_path="zview"
qumark = "'"
dir = "/zview"
root = Tk()
print os.path
#if not os.path.exists(dir):
#    os.makedirs(dir)
#else:
#    shutil.rmtree(dir)  # removes all the subdirectories!
#    os.makedirs(dir)



def openfile():
    file = tkFileDialog.askdirectory() # Tkinter open file
    print file
    a=os.path.join(file, save_path)
    os.makedirs(a)
    for filename in glob.glob(os.path.join(file,"*.txt")):
        #os.makedirs(os.path.join(os.path.dirname(filename),dir))
        data = np.loadtxt(filename, dtype=np.str, skiprows=1)
        if len(data[1])==8 :
            data = np.loadtxt(filename, dtype=np.str, skiprows=1)
        else:
            data = np.loadtxt(filename, dtype=np.str, skiprows=1,delimiter=';')
        l=len(data[1])
        #print l
        while True:
            if l==8 :
                print "we are cool"
                size= len(data[:, 2])
                mat = np.zeros((size, 9))
                z_prime = np.copy(data[:, 1])
                z_dprime = np.copy(data[:, 2])

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
                # completeName = os.path.join(save_path,os.path.basename(filename))
                # completeName1 = os.path.join(save_path,filename1)
                # completeName2 = os.path.join(save_path,filename2)
                #print completeName1
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
                            # print completeName
                            for fm in filenames:
                                with open(fm) as infile:
                                    #print fm
                                    outfile.write(infile.read())

                os.remove(completeName1)
                os.remove(completeName2)
                break
            else:
                #print data
                size = len(data[:, 2])
                print "new version of autolab"
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

                cm = os.path.join(os.path.dirname(filename), save_path)
                completeName = os.path.join(cm, os.path.basename(filename))

                cm1 = os.path.join(os.path.dirname(filename), save_path)
                completeName1 = os.path.join(cm1, filename1)

                cm2 = os.path.join(os.path.dirname(filename), save_path)
                completeName2 = os.path.join(cm2, filename2)
                # completeName = os.path.join(save_path,os.path.basename(filename))
                # completeName1 = os.path.join(save_path,filename1)
                # completeName2 = os.path.join(save_path,filename2)
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
                            # print completeName
                            for fm in filenames:
                                with open(fm) as infile:
                                    #print fm
                                    outfile.write(infile.read())

                os.remove(completeName1)
                os.remove(completeName2)
                break

            break


Button(text='Open file', command=openfile).pack(fill=X)

root.mainloop()