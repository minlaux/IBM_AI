import requests


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, headers=headers, json=input_data)

    if response.status_code == 200:
        result = response.json()
        return result['text']
    else:
        return f"Emotion detection request failed with status code: {response.status_code}"

# test
if __name__ == "__main__":
    text = "I love this new technology."
    result_text = emotion_detector(text)
    print("Emotion detected:", result_text)
