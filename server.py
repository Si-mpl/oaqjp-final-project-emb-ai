''' 
This script will render the index page and handle all the emotion detector activities
that show emotions
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    ''' this function will utilize the emotion detector to determine the 
    emotion of the sentence and display it '''

    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    printsentence = ""
    for key, value in output.items():
        if key != 'dominant_emotion':
            printsentence += f"'{key}': {value}, "
        else:
            printsentence = printsentence[:-2] + f". The dominant emotion is {value}."
    return f"For the given statement, the system reponse is {printsentence}"

@app.route("/")
def render_index_page():
    ''' this function render the index page '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
