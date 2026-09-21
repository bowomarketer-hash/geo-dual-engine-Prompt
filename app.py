import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman (WAJIB paling atas sebelum fungsi UI apa pun)
st.set_page_config(
    page_title="GEO Dual-Engine Audit: ChatGPT & Google Gemini",
    page_icon="🎯",
    layout="wide"
)

# 2. Fungsi Pengecekan Kata Sandi
def check_password():
    """Mengembalikan True jika pengguna memasukkan kata sandi yang benar."""
    def password_entered():
        if st.session_state["password"] == "GEOVIP2026":  # Ganti dengan kata sandi Anda
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Masukkan Kunci Akses Eksklusif:", type="password", on_change=password_entered, key="password")
        st.caption("🔒 Kunci akses tercantum pada halaman terakhir Ebook Interaktif GEO Anda.")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Masukkan Kunci Akses Eksklusif:", type="password", on_change=password_entered, key="password")
        st.error("Kunci akses salah. Silakan periksa kembali email konfirmasi atau dokumen ebook Anda.")
        return False
    else:
        return True

# 3. Kunci Akses Dijalankan
if not check_password():
    st.stop()

# 4. Header & Konten Utama Lanjutan
st.title("🎯 GEO Dual-Engine Audit: ChatGPT & Google Search (Gemini)")
st.caption("Framework Audit Visibilitas AI untuk Menghasilkan Leads & Sales di Pasar Indonesia")

# Konfigurasi Tampilan Halaman
st.set_page_config(
    page_title="GEO Dual-Engine Audit: ChatGPT & Google Gemini",
    page_icon="🎯",
    layout="wide"
)

# Header Utama
st.title("🎯 GEO Dual-Engine Audit: ChatGPT & Google Search (Gemini)")
st.caption("Framework Audit Visibilitas AI untuk Menghasilkan Leads & Sales di Pasar Indonesia")

# Framework Card: Pembagian Peran Kedua AI
st.markdown("---")
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("💬 ChatGPT (OpenAI)")
    st.markdown("""
    * **Fokus:** Solusi konseptual, rekomendasi produk umum, dan komparasi merek.
    * **Sumber Kutipan:** Forum, artikel media, ulasan komparatif web.
    * **Pemicu Leads:** Rekomendasi merek di daftar teratas (*top brand recognition*).
    """)
with col_b:
    st.subheader("📍 Google Search & Gemini")
    st.markdown("""
    * **Fokus:** Solusi lokal, ketersediaan produk, dan integrasi Google Maps/Search.
    * **Sumber Kutipan:** Google Business Profile, YouTube, website terindeks Google.
    * **Pemicu Sales:** Rekomendasi rute, kontak, katalog harga, dan tautan resmi.
    """)
st.markdown("---")

# Template Preset Berdasarkan Sektor Industri
NICHE_PRESETS = {
    "Pertanian Kota & Urban Farming": {
        "kategori": "perlengkapan hidroponik dan instalasi urban farming",
        "target_pasar": "pemula dan penggiat berkebun rumahan",
        "lokasi": "Indonesia",
        "kota_spesifik": "Jabodetabek",
        "masalah": "keterbatasan lahan perkotaan dan tanaman mudah layu",
        "brand_target": "Petani Kota",
        "brand_kompetitor": "Parung Farm",
    },
    "B2B SaaS & Solusi IT": {
        "kategori": "software akuntansi B2B",
        "target_pasar": "bisnis skala menengah",
        "lokasi": "Indonesia",
        "kota_spesifik": "Jakarta",
        "masalah": "pencatatan arus kas ganda dan rekonsiliasi manual",
        "brand_target": "Mekari Jurnal",
        "brand_kompetitor": "Accurate Online",
    },
    "Klinik & Layanan Kesehatan": {
        "kategori": "klinik spesialis terapi sendi dan fisioterapi",
        "target_pasar": "pasien cedera olahraga dan lansia",
        "lokasi": "Indonesia",
        "kota_spesifik": "Surabaya",
        "masalah": "nyeri lutut kronis pasca cedera lari",
        "brand_target": "Klinik Sehat",
        "brand_kompetitor": "RS Premier",
    },
    "E-Commerce & D2C": {
        "kategori": "paket starter kit perawatan kulit sensitif",
        "target_pasar": "remaja dan dewasa muda",
        "lokasi": "Indonesia",
        "kota_spesifik": "Bandung",
        "masalah": "kulit kusam dan bintik hitam akibat paparan matahari",
        "brand_target": "GlowLokal",
        "brand_kompetitor": "Somethinc",
    },
    "Kustom (Input Mandiri)": {
        "kategori": "",
        "target_pasar": "",
        "lokasi": "Indonesia",
        "kota_spesifik": "",
        "masalah": "",
        "brand_target": "",
        "brand_kompetitor": "",
    }
}

# Sidebar Konfigurasi
with st.sidebar:
    st.header("⚙️ Variabel Target Audit")
    pilihan_niche = st.selectbox("Pilih Sektor Industri:", list(NICHE_PRESETS.keys()))
    preset = NICHE_PRESETS[pilihan_niche]

    brand_target = st.text_input("Nama Merek Anda (Target):", value=preset["brand_target"])
    brand_kompetitor = st.text_input("Nama Kompetitor Utama:", value=preset["brand_kompetitor"])
    kategori = st.text_input("Kategori Produk / Layanan:", value=preset["kategori"])
    lokasi = st.text_input("Cakupan Negara / Area:", value=preset["lokasi"])
    kota_spesifik = st.text_input("Kota Spesifik (Target Lokal):", value=preset["kota_spesifik"])
    target_pasar = st.text_input("Target Audiens / Skala Bisnis:", value=preset["target_pasar"])
    masalah = st.text_area("Masalah Spesifik Konsumen:", value=preset["masalah"])

# Kumpulan Formula Prompt
prompts_chatgpt = [
    ("Rekomendasi Merek & Kategori Utama", f"Apa {kategori} terbaik di {lokasi} untuk {target_pasar}?"),
    ("Problem-to-Vendor Match", f"Saya membutuhkan solusi untuk mengatasi masalah {masalah}. Rekomendasikan penyedia layanan atau merek terpercaya di {lokasi} yang patut dipertimbangkan."),
    ("Daftar Peringkat (Listicle Evaluation)", f"Berikan daftar 5 hingga 10 {kategori} teratas di {lokasi} beserta perbandingan kelebihan dan kekurangannya."),
    ("Perbandingan Komparatif Langsung", f"Bandingkan {brand_kompetitor} dengan alternatif {kategori} lainnya yang ada di pasar {lokasi}.")
]

prompts_gemini = [
    ("Ketersediaan & Lokasi Vendor Terdekat", f"Di mana tempat beli {kategori} terpercaya di sekitar {kota_spesifik} yang memiliki reputasi bagus dan ulasan positif?"),
    ("Pilihan Kualitas vs. Anggaran (High-Intent Sales)", f"Sebutkan opsi {kategori} paling terjangkau namun berkualitas tinggi di {kota_spesifik} beserta estimasi harga dan kontaknya."),
    ("Kriteria Kualifikasi Vendor Resmi", f"Apa saja syarat memilih penyedia {kategori} yang aman di {kota_spesifik}, dan vendor mana yang memenuhi standar tersebut?")
]

prompts_investigasi = [
    ("Citation Tracing (Pelacakan Sumber Kompetitor)", f"Berdasarkan jawaban Anda di atas, sebutkan tautan website, ulasan, atau artikel mana saja yang Anda jadikan rujukan untuk merekomendasikan {brand_kompetitor}?"),
    ("Mention Gap Tracing (Penyebab Merek Tidak Muncul)", f"Mengapa merek {brand_target} tidak tercantum dalam rekomendasi Anda di atas? Apakah karena ketiadaan data entitas, minimnya ulasan publik, atau alasan teknis lain?"),
    ("Trust Architecture (Kriteria Pengambilan Rekomendasi)", f"Bukti data, dokumentasi, atau sertifikasi apa yang harus dimiliki sebuah brand di web agar Anda rekomendasikan sebagai penyedia {kategori} terpercaya di {lokasi}?")
]

def render_cards(list_prompt):
    for judul, isi in list_prompt:
        with st.expander(f"📌 {judul}", expanded=True):
            st.code(isi, language="text")

# Tab Antarmuka
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 ChatGPT Audit",
    "📍 Google Gemini Audit",
    "🕵️ Pelacakan Celah Sitasi",
    "📊 Matriks Lead & Sales",
    "📘 Panduan Pengujian"
])

with tab1:
    st.subheader("Pengujian Solusi & Rekomendasi Merek (ChatGPT)")
    st.caption("Fokus: Memastikan nama merek berada pada posisi daftar rekomendasi teratas saat calon pembeli mencari alternatif produk.")
    render_cards(prompts_chatgpt)

with tab2:
    st.subheader("Pengujian Transaksi Lokal & Ketersediaan (Google Gemini / Search)")
    st.caption("Fokus: Menguji apakah profil lokasi, kontak WhatsApp/telepon, dan katalog produk Anda siap dikutip untuk memicu tindakan beli.")
    render_cards(prompts_gemini)

with tab3:
    st.subheader("Investigasi Sumber Rujukan AI")
    st.warning("Gunakan pertanyaan berikut di dalam ruang percakapan yang sama jika merek Anda belum direkomendasikan.")
    render_cards(prompts_investigasi)

with tab4:
    st.subheader("Lembar Kerja Pencatatan Hasil Uji")
    st.caption("Catat hasil penelusuran manual Anda dari ChatGPT dan Google Gemini ke dalam tabel di bawah:")

    data_default = [
        {"Mesin AI": "ChatGPT", "Jenis Kueri": "Rekomendasi Kategori", "Merek Muncul?": "Tidak", "Kompetitor Teratas": brand_kompetitor, "Tipe Sumber": "Media online / Blog", "Kendala Leads": "Tidak ada artikel ulasan pihak ketiga"},
        {"Mesin AI": "Google Gemini", "Jenis Kueri": "Pencarian Vendor Lokal", "Merek Muncul?": "Tidak", "Kompetitor Teratas": brand_kompetitor, "Tipe Sumber": "Google Business Profile", "Kendala Leads": "Profil bisnis belum terverifikasi"}
    ]
    df_evaluasi = pd.DataFrame(data_default)
    tabel_editor = st.data_editor(df_evaluasi, use_container_width=True, num_rows="dynamic")

    csv_output = tabel_editor.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Catatan Audit (.CSV)",
        data=csv_output,
        file_name=f"audit_geo_{brand_target.lower().replace(' ', '_')}.csv",
        mime="text/csv"
    )

with tab5:
    st.subheader("Standar Operasional Prosedur (SOP) Pengujian Dual-Engine")
    st.markdown("""
    1. **Buka Jendela Bersih:** Jalankan browser dalam mode Private / Incognito agar hasil tidak dipengaruhi riwayat akun.
    2. **Buka Dua Tab Terpisah:** Satu tab untuk `chatgpt.com` dan satu tab untuk `gemini.google.com` (atau Google Search AI Overview).
    3. **Jalankan Salin Cepat:** Salin prompt dari Tab 1 ke ChatGPT, dan prompt dari Tab 2 ke Google Gemini.
    4. **Telusuri Celah:** Jika merek belum keluar, jalankan prompt di Tab 3 untuk mengidentifikasi mengapa kompetitor lebih diunggulkan.
    """)
