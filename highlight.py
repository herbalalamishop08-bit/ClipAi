import random


def get_highlight(video_duration, clip_duration=30):

    if video_duration <= clip_duration:
        return 0

    return random.randint(
        0,
        video_duration - clip_duration
    )
