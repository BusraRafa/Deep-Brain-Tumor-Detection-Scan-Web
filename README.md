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

## 🛠️ Preprocessing Pipeline

## 🔀 Data Split — 3,000 MRI Images
``` bash
-  Train:         ───────────────      66.7% (2,000 Images)
-  Validation:    ────────             20.0% (600 Images) 
-  Test:          ──────               13.3% (400 Images) 
```
---

## ⚙️ Preprocessing Steps
``` bash
- Cropping around brain region (contour-based)
- Image resizing to (224, 224)
- Normalization
- Data augmentation (rotation, zoom, flip, etc.)
- Final folders: `TRAIN_CROP/`, `VAL_CROP/`, `TEST_CROP/`
```
---

## 🧠 Model Development

Trained and compared four different CNN architectures:
```bash
- DenseNet169 – 97.0% accuracy
- EfficientNetB2 - 98.75%   (used in the final app)
- InceptionResNetV2 – 99.5% accuracy
- Xception – 98.0% accuracy
```


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
2. **create the virtual environment:**
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
