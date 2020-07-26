import sys
import os
import shutil

# train2017 8899  ls -l |grep "^-"|wc -l
# val2017 2309
# fileList = '/home/zhangchunmei/DarrenZhang/yolov5/VOCdevkit/VOC2007/2007_test.txt'
# targetDir = '/home/zhangchunmei/DarrenZhang/yolov5/coco/images/val2017'

# filedir = open(fileList)
# line = filedir.readline()
# i = 0

# while line:
#     line = line.strip('\n')
#     print(line)
#     shutil.copy(line, targetDir)
#     i += 1
#     line = filedir.readline()
# print(i)


# copy labels
BaseDir = '/home/zhangchunmei/DarrenZhang/yolov5/VOCdevkit/VOC2007/labels/'
fileList = '/home/zhangchunmei/DarrenZhang/yolov5/VOCdevkit/VOC2007/ImageSets/Main/test.txt'
targetDir = '/home/zhangchunmei/DarrenZhang/yolov5/coco/labels/val2017'

filedir = open(fileList)
line = filedir.readline()
i = 0

while line:
    line = str(line.strip('\n')) + '.txt'
    file = os.path.join(BaseDir, line)
    print(file)
    shutil.copy(file, targetDir)
    i += 1
    line = filedir.readline()
print(i)
