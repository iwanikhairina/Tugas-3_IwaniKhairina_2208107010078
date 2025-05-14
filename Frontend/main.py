import streamlit as st
import requests
from PIL import Image
import io

API_URL = "http://localhost:8000/predict/"

st.title("Rock-Paper-Scissors Classifier")
st.write("Anda bisa upload gambar atau pakai kamera untuk klasifikasi")

# Pilihan input: kamera atau file upload
input_method = st.radio("Pilih sumber input:", ("Upload Gambar", "Kamera"))

img = None
if input_method == "Upload Gambar":
    uploaded = st.file_uploader("Pilih file gambar", type=["jpg","png","jpeg"])
    if uploaded:
        img = Image.open(uploaded)
elif input_method == "Kamera":
    camera_img = st.camera_input("Ambil foto dengan kamera")
    if camera_img:
        img = Image.open(camera_img)

# Jika ada gambar, tampilkan & tombol Predict
if img:
    st.image(img, caption="Input image", use_container_width=True)
    if st.button("Predict"):
        with st.spinner("Memproses..."):
            # Siapkan file untuk dikirim ke backend
            buf = io.BytesIO()
            img.save(buf, format="JPEG")
            buf.seek(0)
            files = {"file": ("image.jpg", buf.getvalue(), "image/jpeg")}
            try:
                response = requests.post(API_URL, files=files)
                if response.ok:
                    data = response.json()
                    
                    # Tampilkan hasil dengan warna yang berbeda berdasarkan class
                    if data['label'] == "rock":
                        result_color = "blue"
                    elif data['label'] == "paper":
                        result_color = "green"
                    elif data['label'] == "scissors":
                        result_color = "red"
                    else:
                        result_color = "orange"
                    
                    st.markdown(f"<h2 style='color:{result_color};text-align:center'>{data['label'].upper()}</h2>", unsafe_allow_html=True)
                    st.progress(float(data['confidence']))
                    st.text(f"Confidence: {data['confidence']*100:.1f}%")
                else:
                    st.error(f"Terjadi kesalahan: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {str(e)}")
                st.info("Pastikan backend server sedang berjalan di http://localhost:8000")

# Tambahkan informasi tentang proyek
with st.expander("Tentang Proyek"):
    st.markdown("""
    ### Rock-Paper-Scissors Image Classifier
    
    Proyek ini menggunakan Deep Learning untuk mengklasifikasikan gambar tangan yang menunjukkan:
    - ✊ **Rock** (Batu)
    - ✋ **Paper** (Kertas)
    - ✌️ **Scissors** (Gunting)
    
    **Teknologi yang digunakan:**
    - Model: MobileNetV2 dengan Transfer Learning
    - Backend: FastAPI
    - Frontend: Streamlit
    
    **Cara Penggunaan:**
    1. Pilih sumber input (upload gambar atau ambil dengan kamera)
    2. Klik tombol "Predict" untuk mendapatkan hasil klasifikasi
    
    *Proyek ini dikembangkan untuk tugas mata kuliah Machine Learning.*
    """)
