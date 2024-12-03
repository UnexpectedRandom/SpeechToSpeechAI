import torch
import numpy as np

# https://huggingface.co/docs/transformers/en/model_doc/t5
from transformers import T5ForConditionalGeneration, T5Tokenizer
# https://docs.python.org/3/library/wave.html
import wave
# https://librosa.org/doc/latest/index.html
import librosa