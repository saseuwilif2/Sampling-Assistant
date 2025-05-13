import streamlit as st

st.set_page_config(page_title="Sampling Assistant - Tabel Acak", layout="centered")
st.title("📋 Sampling Assistant - Tabel Bilangan Acak")

st.markdown("""
Aplikasi ini membantu menentukan jumlah dan daftar sampel berdasarkan ukuran populasi 
menggunakan pendekatan **tabel bilangan acak** (random number table).
""")

# Input user
pop_size = st.number_input("Masukkan jumlah populasi", min_value=1, step=1)
sample_size = st.number_input("Masukkan jumlah sampel yang diinginkan", min_value=1, step=1)

if st.button("Hitung dan Pilih Sampel"):
    if sample_size > pop_size:
        st.error("Jumlah sampel tidak boleh lebih besar dari populasi.")
    else:
        # Menentukan jumlah digit ID populasi (misal: 100 -> 3 digit)
        digit_length = len(str(pop_size))
        
        st.markdown(f"✅ Setiap ID populasi akan terdiri dari **{digit_length} digit**.")

        # Generate 'tabel acak' berupa digit 0–9 sebanyak 1000 digit
        random_digits = [str(random.randint(0, 9)) for _ in range(1000)]

        # Gabungkan digit menjadi string
        digit_str = ''.join(random_digits)

        # Pisahkan menjadi blok sesuai digit_length
        blocks = [digit_str[i:i+digit_length] for i in range(0, len(digit_str), digit_length)]

        # Filter hanya blok yang valid (dalam rentang populasi dan tidak nol)
        valid_samples = []
        seen = set()

        for block in blocks:
            if len(block) != digit_length:
                continue
            val = int(block)
            if 1 <= val <= pop_size and val not in seen:
                valid_samples.append(val)
                seen.add(val)
            if len(valid_samples) == sample_size:
                break

        if len(valid_samples) < sample_size:
            st.warning("Jumlah digit acak tidak cukup menghasilkan semua sampel unik. Tambah jumlah digit atau kurangi jumlah sampel.")
        else:
            st.success(f"Jumlah sampel berhasil dipilih: **{sample_size}**")
            st.markdown("### 🎯 ID Sampel Terpilih:")
            st.code(", ".join(str(v).zfill(digit_length) for v in valid_samples))

            with st.expander("🔢 Tabel Bilangan Acak (simulasi)"):
                # Tampilkan tabel acak dalam format tabel 20 kolom
                rows = [random_digits[i:i+20] for i in range(0, len(random_digits), 20)]
                for row in rows[:20]:  # tampilkan 20 baris saja
                    st.text(" ".join(row))
