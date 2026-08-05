import streamlit as st
import os
from clipper import make_clip

st.set_page_config(
    page_title="ClipAI",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 ClipAI")
st.write("Selamat datang di ClipAI")

os.makedirs("uploads", exist_ok=True)
st.divider()
st.subheader("📂 Video yang sudah diupload")

videos = [
    f for f in os.listdir("uploads")
    if f.endswith((".mp4", ".mov", ".avi", ".mkv"))
]

if videos:
    for video in videos:
        st.write(f"🎥 {video}")
else:
    st.info("Belum ada video yang diupload.")
uploaded = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi", "mkv"]
)

if uploaded:

    input_path = f"uploads/{uploaded.name}"

    with open(input_path, "wb") as f:
        f.write(uploaded.getbuffer())

    st.success("✅ Video berhasil disimpan")

    st.video(uploaded)

    if st.button("Generate Clip"):

        output = f"uploads/clip_{uploaded.name}"

        make_clip(input_path, output)

        st.success("✅ Clip berhasil dibuat!")

        st.video(output)

        with open(output, "rb") as f:
            st.download_button(
                "📥 Download Clip",
                data=f,
                file_name=f"clip_{uploaded.name}",
                mime="video/mp4"
            )
