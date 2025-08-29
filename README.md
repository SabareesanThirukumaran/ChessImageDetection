# ♟ Chessboard Detection with YOLOv8 🤖✨

Welcome to **Chessboard Detection** – a project where AI meets chess! Train a YOLOv8 segmentation model to detect chessboards and chess pieces from images with ease. Perfect for your first computer vision project! 🖼️🧠
Chess Board Images from Kaggle --> https://www.kaggle.com/datasets/imtkaggleteam/chess-pieces-detection-image-dataset

## 🚀 Features
- Custom dataset of chessboard images with polygon masks ♟️
- YOLOv8 training & evaluation pipeline ⚡
- Inference script to predict on new images (`scripts/predict.py`) 🏎️
- Automatically saves prediction images in `predictions/` folder 🖼️✅

## 💻 Installation
1. Clone the repository:
    git clone https://github.com/SabareesanThirukumaran/ChessImageDetection.git
2. Navigate to project:
   cd ChessImageDetection
3. Install dependencies:
   pip install -r requirements.txt

## 🏋️‍♂️ Training
- Run the training script:
   python scripts/train.py
- Training configuration:
  Epochs: 100 ⏱️
  Image size: 416 📐
  Batch size: 4
  Optimizer: SGD
  Trained weights saved in `chessboard-yolo/`

## 🔍 Prediction
- Run inference:
   python scripts/predict.py
- Model path: ./chessboard-yolo/runX/weights/best.pt
- Input images: testImages/
- Output: predictions/run1/

## 📊 Results
- Trained on ~600 chessboard images 📸
- Achieved working predictions 🎯
- Example outputs available in `predictions/run1/` 🖼️

## 🌟 Future Improvements
- Add more diverse images with different lighting & angles 🌞🌜
- Train longer with higher image resolution (e.g., 640px) 📏
- Experiment with larger YOLOv8 models (m or l) for better accuracy 📈
- Refine masks for cleaner detection ✨

## Author
Sabareesan Thirukumaran - Github / Linkedin

## 🏁 Conclusion
This is a **first end-to-end ML project** including dataset creation, model training, inference, and visualization. A perfect foundation for advanced chessboard analysis and piece detection! ♟️🤖💡
