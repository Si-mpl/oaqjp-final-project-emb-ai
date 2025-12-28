import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=jsonobj, headers=headers)
    formattedjson = response.json()

    formatted = formattedjson['emotionPredictions'][0]['emotion']
    formatted["dominant_emotion"] = max(formatted, key=formatted.get)

    return formatted



'''
from emotion_detection import emotion_detector
emotion_detector("I am so happy I am doing this")
'''