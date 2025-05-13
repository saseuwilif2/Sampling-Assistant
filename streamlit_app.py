import streamlit as st

st.set_page_config(page_title="Sampling Assistant", layout="centered")

st.title("📊 Sampling Assistant")
st.markdown("Aplikasi ini membantu menentukan jumlah dan daftar sampel berdasarkan ukuran populasi dan persentase sampling.")

# Input data
pop_size = st.number_input("Masukkan jumlah populasi", min_value=1, step=1)

sampling_percent = st.slider("Pilih persentase sampling (%)", min_value=1, max_value=100, value=10)

# Tombol untuk menghitung
if st.button("Hitung Sampel"):
    sample_size = round((sampling_percent / 100) * pop_size)
    st.success(f"Jumlah sampel yang harus disampling: **{sample_size}** dari total {pop_size}")

    # Pilih sampel acak
    population_list = list(range(1, pop_size + 1))
    sampled = random.sample(population_list, sample_size)

    # Tampilkan sampel
    st.markdown("### 🎯 Daftar ID yang harus disampling:")
    st.code(", ".join(map(str, sampled)), language='text')
