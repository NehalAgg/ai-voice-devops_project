import requests
from voice import get_voice

text = get_voice()
print("You said:", text)

if text != "error":
    res = requests.post(
        "http://127.0.0.1:8000/predict",
        params={"text": text}
    )
    print("Prediction:", res.json())
else:
    print("Voice not recognized")