import os
import sys
import cv2
from glob import glob

file_path = sys.argv[1]
info_name = sys.argv[2]

image_names = glob(os.path.join(file_path, '*'))

with open(info_name, 'w') as  file:
    for index, img in enumerate(image_names):
        img_cv = cv2.imread(img)
        shape = img_cv.shape
        width, height = shape[1], shape[0]
        content = ' '.join([str(index), img, str(width), str(height)])
        file.write(content)
        file.write('\n')
