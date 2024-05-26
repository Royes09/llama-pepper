
import speech_recognition as sr
import pyaudio
import wave

def record (): 
    chunk = 1024 
    sample_format = pyaudio.paInt16  
    channels = 2
    fs = 44100  
    seconds = 3
    filename = "output.wav"
    p = pyaudio.PyAudio()  
    print('Recording')
    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
    frames = []  
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data) 
    stream.stop_stream()
    stream.close()
    p.terminate()   
    print('Finished recording')
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
def trascribe () :
    r = sr.Recognizer()
    with sr.AudioFile('output.wav') as source:
            audio_text = r.listen(source)   
    try:       
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')

record()
trascribe()