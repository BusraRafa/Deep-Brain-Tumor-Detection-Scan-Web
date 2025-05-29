from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

model = tf.keras.models.load_model("model/xception_brain_tumor_model.h5")
print("Model output shape:", model.output_shape)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    image = image.resize((224, 224))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    prediction = model.predict(img_array)[0][0]
    print("Raw prediction:", prediction)
    result = "Brain Tumor Detected" if prediction >= 0.5 else "No Brain Tumor Detected"

    return render_template("home.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
