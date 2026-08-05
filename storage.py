import os

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def save_video(uploaded_file):
    path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return path


def get_videos():
    return [
        f for f in os.listdir(UPLOAD_FOLDER)
        if f.endswith((".mp4", ".mov", ".avi", ".mkv"))
    ]


def get_clips():
    return [
        f for f in os.listdir(OUTPUT_FOLDER)
        if f.endswith(".mp4")
    ]
