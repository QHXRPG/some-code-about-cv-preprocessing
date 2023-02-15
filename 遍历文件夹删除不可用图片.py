import os
import cv2
from glob import glob
file = '/Users/qiuhaoxuan/Downloads/images1-4/train'
i=0
for root, dirs, files in os.walk(file):
    for file in files:
        path = os.path.join(root, file)
        print(path)
        images = glob(path)
        for image in images:
            i=i+1
            img = cv2.imread(image)
            if i % 2==0:
                print(image)
                os.remove(image)