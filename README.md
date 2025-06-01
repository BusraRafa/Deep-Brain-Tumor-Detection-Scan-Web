# 🧠 Brain Tumor Detection Web App

This is a web-based brain tumor detection application that allows users to upload MRI images and get predictions using a deep learning model trained on brain tumor data.
## 📊 Dataset 
```bash
https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection/data
```
##  About Dataset Structure

| Folder | Description | Number of Images |
|---|---|---|
| `yes` | Contains **tumorous** Brain MRI Images. | 1500 |
| `no` | Contains **non-tumorous** Brain MRI Images. | 1500 |

## 🚀 Live Demo
> Coming soon (once deployed on Vercel)

## 📌 Features

- Upload MRI images for prediction
- Detects presence or absence of brain tumor
- Uses a trained EfficientNetB2 deep learning model
- Streamlit-based user interface
- Clean and user-friendly web design
- Responsive and fast prediction

## 🧠 Model Details

- **Architecture**: EfficientNetB2
- **Input Shape**: `(224, 224, 3)`
- **Layers**:
  - GlobalMaxPooling2D
  - Dropout (rate = 0.2)
  - Dense layer with sigmoid activation
- **Output**: Binary classification (Tumor / No Tumor)
- **Frameworks**: TensorFlow / Keras

## 🗂️ Project Structure
```bash
brain-tumor-detection/
│
├── static/ 
│  └── style.css
├── templates/ 
│ └── home.html
│
├── model/
│ └── brain_tumor_model.h5 
│
├── web_app.py 
├── requirements.txt 
├── README.md
└── .gitignore
```

## 🔧 Installation & Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/brain-tumor-detection.git
   cd brain-tumor-detection
   ```
2.**create the virtual environment:**
  ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```bash
   python web_app.py
   ```
5. **Open your browser and go to:**
   ```bash
   http://127.0.0.1:5000/
   ```
