from clipper import make_clip
import os

OUTPUT_FOLDER = "uploads"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_clip(input_path):

    filename = os.path.basename(input_path)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"clip_{filename}"
    )

    make_clip(input_path, output_path)

    return {
        "status": "success",
        "message": "✅ Clip berhasil dibuat",
        "output": output_path
    }


def generate_subtitle(input_path):
    return "Subtitle akan segera tersedia."
