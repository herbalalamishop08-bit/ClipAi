import streamlit as st
import os

from storage import save_video, get_videos, get_clips
from ai import generate_clip
from clipper import make_clip

st.set_page_config(
    page_title="ClipAI",
    page_icon="🎬",
    layout="wide"
)

os.makedirs("uploads", exist_ok=True)

# ======================
# Sidebar
# ======================
with st.sidebar:
    st.title("🎬 ClipAI")

    menu = st.radio(
        "Menu",
        [
            "🏠 Dashboard",
            "📤 Upload",
            "📂 My Videos",
            "📥 Results",
            "⚙️ Settings"
        ]
    )

# ======================
# Dashboard
# ======================
if menu == "🏠 Dashboard":

    st.title("🎬 ClipAI Dashboard")
    st.write("Selamat datang di ClipAI!")
    st.success("Server berjalan dengan baik ✅")

# ======================
# Upload
# ======================
elif menu == "📤 Upload":

    st.title("📤 Upload Video")

    uploaded = st.file_uploader(
        "Pilih Video",
        type=["mp4", "mov", "avi", "mkv"]
    )

    if uploaded:

        input_path = save_video(uploaded)

        st.success("✅ Video berhasil disimpan")

        st.video(uploaded)

        if st.button("Generate Clip"):

            progress = st.progress(0)

            for i in range(100):
                progress.progress(i + 1)

            result = generate_clip(input_path)

            st.success(result["message"])

# ======================
# My Videos
# ======================
elif menu == "📂 My Videos":

    st.title("📂 Video Saya")

    videos = get_videos()

    if videos:
        for video in videos:
            st.write(f"🎥 {video}")
    else:
        st.info("Belum ada video.")

# ======================
# Results
# ======================
elif menu == "📥 Results":

    st.title("📥 Hasil Clip")

    clips = get_clips()

    if clips:

        for clip in clips:

            st.write(f"✅ {clip}")

            with open(f"uploads/{clip}", "rb") as f:

                st.download_button(
                    f"⬇️ Download {clip}",
                    data=f,
                    file_name=clip,
                    mime="video/mp4"
                )

    else:

        st.info("Belum ada clip.")

# ======================
# Settings
# ======================
elif menu == "⚙️ Settings":

    st.title("⚙️ Pengaturan")

    st.write("Versi : ClipAI v1.0")

    st.write("Developer : Ahmad")
