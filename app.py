import streamlit as st
import os

from storage import save_video, get_videos, get_clips
from ai import generate_clip

st.set_page_config(
    page_title="ClipAI",
    page_icon="🎬",
    layout="wide"
)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================
# SIDEBAR
# ==========================

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

# ==========================
# DASHBOARD
# ==========================

if menu == "🏠 Dashboard":

    st.title("🎬 ClipAI Dashboard")

    st.success("🟢 Server Online")

    st.write("Selamat datang di ClipAI!")

    st.info(
        "Upload video panjang lalu buat beberapa clip otomatis."
    )

# ==========================
# UPLOAD
# ==========================

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

        duration = st.selectbox(
            "Durasi Clip",
            [15, 30, 60],
            index=1
        )

        if st.button("🚀 Generate Clip"):

            progress = st.progress(0)
            status = st.empty()

            for i in range(100):

                progress.progress(i + 1)

                if i < 30:
                    status.text("📤 Upload...")
                elif i < 60:
                    status.text("🎬 Processing...")
                elif i < 90:
                    status.text("✂️ Creating Clips...")
                else:
                    status.text("✅ Finishing...")

            result = generate_clip(
                input_path,
                duration
            )
                        st.success(result["message"])

            if "outputs" in result:

                st.subheader("🎬 Hasil Clip")

                for i, clip in enumerate(result["outputs"], start=1):

                    st.write(f"### Clip {i}")

                    st.video(clip)

                    with open(clip, "rb") as f:

                        st.download_button(
                            label=f"📥 Download Clip {i}",
                            data=f,
                            file_name=os.path.basename(clip),
                            mime="video/mp4",
                            key=f"clip_{i}"
                        )

            else:

                st.error("❌ Tidak ada clip yang berhasil dibuat.")
                # ==========================
# MY VIDEOS
# ==========================

elif menu == "📂 My Videos":

    st.title("📂 My Videos")

    videos = get_videos()

    if videos:

        for video in videos:

            st.write(f"🎥 {video}")

    else:

        st.info("Belum ada video.")

# ==========================
# RESULTS
# ==========================

elif menu == "📥 Results":

    st.title("📥 Results")

    clips = get_clips()

    if clips:

        for clip in clips:

            st.write(f"✅ {clip}")

            clip_path = os.path.join(
                OUTPUT_FOLDER,
                clip
            )

            if os.path.exists(clip_path):

                st.video(clip_path)

                with open(clip_path, "rb") as f:

                    st.download_button(
                        label=f"⬇️ Download {clip}",
                        data=f,
                        file_name=clip,
                        mime="video/mp4",
                        key=f"result_{clip}"
                    )

    else:

        st.info("Belum ada clip.")

# ==========================
# SETTINGS
# ==========================

elif menu == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.write("ClipAI Version 2.0")

    st.write("Developed by Ahmad")
