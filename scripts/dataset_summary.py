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

# Checking copies in annotations or images

print(checkComp(testRealImg, testRealAnn))
print(checkCorr(testRealImg))
print(checkValImg(testRealImg))
		

						
					
