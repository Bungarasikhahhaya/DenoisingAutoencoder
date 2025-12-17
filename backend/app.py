from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app)

# ----- KONFIGURASI MODEL -----
MODEL_PATH = r"D:\Anis\sem 5\prak ai\project uas\face_clean\DenoisingAutoencoder\backend\model\DenoisingAutoencoder-20251202T172816Z-1-001\DenoisingAutoencoder\saved_models\dataweights.115-0.00.keras"

print("MODEL_PATH =", MODEL_PATH)
print("EXISTS? ", os.path.isfile(MODEL_PATH))

IMG_SIZE = (256, 256)  # ganti sesuai input model
IS_GRAY = False        # True kalau model 1-channel (grayscale)

# Load model sekali di awal
model = load_model(MODEL_PATH)


def preprocess_image(file_bytes: bytes) -> np.ndarray:
    # Baca gambar dari bytes
    image = Image.open(io.BytesIO(file_bytes))

    # Simpan ukuran asli
    original_size = image.size  # (width, height)

    # Konversi mode
    if IS_GRAY:
        image = image.convert("L")   # grayscale
    else:
        image = image.convert("RGB")  # 3 channel

    # Resize sesuai ukuran input model
    image = image.resize(IMG_SIZE)

    # ke numpy array dan normalisasi
    array = img_to_array(image) / 255.0  # [0,1]
    if IS_GRAY and array.ndim == 2:
        array = np.expand_dims(array, axis=-1)  # (h,w,1)
    array = np.expand_dims(array, axis=0)       # (1,h,w,c)
    return array, original_size


def array_to_base64(img_array: np.ndarray) -> str:
    # img_array: (h,w,c) atau (h,w)
    img_array = np.clip(img_array * 255.0, 0, 255).astype("uint8")
    if img_array.ndim == 2:
        img = Image.fromarray(img_array, mode="L")
    else:
        img = Image.fromarray(img_array)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return base64.b64encode(byte_im).decode("utf-8")


# Endpoint test untuk cek CORS
@app.route("/api/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})


@app.route("/api/denoise", methods=["POST"])
def denoise():
    # Pastikan ada file dengan key 'image'
    if "image" not in request.files:
        return jsonify({"error": "no image"}), 400

    file = request.files["image"]
    img_bytes = file.read()

    # Preprocess gambar
    x, original_size = preprocess_image(img_bytes)

    # Prediksi dengan autoencoder
    denoised = model.predict(x)[0]  # keluaran: (h,w,c) atau (h,w,1)

    # Kalau 1-channel, buang channel axis
    if denoised.ndim == 3 and denoised.shape[-1] == 1:
        denoised = denoised.squeeze(-1)


    # Konversi array ke gambar PIL dengan mode yang sesuai
    arr_uint8 = np.clip(denoised * 255.0, 0, 255).astype("uint8")
    if IS_GRAY:
        pil_img = Image.fromarray(arr_uint8, mode="L")
    else:
        pil_img = Image.fromarray(arr_uint8, mode="RGB")

    # Resize ke ukuran asli
    pil_img = pil_img.resize(original_size)

    # Kembali ke array float [0,1] untuk base64
    arr_resized = np.asarray(pil_img).astype(np.float32) / 255.0

    # Konversi ke base64
    b64 = array_to_base64(arr_resized)

    return jsonify({"image_base64": b64})


if __name__ == "__main__":
    print("Starting Flask...")
    app.run(host="0.0.0.0", port=5000, debug=True)