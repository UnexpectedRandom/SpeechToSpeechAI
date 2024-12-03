# This will be your entry point for integrating everything.

import torch
import pyaudio
import numpy as np
import librosa
import wave
import os
import logging
from stt_model import SpeechToTextModel
from nlp_model import NLPModel
from tts_model import TextToSpeechModel
