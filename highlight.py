import os

from scenedetect import detect, ContentDetector


def detect_highlights(
    input_path,
    max_clips=3,
    min_duration=15,
    max_duration=60
):

    scenes = detect(
        input_path,
        ContentDetector(
            threshold=27.0,
            min_scene_len=15
        )
    )

    highlights = []

    for start, end in scenes:

        start_time = start.get_seconds()
        end_time = end.get_seconds()

        duration = end_time - start_time

        if duration < min_duration:
            continue

        if duration > max_duration:
            duration = max_duration

        highlights.append({
            "start": start_time,
            "duration": duration
        })

        if len(highlights) >= max_clips:
            break

    return highlights
