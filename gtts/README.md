# Evaluation of gTTS for Text-to-Speech on my local computer:

## Software used

[gTTS](https://pypi.org/project/gTTS/) *(Google Text-to-Speech), a Python library and CLI tool to interface with* **Google Translate text-to-speech API**

## Methodology

I utilized a web to input the text that needed to be converted, and the conversion process was executed on the backend.

## Initial Results

- **Conversion's speed**: pretty fast
- **Cost**: free
- **Can it run on my local computer without sending information?**: It sends information to Google
- **Parametrizable (gender, dialect, speed,...)**: Take a look at [this](https://stackoverflow.com/questions/37600197/custom-python-gtts-voice)
- **Limits**: the results for short texts were good enough. However, further testing with longer texts is required to identify and address any [issues](https://github.com/pndurette/gTTS/issues/119)




