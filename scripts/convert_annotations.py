import os
import json
import cv2

RAW_ANNOTATION_PATH = os.path.join("data","annotations","real")
CONVERTED_ANNOTATION_PATH = os.path.join("data","processed","real")

def conversion_routine(fileLine):
    parts = fileLine.strip().split()
    class_id = parts[0]
    coords = list(map(float, parts[1:]))

    allX = coords[0::2]
    allY = coords[1::2]

    xmin = min(allX)
    xmax = max(allX)
    ymin = min(allY)
    ymax = max(allY)

    centerX = (xmax + xmin) / 2
    centerY = (ymax + ymin) / 2
    width = xmax - xmin
    height = ymax - ymin

    return f"{class_id} {centerX} {centerY} {width} {height}"

def convert_all(annotation_path, converted_path, extension="txt"):
    allFiles = os.listdir(annotation_path)
    for files in allFiles:
        if files.endswith(extension):
            inputPath = os.path.join(annotation_path, files)
            outputPath = os.path.join(converted_path, files)

            with open(inputPath, "r") as file, open(outputPath, "w") as out:
                for line in file:
                    converted = conversion_routine(line)
                    out.write(converted + "\n")

convert_all(RAW_ANNOTATION_PATH, CONVERTED_ANNOTATION_PATH)

