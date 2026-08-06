import subprocess
import os

def make_clip(input_file, output_file, duration=30):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_file
    ], check=True)
