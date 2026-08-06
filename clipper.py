import subprocess
import os

def make_clip(input_file, output_file, duration=30):

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-t", str(duration),
        "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        output_file
    ], check=True)
