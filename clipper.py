import subprocess
import os

def make_clip(input_path, output_path, duration=30):

    os.makedirs("outputs", exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-t", str(duration),
        "-vf", "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "28",
        "-c:a", "aac",
        "-b:a", "128k",
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path
