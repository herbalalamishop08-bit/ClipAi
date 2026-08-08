import os

from clipper import make_clip
from multi_clip import get_clip_points
from thumbnail import create_thumbnail


OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_clip(input_path, duration=30):

    filename = os.path.basename(input_path)

    clips = []

    clip_points = get_clip_points()

    for start_time in clip_points:

        output_path = os.path.join(
            OUTPUT_FOLDER,
            f"clip_{start_time}_{filename}"
        )

        make_clip(
            input_path,
            output_path,
            duration,
            start_time
        )

        thumbnail_path = create_thumbnail(
            output_path
        )

        clips.append({
            "video": output_path,
            "thumbnail": thumbnail_path
        })

    return {
        "status": "success",
        "message": f"✅ {len(clips)} clip berhasil dibuat",
        "outputs": clips
    }


def generate_subtitle(input_path):

    return "Coming Soon"
