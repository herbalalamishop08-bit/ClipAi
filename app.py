import streamlit as st
import os

from storage import save_video, get_videos, get_clips
from ai import generate_clip
from subtitle import generate_subtitle


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
        "Upload video panjang lalu buat clip otomatis."
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

        # ==========================
        # GENERATE CLIP
        # ==========================

        st.subheader("🎬 Clip Generator")

        duration = st.selectbox(
            "⏱️ Pilih Durasi Clip",
            [15, 30, 60],
            index=1
        )

        if st.button(
            "🚀 Generate Clip",
            key="generate_clip"
        ):

            try:

                with st.spinner(
                    "🎬 Membuat highlight clip..."
                ):

                    result = generate_clip(
                        input_path,
                        duration
                    )

                st.success(
                    result["message"]
                )

                if "outputs" in result:

                    st.subheader(
                        "🎬 Hasil Clip"
                    )

                    for i, clip in enumerate(
                        result["outputs"],
                        start=1
                    ):

                        video_path = clip["video"]
                        thumbnail_path = clip["thumbnail"]

                        st.write(
                            f"### 🎬 Clip {i}"
                        )

                        # Thumbnail

                        if os.path.exists(
                            thumbnail_path
                        ):

                            st.image(
                                thumbnail_path,
                                caption=f"📷 Thumbnail Clip {i}",
                                width=300
                            )

                        # Video

                        if os.path.exists(
                            video_path
                        ):

                            st.video(
                                video_path
                            )

                            with open(
                                video_path,
                                "rb"
                            ) as f:

                                st.download_button(
                                    label=f"📥 Download Clip {i}",
                                    data=f,
                                    file_name=os.path.basename(
                                        video_path
                                    ),
                                    mime="video/mp4",
                                    key=f"download_clip_{i}"
                                )

            except Exception as e:

                st.error(
                    f"❌ Gagal membuat clip: {e}"
                )


        # ==========================
        # SUBTITLE
        # ==========================

        st.divider()

        st.subheader(
            "📝 Auto Subtitle"
        )

        st.write(
            "Buat transkrip bahasa Indonesia "
            "dari video menggunakan Whisper."
        )

        if st.button(
            "📝 Generate Subtitle",
            key="generate_subtitle"
        ):

            try:

                with st.spinner(
                    "🧠 Whisper sedang mendengarkan video..."
                ):

                    subtitle_result = generate_subtitle(
                        input_path
                    )

                st.success(
                    "✅ Transkripsi berhasil!"
                )

                text = subtitle_result.get(
                    "text",
                    ""
                )

                if text:

                    st.text_area(
                        "📝 Hasil Transkripsi",
                        text,
                        height=250
                    )

                    st.download_button(
                        label="📥 Download TXT",
                        data=text,
                        file_name="subtitle.txt",
                        mime="text/plain",
                        key="download_subtitle"
                    )

                else:

                    st.warning(
                        "Tidak ada teks yang terdeteksi."
                    )

            except Exception as e:

                st.error(
                    f"❌ Subtitle gagal dibuat: {e}"
                )


# ==========================
# MY VIDEOS
# ==========================

elif menu == "📂 My Videos":

    st.title("📂 My Videos")

    videos = get_videos()

    if videos:

        for video in videos:

            st.write(
                f"🎥 {video}"
            )

    else:

        st.info(
            "Belum ada video."
        )


# ==========================
# RESULTS
# ==========================

elif menu == "📥 Results":

    st.title("📥 Results")

    clips = get_clips()

    if clips:

        for clip in clips:

            st.write(
                f"✅ {clip}"
            )

            clip_path = os.path.join(
                OUTPUT_FOLDER,
                clip
            )

            if os.path.exists(
                clip_path
            ):

                st.video(
                    clip_path
                )

                with open(
                    clip_path,
                    "rb"
                ) as f:

                    st.download_button(
                        label=f"⬇️ Download {clip}",
                        data=f,
                        file_name=clip,
                        mime="video/mp4",
                        key=f"result_{clip}"
                    )

            else:

                st.warning(
                    f"File tidak ditemukan: {clip}"
                )

    else:

        st.info(
            "Belum ada clip."
        )


# ==========================
# SETTINGS
# ==========================

elif menu == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.write(
        "ClipAI Version 2.2"
    )

    st.write(
        "Developed by Ahmad"
    )
