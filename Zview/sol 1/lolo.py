import glob
import numpy as np
import os
#import shutil
save_path="zview/"
qumark = "'"
for filename in glob.glob('*.txt'):
    data = np.loadtxt(filename, dtype=np.str, skiprows=1,delimiter=';')
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

    filename1= "Z view appendix " + filename
    filename2 = "Z view data " + filename
    completeName= os.path.join(save_path, filename)
    completeName1 = os.path.join(save_path, filename1)
    completeName2 = os.path.join(save_path, filename2)
    #print completeName
    with open(completeName1, 'w') as f:
    #
    #     #f.seek(0,0)
    #     #header = '"  Freq (Hz)', 'Ampl', 'Time(Sec);', 'Z' + qumark + '(a);', 'Z' + qumark * 2 + '(b);', 'GD;', 'Err;','Range;'
         f.write('"Z60W Data File: Version 1.1" \n' + '"" \n' + '"" \n'
                 + '"" \n' + '"" \n' + '"" \n' +
                 '"" \n'  + '"" \n'+'0.2.0.1.1.100000 \n'+ '150\n'
                 +"Freq (Hz) Ampl Time(Sec); Z'(a) Z''(b) GD Err Range \n")+
                'Z' + qumark * 2 + '(b);', 'GD;', 'Err;','Range;')

    #
    #     f.close()
    #
    #     np.savetxt(completeName2, mat, fmt='%.5f', newline=os.linesep)
    #
    #     filenames = [completeName1,completeName2]
    #     for filename in glob.glob('*.txt'):
    #
    #         with open(completeName, 'w') as outfile:
    #                 for fname in filenames:
    #
    #                     with open(fname) as infile:
    #                         outfile.write(infile.read())
    #     print fname
    #     #os.remove(filename2)
    # #os.remove(fname)                      #os.remove("zview/"+filename1)