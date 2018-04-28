import fileinput
import glob

file_list = glob.glob("*.txt")
print file_list
with open('result.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)