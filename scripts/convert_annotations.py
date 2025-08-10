import os
import json
import cv2

RAW_ANNOTATION_PATH = os.path.join("data","annotations","raw")
CONVERTED_ANNOTATION_PATH = os.path.join("data","annotations","converted")

def convertFiles(x_min, x_max, image_width, y_min, y_max, image_height):
	#YOLO FORMAT = id, centerx, centery, width, height
	imageXCent = (x_min + x_max) / 2.0  / image_width
	imageYCent = (y_min + y_max) / 2.0 / image_height
	return imageXCent, imageYCent, image_width, image_height


def process_path(json_path, output_path, img_width, img_height):
	
	with open(json_path, "r") as f:
		data = json.load(f)
		
	with open(output_path, "w") as out:
		for obj in data['objects']:
			class_id = obj['class_id']
			x_min, y_min = obj['bbox'][0], obj['bbox'][1]
			x_max, y_max = obj['bbox'][2], obj['bbox'][3]

			x, y, w, h = convertFiles(x_min, x_max, img_width, y_min, y_max, img_height)
			out.write(f"{class_id} {x} {y} {w} {h}\n")


for files in os.listdir(RAW_ANNOTATION_PATH):
	if not files.endswith(".json"):
		continue

	else:
		json_path = os.path.join(RAW_ANNOTATION_PATH, files)
		output_path = os.path.join(CONVERTED_ANNOTATION_PATH, files.replace(".json", ".txt"))
		
		image_path = os.path.join("data/raw/real", files.replace(".json", ".jpg"))
		img = cv2.imread(image_path)
		h, w = img.shape[:2]

		process_path(json_path, output_path, w, h)

	