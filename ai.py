import os
import re
import google.generativeai as genai
from clipper import make_clip

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def get_best_start_time(filename):
    prompt = f"""
Video berdurasi beberapa menit.

Tentukan detik terbaik untuk membuat video viral berdurasi pendek.

Jawab HANYA ANGKA.
Contoh:
25
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    match = re.search(r"\d+", text)

    if match:
        return int(match.group())

    return 0


def generate_clip(input_path, duration=30):

    filename = os.path.basename(input_path)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"clip_{filename}"
    )

    start_time = get_best_start_time(filename)

    make_clip(
        input_path,
        output_path,
        duration,
        start_time
    )

    return {
        "status": "success",
        "message": f"✅ Clip dibuat dari detik {start_time}",
        "output": output_path
    }


def generate_subtitle(input_path):
    return "Coming Soon"
