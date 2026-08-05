import streamlit as st

st.set_page_config(
    page_title="ClipAI",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 ClipAI")

st.write("Selamat datang di ClipAI")

uploaded = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi", "mkv"]
)

if uploaded:
    st.success(f"Video berhasil dipilih: {uploaded.name}")
    st.video(uploaded)

    if st.button("Generate Clip"):
        st.info("🚀 Fitur AI sedang dikembangkan...")
import os

os.makedirs("uploads", exist_ok=True)

with open(f"uploads/{uploaded.name}", "wb") as f:
    f.write(uploaded.getbuffer())

st.success("✅ Video berhasil disimpan")
