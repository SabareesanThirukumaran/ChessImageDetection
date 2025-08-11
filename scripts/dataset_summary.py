import os, glob, pandas, cv2

possible_extensions = ["jpg", "png"]
totalImages = 0

#All Real Image Path
realImages_fullPath = os.path.join("data","raw","real")
image_paths_real = []
if os.path.exists(realImages_fullPath):

    for ext in possible_extensions:
        image_paths_real.extend(glob.glob(os.path.join(realImages_fullPath, f"*.{ext}")))

    fullRealFiles = len([path for path in os.listdir(realImages_fullPath) if os.path.isfile(os.path.join(realImages_fullPath, path))])
    countReal = len(image_paths_real)

    if fullRealFiles == countReal:
        totalImages += countReal

# All Image Count
    
#Checking image & annotation compatability
RealannotationPath = os.path.join("data","annotations","real")
VirtualannotationPath = os.path.join("data","annotations","virtual")

if len(os.listdir(RealannotationPath)) == countReal:
    count = 0
    
    # Checking all REAL compatability
    real_image_basenames = set(os.path.splitext(f)[0] for f in os.listdir(realImages_fullPath) if os.path.isfile(os.path.join(realImages_fullPath, f)))
    real_annotations_basenames = set(os.path.splitext(f)[0] for f in os.listdir(RealannotationPath) if os.path.isfile(os.path.join(RealannotationPath, f)))

    if real_image_basenames == real_annotations_basenames:
        print("All REAL annotations are in equal to Images")
    else:
        print("There is a mismatch (REAL)")

# Checking Image Corruption Validity

def checkImageCorruption(path):
    return cv2.imread(path) is None

print([checkImageCorruption(os.path.join(realImages_fullPath, f)) for f in os.listdir(realImages_fullPath)])

# 1 - Real Images
realCorruptionCount = 0
for images in os.listdir(realImages_fullPath):
    fullImagePath = os.path.join(realImages_fullPath,images)
    if checkImageCorruption(fullImagePath):
        print(f"{fullImagePath} is corrupted.")
        realCorruptionCount += 1

if realCorruptionCount == 0:
    print("All Images are NOT corrupted")

# Checking Image dimension Validity

def checkImageSize(path):
    img = cv2.imread(path)
    height, width = img.shape[:2]
    return width <= 0 or height <= 0 or width > 416 or height > 416

imageSizeFails = [checkImageSize(os.path.join(realImages_fullPath, f)) for f in os.listdir(realImages_fullPath)]
print(imageSizeFails)

# Checking Annotation file validity

def checkAnnotationFile(annotations_folder, annotations_basenames, extension="txt"):
    for files in annotations_basenames:
        filename = files + "." + extension
        full_path = os.path.join(annotations_folder, filename)

        if not os.path.exists(full_path):
            return f"{filename} does not exist."
        
        with open(full_path, "r") as f:  # Use full path here
            lines = f.readlines()

            if len(lines) == 0:
                return f"No lines in file {filename}"

            for i, line in enumerate(lines):
                parts = line.strip().split()
                if len(parts) != 5:
                    return f"Annotation file is not full in {filename} line {i+1}"

                try:
                    class_id = int(parts[0])
                except ValueError:
                    return f"Class id is not an integer in {filename} line {i+1}"

                try:
                    dimensions = [float(d) for d in parts[1:]]
                except ValueError:
                    return f"One or more dimensions are not correct in {filename} line {i+1}"

                if any(d < 0 or d > 1 for d in dimensions):
                    return f"Dimensions are out of bounds in {filename} line {i+1}"

    return "All annotation files are valid"
				
annotationCheck = [checkAnnotationFile(RealannotationPath, real_annotations_basenames, extension="txt")]
print(annotationCheck)



# Checking copies in annotations or images

def checkCopies(pathway):
	allFiles = os.listdir(pathway)
	if set(allFiles) == allFiles:
		return "No files are copied"

	else:
		copies = []
		for files in allFiles:
			if allFiles.count(files) > 1:
				copies.append(files)
		return f"{copies} are copied"



		

						
					
