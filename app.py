from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)

# Load model autoencoder
model = tf.keras.models.load_model('path_to_your_model.h5')  # Gantilah dengan path model Anda

# Fungsi untuk mendecode gambar base64
def decode_image(image_data):
    img_data = base64.b64decode(image_data)
    img = Image.open(BytesIO(img_data))
    img = img.convert('RGB')  # Pastikan format gambar RGB
    img = np.array(img) / 255.0  # Normalisasi gambar
    return np.expand_dims(img, axis=0)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Mengambil gambar base64 dari request
        image_data = data.get('image')

        # Mendecode dan memproses gambar
        image = decode_image(image_data)

        # Melakukan prediksi dengan model autoencoder
        denoised_image = model.predict(image)

        # Mengonversi gambar hasil rekonstruksi menjadi base64
        output_image = (denoised_image[0] * 255).astype(np.uint8)
        pil_img = Image.fromarray(output_image)
        buffered = BytesIO()
        pil_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return jsonify({'status': 'success', 'denoised_image': img_str})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)