"""
Flask web server for Emotion Detection application.
Provides REST API endpoint for emotion analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__,
            template_folder='oaqjp-final-project-emb-ai/templates',
            static_folder='oaqjp-final-project-emb-ai/static')


@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def analyze_emotion():
    """
    Analyze emotion in provided text.
    
    Returns:
        str: Formatted analysis or error message.
    """
    text_input = request.args.get('textToAnalyze')

    if not text_input or not text_input.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_input)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    