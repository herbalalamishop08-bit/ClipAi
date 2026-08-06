import os
from clipper import make_clip

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_clip(input_path, duration=30, start_time=0):

    filename = os.path.basename(input_path)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"clip_{filename}"
    )

    make_clip(
        input_path=input_path,
        output_path=output_path,
        duration=duration,
        start_time=start_time
    )

    return {
        "status": "success",
        "message": "✅ Clip berhasil dibuat",
        "output": output_path
    }


def generate_subtitle(input_path):
    return "Fitur subtitle akan segera hadir."
