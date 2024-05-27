import sounddevice
from scipy.io.wavfile import write
import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def output_device ():
    fs= 44100
    print("Recording.....n")
    record_voice = sounddevice.rec( int ( 10 * fs ) , samplerate = fs, channels = 2 )
    sounddevice.wait()
    write("out.wav", fs, record_voice)
    print("Finished.....nPlease check your output file")
    result = query("out.wav")
    text =str(result['text'])
    return text
