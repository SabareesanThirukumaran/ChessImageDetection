import os
import json
import cv2

RAW_ANNOTATION_PATH = os.path.join("data","annotations","real")
CONVERTED_ANNOTATION_PATH = os.path.join("data","processed","real")

allX = [x1, x2, x3, x4]
allY = [y1, y2, y3, y4]

xmin = min(allX)
xmax = max(allX)
ymin = min(allY)
ymax = max(allY)

centerX = (xmax + xmin) / 2
centerY = (ymax + ymin) / 2
width = xmax - xmin
height = ymax - ymin

