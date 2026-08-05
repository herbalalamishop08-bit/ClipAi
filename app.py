import streamlit as st
import os
from clipper import make_clip

st.set_page_config(
    page_title="ClipAI",
    page_icon="🎬",
    layout="wide"
)

os.makedirs("uploads", exist_ok=True)

# ===== Sidebar =====
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

# ===== Dashboard =====
if menu == "🏠 Dashboard":
    st.title("🎬 ClipAI Dashboard")
    st.write("Selamat datang di ClipAI!")

# ===== Upload =====
elif menu == "📤 Upload":
    st.title("📤 Upload Video")

    uploaded = st.file_uploader(
        "Pilih Video",
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

# ===== My Videos =====
elif menu == "📂 My Videos":
    st.title("📂 Video Saya")

    videos = [
        f for f in os.listdir("uploads")
        if f.endswith((".mp4", ".mov", ".avi", ".mkv"))
        and not f.startswith("clip_")
    ]

    if videos:
        for video in videos:
            st.write(f"🎥 {video}")
    else:
        st.info("Belum ada video.")

# ===== Results =====
elif menu == "📥 Results":
    st.title("📥 Hasil Clip")

    clips = [
        f for f in os.listdir("uploads")
        if f.startswith("clip_")
    ]

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

# ===== Settings =====
elif menu == "⚙️ Settings":
    st.title("⚙️ Pengaturan")
    st.write("Fitur pengaturan akan segera hadir.")
