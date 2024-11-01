import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import text



model_path = '/C:/Users/NGALANDM/Downloads/universal_sentence_encoder.tflite'



import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
TextEmbedder = mp.tasks.text.TextEmbedder
TextEmbedderOptions = mp.tasks.text.TextEmbedderOptions

# For creating a text embedder instance:
options = TextEmbedderOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    quantize=True)
text_embedder = TextEmbedder.create_from_model_path(options)
    
input_text = "The input text to be embedded."

# Perform text embedding on the provided input text.
embedding_result = text_embedder.embed(input_text)

print(embedding_result)

