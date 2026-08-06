import subprocess
import os


def make_clip(input_file, output_file, duration=30, start_time=0):

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-threads", "1",
        "-ss", str(start_time),
        "-i", input_file,
        "-t", str(duration),
        "-vf", "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "28",
        "-c:a", "aac",
        "-b:a", "128k",
        output_file
    ]

    subprocess.run(command, check=True)
