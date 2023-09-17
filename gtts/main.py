from flask import Flask, request, jsonify, render_template
from gtts import gTTS
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    try:
        text = request.form.get('text')
        if text:
            tts = gTTS(text)

            audio_dir = 'static/audio'
            os.makedirs(audio_dir, exist_ok=True)

            audio_file_path = os.path.join(audio_dir, 'output.mp3')
            tts.save(audio_file_path)

            audio_url = '/static/audio/output.mp3'
            return jsonify({'success': True, 'audio_url': audio_url})
        else:
            return jsonify({'success': False, 'message': 'No text provided'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
