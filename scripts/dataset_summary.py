import os, glob, pandas, cv2

possible_extensions = ["jpg", "png"]
text_extensions = ["txt"]
totalImages = 0

#All Image and Annotations Paths
testRealImg = os.path.join("data", "raw", "test", "images")
testRealAnn = os.path.join("data", "raw", "test", "labels")

trainRealImg = os.path.join("data", "raw", "train", "images")
trainRealAnn = os.path.join("data", "raw", "train", "labels")

validRealImg = os.path.join("data", "raw", "valid", "images")
validRealAnn = os.path.join("data", "raw", "valid", "labels")

#Checking image & annotation compatability
def checkComp(imgPath, annPath):
    resultsCOMP = ["COMPATABILITY CHECK"]
    if len(os.listdir(imgPath)) == len(os.listdir(annPath)):
        resultsCOMP.append("Same number of images and annotations.")
    else:
        resultsCOMP.append("NOT same number of images and annotations.")

    imgBase = sorted([os.path.splitext(f)[0] for f in os.listdir(imgPath) if os.path.isfile(os.path.join(imgPath, f))])
    annBase = sorted([os.path.splitext(f)[0] for f in os.listdir(annPath) if os.path.isfile(os.path.join(annPath, f))])

    if imgBase == annBase:
        resultsCOMP.append("Correct ANNOTATIONS for IMAGES")
    else:
        resultsCOMP.append("Incorrect ANNOTATIONS for IMAGES")

    return resultsCOMP

# Checking Image Corruption Validity
def checkCorr(imgPath):
    resultsCORR = ["CORRUPTION CHECK"]
    corrupted = []
    allImages = [images for images in os.listdir(imgPath) if os.path.isfile(os.path.join(imgPath, images))]
    for img in allImages:
        if cv2.imread(os.path.join(imgPath, img)) is None:
            corrupted.append(img)

    if corrupted:
        resultsCORR.append(f"Corrupted Images : {corrupted}")
    else:
        resultsCORR.append("No corrupted images")

    return resultsCORR

# Checking Image dimension Validity
def checkValImg(imgPath):
    resultsVal = ["IMG SIZE VALIDITY CHECK"]
    invalid = []
    allImages = [images for images in os.listdir(imgPath) if os.path.isfile(os.path.join(imgPath, images))]
    for img in allImages:
        newImg = cv2.imread(os.path.join(imgPath, img))
        height, width = newImg.shape[:2]
        if height > 416 or width > 416 or height <= 0 or width <= 0:
            invalid.append(img)
    
    if invalid:
        resultsVal.append(f"Invalid Images : {invalid}")
    else:
        resultsVal.append("No invalid images")

    return resultsVal

# Checking Annotation file validity
def checkValAnn(annPath):
    resultsValAnn = ["ANNOTATION VALIDITY CHECK"]
    invalid = []
    allAnnotations = [annotations for annotations in os.listdir(annPath) if os.path.isfile(os.path.join(annPath, annotations))]
    for ann in allAnnotations:
        with open(os.path.join(annPath, ann), "r") as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines):
            parts = line.strip().split()
            
            if len(parts) < 7:
                invalid.append([f"File {ann}, Reason : Not enoughs COORDINATES"])
                continue
                
            try:
                classId = int(parts[0])
                coords = list(map(float, parts[1:]))
            except ValueError:
                invalid.append([f"File {ann}, Reason : Not Numeric NUMBER"])
                continue

            if classId < 0 or classId > 12:
                invalid.append([f"File {ann}, Reason : Invalid CLASS"])

            if len(coords) % 2 != 0:
                invalid.append([f"File {ann}, Reason : Not EVEN"])

            xCoords = coords[0::2]
            yCoords = coords[1::2]

            if not all(0 <= x <= 1 for x in xCoords):
                invalid.append([f"File {ann}, Reason : Invalid X COORD"])
            
            if not all(0 <= y <= 1 for y in yCoords):
                invalid.append([f"File {ann}, Reason : Invalid Y COORD"])

    if invalid:
        resultsValAnn.append(invalid)
    else:
        resultsValAnn.append("All Annotations Valid")
    
    return resultsValAnn 

# Checking copies in annotations or images
def checkCop(inpPath):
    resultCOP = ["COPY CHECK"]
    invalid = []
    allFiles = [file for file in os.listdir(inpPath) if os.path.isfile(os.path.join(inpPath, file))]
    for files in allFiles:
        if allFiles.count(files) > 1:
            invalid.append(files)
    
    if invalid:
        resultCOP.append(invalid)
    else:
        resultCOP.append("No Copied Files")
    
    return resultCOP


print(checkComp(validRealImg, validRealAnn))
print(checkCorr(validRealImg))
print(checkValImg(validRealImg))
print(checkValAnn(validRealAnn))
print(checkCop(validRealAnn))
		

						
					
