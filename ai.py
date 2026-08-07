import os

from clipper import make_clip
from multi_clip import get_clip_points

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_clip(input_path, duration=30):

    filename = os.path.basename(input_path)

    clips = []

    for start_time in get_clip_points():

        output_path = os.path.join(
            OUTPUT_FOLDER,
            f"{start_time}_{filename}"
        )

        make_clip(
            input_path,
            output_path,
            duration,
            start_time
        )

        clips.append(output_path)

    return {
        "status": "success",
        "message": "✅ 3 Clip berhasil dibuat",
        "outputs": clips
    }


def generate_subtitle(input_path):
    return "Coming Soon"
