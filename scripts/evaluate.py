from ultralytics import YOLO

model = YOLO("./chessboard-yolo/run13/weights/best.pt")
results = model.predict(
    source="./testImages",
    imgsz=640,
    conf=0.5,
    save=True,
    save_txt=False,
    project="predictions",
    name="run1"
)