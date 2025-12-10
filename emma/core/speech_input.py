# core/speech_input.py
import json, queue, sounddevice as sd
from vosk import Model, KaldiRecognizer

class SpeechInput:
    def __init__(self):
        self.model = Model("models/vosk")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.q = queue.Queue()

    def audio_callback(self, indata, frames, time, status):
        self.q.put(bytes(indata))

    def listen(self):
        with sd.RawInputStream(samplerate=16000, blocksize=8000,
                               dtype='int16', channels=1,
                               callback=self.audio_callback):
            print("Listening...")
            while True:
                data = self.q.get()
                if self.rec.AcceptWaveform(data):
                    result = json.loads(self.rec.Result())
                    return result.get("text", "")
