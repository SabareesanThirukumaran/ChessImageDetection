import os, glob, pandas, cv2

possibly_extensions = ["jpg", "png"]
totalImages = 0

#All Virtual Image Paths
virtualImages_fullPath = os.path.join("data","raw","virtual") 
image_paths_virtual = []
if os.path.exists(virtualImages_fullPath):

    for ext in possibly_extensions:
        image_paths_virtual.extend(glob.glob(os.path.join(virtualImages_fullPath, f"*.{ext}")))

    fullVirtualFiles = len([path for path in os.listdir(virtualImages_fullPath) if os.path.isfile(os.path.join(virtualImages_fullPath, path))])
    countVirtual = len(image_paths_virtual)

    if fullVirtualFiles == countVirtual:
        totalImages += countVirtual

#All Real Image Path
realImages_fullPath = os.path.join("data","raw","real")
image_paths_real = []
if os.path.exists(realImages_fullPath):

    for ext in possibly_extensions:
        image_paths_real.extend(glob.glob(os.path.join(realImages_fullPath, f"*.{ext}")))

    fullRealFiles = len([path for path in os.listdir(realImages_fullPath) if os.path.isfile(os.path.join(realImages_fullPath, path))])
    countReal = len(image_paths_real)

    if fullRealFiles == countReal:
        totalImages += countReal

# All Image Count
if totalImages == 300:
    
    #Checking image & annotation compatability
    RealannotationPath = os.path.join("data","annotations","real")
    VirtualannotationPath = os.path.join("data","annotations","virtual")

    if len(os.listdir(RealannotationPath)) == countReal and len(os.listdir(VirtualannotationPath)) == countVirtual:
        count = 0
        
        # Checking all REAL compatability
        real_image_basenames = set(os.path.splitext(f)[0] for f in os.listdir(realImages_fullPath) if os.path.isfile(os.path.join(realImages_fullPath, f)))
        real_annotations_basenames = set(os.path.splitext(f)[0] for f in os.listdir(RealannotationPath) if os.path.isfile(os.path.join(RealannotationPath, f)))

        if real_image_basenames == real_annotations_basenames:
            print("All REAL annotations are in equal to Images")
        else:
            print("There is a mismatch (REAL)")

        # Checking all VIRTUAL compatability
        virtual_image_basenames = set(os.path.splitext(f)[0] for f in os.listdir(virtualImages_fullPath) if os.path.isfile(os.path.join(virtualImages_fullPath, f)))
        virtual_annotations_basenames = set(os.path.splitext(f)[0] for f in os.listdir(VirtualannotationPath) if os.path.isfile(os.path.join(VirtualannotationPath, f)))

        if virtual_image_basenames == virtual_annotations_basenames:
            print("All VIRTUAL annotations are in equal to Images")
        else:
            print("There is a mismatch (VIRTUAL)")

# Checking Image Corruption Validity

def checkImageCorruption(path):
    return cv2.imread(path) is None

# 1 - Real Images
realCorruptionCount = 0
for images in os.listdir(realImages_fullPath):
    fullImagePath = os.path.join(realImages_fullPath,images)
    if checkImageCorruption(fullImagePath):
        print(f"{fullImagePath} is corrupted.")
        realCorruptionCount += 1

if realCorruptionCount == len(os.listdir(realImages_fullPath)):
    print("All Images are NOT corrupted")

# 2 - Virtual Images
virtualCorruptionCount = 0
for images in os.listdir(virtualImages_fullPath):
    fullImagePath = os.path.join(virtualImages_fullPath,images)
    if checkImageCorruption(fullImagePath):
        print(f"{fullImagePath} is corrupted.")
        virtualCorruptionCount += 1

if virtualCorruptionCount == len(os.listdir(virtualImages_fullPath)):
    print("All Images are NOT corrupted")

# Checking Image dimension Validity

def checkImageSize(path):
    img = cv2.imread(path)
    width, height = img.shape[:2]
    return width <= 0 or height <= 0 or width > 1920 or height > 1920

