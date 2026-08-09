import whisper


MODEL_NAME = "tiny"

_model = None


def get_model():

    global _model

    if _model is None:
        _model = whisper.load_model(MODEL_NAME)

    return _model


def generate_subtitle(input_path):

    model = get_model()

    result = model.transcribe(
        input_path,
        language="id",
        fp16=False
    )

    return result
