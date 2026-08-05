import subprocess
import os

def make_clip(input_file, output_file):
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-t", "30",
        "-c:v", "libx264",
        "-c:a", "aac",
        output_file
    ], check=True)
