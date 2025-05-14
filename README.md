# 🎮 Proyek Klasifikasi Gambar Batu, Kertas, Gunting

**Nama**: Iwani Khairina
**NIM**: 2208107010078

---

## 📝 Ringkasan Proyek

Proyek ini bertujuan untuk membangun sistem klasifikasi gambar menggunakan metode *Transfer Learning* dengan arsitektur **MobileNetV2**. Model akan mengenali tiga kategori gambar, yaitu:

* 🪨 Batu (*Rock*)
* 📄 Kertas (*Paper*)
* ✂️ Gunting (*Scissors*)

Model yang telah dilatih akan diintegrasikan ke dalam aplikasi backend berbasis **FastAPI**, yang memungkinkan pengguna mengirim gambar dan menerima prediksi secara langsung.

---

## ⚙️ Teknologi yang Digunakan

* **TensorFlow / Keras** → Untuk membangun dan melatih model klasifikasi.
* **FastAPI** → Untuk membuat REST API backend.
* **Uvicorn** → Server untuk menjalankan aplikasi FastAPI.
* **Pillow (PIL)** → Untuk memproses gambar.
* **NumPy** → Untuk manipulasi data numerik.
* **scikit-learn** → Untuk evaluasi performa model (*classification report*, *confusion matrix*).

---

## 🗂️ Struktur Direktori Proyek


