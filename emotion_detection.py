import requests


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_data = { 
        "raw_document": { "text": text_to_analyse } 
    }
    
    response = requests.post(url, headers=headers, json=input_data)

    if response.status_code == 200:
        result = response.json()
        emotions = result.get('raw_emotion', {}).get('scores', {})
        
        dominant_emotion, _ = find_dominant_emotion(emotions)
        
        emotions['dominant_emotion'] = dominant_emotion
        
        return emotions
    else:
        return f"Emotion detection request failed with status code: {response.status_code}"



def find_dominant_emotion(emotions):
    # find emotion with highest score
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
    
    return dominant_emotion, dominant_score


# test
if __name__ == "__main__":
    text = "I am so happy doing this."
    emotion_scores = emotion_detector(text)
    
    print(emotion_scores)