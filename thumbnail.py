import subprocess
import os


def generate_thumbnail(input_path, output_path):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-ss", "3",
        "-i", input_path,
        "-frames:v", "1",
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path
