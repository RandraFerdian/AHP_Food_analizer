import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AHP Fast Food Analyzer | Latar Belakang",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 Latar Belakang & Dataset")

st.markdown("""
## 🌍 Konteks Global

Menurut **Organisasi Kesehatan Dunia (WHO)**, pola makan yang tidak sehat menyumbang sekitar **11 juta kematian setiap tahun** di seluruh dunia.  
Konsumsi tinggi makanan cepat saji yang kaya kalori, lemak jenuh, natrium (garam), dan kolesterol menjadi kontributor utama berbagai penyakit tidak menular, seperti:

- 🫀 **Penyakit jantung koroner**
- ⚖️ **Obesitas**
- 🧠 **Tekanan darah tinggi**
- 🍟 **Diabetes tipe 2**

---

## 🤔 Mengapa AHP?

Dalam memilih makanan cepat saji yang lebih sehat, kita dihadapkan pada banyak alternatif dan kriteria yang saling bertentangan.  
Metode **Analytical Hierarchy Process (AHP)** membantu memecahkan masalah ini dengan cara:

- Menyusun kriteria penting secara hierarkis
- Membandingkan alternatif berdasarkan bobot tiap kriteria
- Menghasilkan peringkat akhir yang dapat diandalkan

---

## 🧾 Kriteria Penilaian

Dalam aplikasi ini, saya mengevaluasi setiap menu fast food berdasarkan **5 kriteria utama kesehatan**, yaitu:

1. 🥩 **Protein** – Nutrien penting untuk pertumbuhan otot & regenerasi sel
2. 🔥 **Kalori** – Jumlah energi; terlalu tinggi → obesitas
3. 🧈 **Lemak** – Berlebih dapat menyumbat arteri
4. 🧂 **Garam (Sodium)** – Kelebihan dapat meningkatkan tekanan darah
5. 🥚 **Kolesterol** – Dapat memicu gangguan jantung jika berlebihan

---

## 📊 Dataset Fast Food

Dataset ini berisi informasi nutrisi dari berbagai jenis makanan cepat saji yang dikumpulkan dari restoran-restoran ternama dunia, seperti:

- McDonald's
- Burger King
- KFC
- Subway
- Wendy's, dll.

Setiap entri memuat kandungan nutrisi seperti kalori, protein, lemak, kolesterol, sodium, dan lainnya.

""")


df = pd.read_csv("./dataset/fastfood_clean.csv")

with st.expander("📂 Lihat Data Nutrisi Fast Food (klik untuk buka/tutup)"):
    st.dataframe(df, use_container_width=True)

st.caption("📌 Sumber: https://openintro.org/data/index.php?data=fastfood (telah dibersihkan & disederhanakan)")
