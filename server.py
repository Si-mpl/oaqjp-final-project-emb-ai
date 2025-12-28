from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)
    printSentence = ""
    for key, value in output.items():
        if key != 'dominant_emotion':
            printSentence += f"'{key}': {value}, "
        else:
            printSentence = printSentence[:-2] + f". The dominant emotion is {value}."
    return f"For the given statement, the system reponse is {printSentence}"

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")