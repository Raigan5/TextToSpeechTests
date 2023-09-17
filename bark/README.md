# Evaluation of Bark for Text-to-Speech on my local computer:

## Software used

[Bark](https://github.com/suno-ai/bark) *Bark is a transformer-based text-to-audio model... can generate highly realistic, multilingual speech... can also produce nonverbal communications like laughing, sighing and crying... Bark was developed for research purposes... which can deviate in unexpected ways from provided prompts.*

It's available on [Hugging Face](https://huggingface.co/spaces/suno/bark)

## Methodology

Bark uses PyTorch and it needs a GPU compatible with CUDA to run smoothly, but I don't have such a GPU, so I installed the version that uses CPU.

I tried to say "Hello" with the small model.

## Initial Results

- **Conversion's speed**: with my CPU (amd 3600x), it's way too slow. I should try it on [Google Colab](https://colab.research.google.com)
- **Cost**: free
- **Can it run on my local computer without sending information?**: yes
- **Parametrizable (gender, dialect, speed,...)**: I wasn't able to test it.
- **Limits**: I wasn't able to test it.
