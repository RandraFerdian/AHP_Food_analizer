import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="AHP Fast Food Analyzer/Home",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Konten utama
st.markdown("""
# 🍔 **AHP Fast Food Analyzer**
### Menentukan Fast Food Tersehat Menggunakan Metode Analytical Hierarchy Process (AHP)

---

Selamat datang di aplikasi analisis makanan cepat saji berbasis metode AHP!  
Tujuan dari aplikasi ini adalah membantu pengguna memilih makanan cepat saji yang **paling sehat** berdasarkan berbagai **kriteria nutrisi**.

Silakan navigasi ke halaman berikutnya melalui sidebar di kiri layar.
""")
