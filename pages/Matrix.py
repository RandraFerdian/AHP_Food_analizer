import streamlit as st
import numpy as np
import pandas as pd
from utils.ahp_utils import calc_norm

st.set_page_config(
    page_title="AHP Fast Food Analyzer | Matrix",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv("./dataset/fastfood_clean.csv")
st.title("🔢 Matrix Perbandingan & Bobot Kriteria")

# --- Matrix Perbandingan ---
MPBk = np.array([
        [1,   2, 3, 4, 4],
        [1/2, 1, 2, 3, 3],
        [1/3, 1/2, 1, 2, 2],
        [1/4, 1/3, 1/2, 1, 1],
        [1/4, 1/3, 1/2, 1, 1]
    ])

st.subheader("📐 Matriks Perbandingan Kriteria")
with st.expander("📊 Lihat Matriks Perbandingan"):
    st.dataframe(pd.DataFrame(MPBk,
                               columns=["Protein", "Kalori", "Lemak", "Garam", "Kolesterol"],
                               index=["Protein", "Kalori", "Lemak", "Garam", "Kolesterol"]),
                 use_container_width=True)

norm_MPB = calc_norm(MPBk)
m, n = norm_MPB.shape
V = np.sum(norm_MPB, axis=1)
w_MPB = V / m

# --- Bobot Kriteria ---
st.subheader("⚖️ Bobot Kriteria")
cols = st.columns(5)
kriteria = ["Protein", "Kalori", "Lemak", "Garam", "Kolesterol"]
for i in range(5):
    cols[i].metric(label=kriteria[i], value=f"{w_MPB[i]:.4f}")

st.divider()

# --- Uji Konsistensi ---
Aw_MPB = MPBk @ w_MPB
lambda_max = np.mean(Aw_MPB / w_MPB)
CI_MPB = (lambda_max - n) / (n - 1)
RI_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24}
RI_MPB = RI_dict.get(n, 1.12)
CR_MPB = CI_MPB / RI_MPB

st.subheader("🧪 Uji Konsistensi")
st.write("Konsistensi penilaian kriteria sangat penting dalam AHP.")
st.code(f"λ max = {lambda_max:.4f}\nCI = {CI_MPB:.4f}\nRI = {RI_MPB}\nCR = {CR_MPB:.4f}")
if CR_MPB < 0.10:
    st.success("✅ Konsisten! (CR < 0.10)")
else:
    st.error("⚠️ Tidak konsisten (CR > 0.10)")

st.divider()

# --- Bobot Kriteria Alternatif ---
st.subheader("📊 Bobot Kriteria Alternatif")
st.markdown("Bobot alternatif dihitung dari masing-masing nilai kriteria nutrisi (dinormalisasi).")

w_E = calc_norm(df['protein'].values)
w_L = calc_norm(df['total_fat'].values)
w_Ka = calc_norm(df['calories'].values)
w_G = calc_norm(df['sodium'].values)
w_Ko = calc_norm(df['cholesterol'].values)

wM = np.column_stack((w_E, w_Ka, w_L, w_G, w_Ko))

with st.expander("📂 Lihat Bobot Kriteria Alternatif (per Item)"):
    st.dataframe(pd.DataFrame(wM,
                              columns=["Protein", "Kalori", "Lemak", "Garam", "Kolesterol"],
                              index=df['item']),
                 use_container_width=True)

st.info("✅ Bobot alternatif ini akan digunakan untuk menghitung skor akhir dari setiap alternatif fast food.")
