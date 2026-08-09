import os

from clipper import make_clip
from highlight import detect_highlights
from thumbnail import create_thumbnail


OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_clip(input_path, duration=30):

    filename = os.path.basename(input_path)

    clips = []

    highlights = detect_highlights(
        input_path,
        max_clips=3,
        min_duration=15,
        max_duration=duration
    )

    # Jika scene detection tidak menemukan scene yang cocok,
    # gunakan titik cadangan 0, 30, 60.
    if not highlights:

        highlights = [
            {
                "start": 0,
                "duration": duration
            },
            {
                "start": duration,
                "duration": duration
            },
            {
                "start": duration * 2,
                "duration": duration
            }
        ]

    for i, highlight in enumerate(highlights, start=1):

        start_time = highlight["start"]
        clip_duration = min(
            highlight["duration"],
            duration
        )

        output_path = os.path.join(
            OUTPUT_FOLDER,
            f"highlight_{i}_{filename}"
        )

        make_clip(
            input_path,
            output_path,
            clip_duration,
            start_time
        )

        thumbnail_path = create_thumbnail(
            output_path
        )

        clips.append({
            "video": output_path,
            "thumbnail": thumbnail_path,
            "start": start_time,
            "duration": clip_duration
        })

    return {
        "status": "success",
        "message": f"✅ {len(clips)} highlight clip berhasil dibuat",
        "outputs": clips
    }


def generate_subtitle(input_path):

    return "Coming Soon"
