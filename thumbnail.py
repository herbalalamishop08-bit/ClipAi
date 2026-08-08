import os
import subprocess


THUMBNAIL_FOLDER = "outputs/thumbnails"

os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)


def create_thumbnail(video_path):

    filename = os.path.splitext(
        os.path.basename(video_path)
    )[0]

    thumbnail_path = os.path.join(
        THUMBNAIL_FOLDER,
        f"{filename}.jpg"
    )

    command = [
        "ffmpeg",
        "-y",
        "-ss", "1",
        "-i", video_path,
        "-frames:v", "1",
        "-q:v", "2",
        thumbnail_path
    ]

    subprocess.run(
        command,
        check=True
    )

    return thumbnail_path
