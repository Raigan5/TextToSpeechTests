from transformers import AutoProcessor, BarkModel
#pip install git+https://github.com/huggingface/transformers.git
#https://pytorch.org/get-started/locally/
#In my case: pip3 install torch torchvision torchaudio

import scipy

#https://github.com/suno-ai/bark#how-much-vram-do-i-need
import os
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

voice_preset = "v2/en_speaker_6"

inputs = processor("Hello", voice_preset=voice_preset)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()

sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write('bark_out.wav', rate=sample_rate, data=audio_array)