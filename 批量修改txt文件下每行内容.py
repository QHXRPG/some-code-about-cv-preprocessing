import os
import glob
seq_dir = os.path.expanduser('/Users/qiuhaoxuan/Downloads/images1-4/images-part1/labels/BoLuo/')
files=glob.glob(seq_dir + '*.txt')
for f, file in enumerate(files):


    readfile = open(file, 'r') #读取文件
    fline = readfile.readlines() #读取txt文件中每一行
    savetxt = open(file, 'w')

    for j in fline:
        s ='34'+ j[1:]
        savetxt.write(s) #写入新的文件中

