# emma/core/emma_brain.py
from core.speech_input import SpeechInput
from core.speech_output import EmmaVoice
from core.nlp_engine import NLP
from core.command_router import CommandRouter

class EmmaBrain:
    def __init__(self):
        self.speech = SpeechInput()
        self.voice = EmmaVoice()
        self.nlp = NLP()
        self.router = CommandRouter()

    def process(self, text: str):
        intent = self.nlp.parse(text)
        response = self.router.execute(intent)
        return response
    def run(self):
        print("EMMA online. Awaiting your command, sir.")
        while True:
            text = self.speech.listen()
            if not text:
                continue

            intent = self.nlp.parse(text)
            response = self.router.execute(intent)

            if response:
                self.voice.speak(response)
                print("EMMA:", response)
