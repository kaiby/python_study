"""
tts_test - 

Author: kaiby
Date: 2024/5/31 17:21
"""

import ChatTTS
from IPython.display import Audio

chat = ChatTTS.Chat()
chat.load_models()

texts = ["<PUT YOUR TEXT HERE>"]

wavs = chat.infer(texts, use_decoder=True)
Audio(wavs[0], rate=24_000, autoplay=True)
