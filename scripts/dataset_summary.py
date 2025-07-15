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
    print("All Images Collected")
