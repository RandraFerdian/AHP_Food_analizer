import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from utils.ahp_utils import calc_norm

st.set_page_config(
    page_title="AHP Fast Food Analyzer | Hasil",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏆 Hasil Perhitungan AHP")

df = pd.read_csv("./dataset/fastfood_clean.csv")

# Bobot Kriteria (dari perhitungan sebelumnya)
w_MPB = np.array([0.4129, 0.2571, 0.1539, 0.0881, 0.0881])

# Hitung bobot alternatif
w_E = calc_norm(df['protein'].values)
w_L = calc_norm(df['total_fat'].values)
w_Ka = calc_norm(df['calories'].values)
w_G = calc_norm(df['sodium'].values)
w_Ko = calc_norm(df['cholesterol'].values)

wM = np.column_stack((w_E, w_Ka, w_L, w_G, w_Ko))
MC_Scores = np.dot(wM, w_MPB)
df['score'] = MC_Scores

# Ambil 10 tertinggi
top10 = df[['restaurant', 'item', 'score']].sort_values(by='score', ascending=False).head(10)

# Tampilkan hasil terbaik
best = top10.iloc[0]
st.markdown("## 🥇 Fast Food Tersehat")
st.success(f"""
**{best['item']}** dari **{best['restaurant']}**  
Skor AHP: **{best['score']:.4f}**
""")

# Tampilkan Top 10
st.divider()
st.markdown("## 📊 Top 10 Fast Food Berdasarkan Skor AHP")
with st.expander("📄 Tabel 10 Teratas"):
    st.dataframe(top10.reset_index(drop=True), use_container_width=True)

# Visualisasi dengan Altair (bar horizontal)
st.divider()
st.markdown("## 📈 Visualisasi Skor (Top 10)")
with st.expander("📊 Lihat Grafik (klik untuk buka/tutup)"):
    st.write("Grafik ini menunjukkan perbandingan skor AHP dari 10 menu fast food teratas berdasarkan kriteria nutrisi.")
    bar_chart = alt.Chart(top10).mark_bar(size=20).encode(
    x=alt.X('score:Q', title='Skor AHP'),
    y=alt.Y('item:N', sort='-x', title='Menu'),
    color=alt.Color('restaurant:N', legend=alt.Legend(title="Restoran")),
    tooltip=['restaurant', 'item', 'score']
    ).properties(
    width=800,
    height=400
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    )
    st.altair_chart(bar_chart, use_container_width=True)

# Info akhir
st.info("Skor dihitung berdasarkan kombinasi bobot dari masing-masing kriteria nutrisi menggunakan metode AHP.")
