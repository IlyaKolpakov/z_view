import csv

txt_file = r"sol 1 [1] copy.txt"
csv_file = r"mycsv.csv"

With open("sol 1 [1] copy.txt","rb") as f:
    reader=csv.reader(f)
    for row in reader
        print row

#With open("sol 1 [1] copy.txt", "rb") as f:
#reader = csv.reader(f)
#for row in reader:
#print row
# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
in_txt = csv.reader(open(txt_file, "rb"), delimiter = '/')
#print in_txt
#out_csv = csv.writer(open(csv_file, 'wb'))

#out_csv.writerows(in_txt)
