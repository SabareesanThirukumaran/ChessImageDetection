from ultralytics import YOLO

model = YOLO("yolov8s-seg.pt")

model.train(data="data.yaml", epochs=100, imgsz=416, batch=4, device=0, workers=4, patience=20, optimizer="SGD", verbose=True, save=True, half=True, project="chessboard-yolo", name="run1")
model.val()