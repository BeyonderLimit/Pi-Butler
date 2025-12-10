# core/nlp_engine.py
import re

class NLP:
    def parse(self, text):
        text = text.lower().strip()

        # Comprehensive intent matching
        intents = {
            "hello": "greet",
            "hi emma": "greet",
            "hey emma": "greet",
            "emma": "greet",
            "who are you": "identity",
            "what are you": "identity",
            "identify yourself": "identity",
            "what can you do": "capabilities",
            "help": "help",
            "help me": "help",
            "assist": "help",
            "bye": "standby",
            "sleep": "standby",
            "what time": "time",
            "time is it": "time",
            "what date": "date",
            "date is it": "date",
            "status": "status",
            "calculate": "math",
            "set timer": "timer",
            "remind": "reminder",
            "set a reminder": "reminder",
            "launch": "launch_app",
            "open": "launch_app",
            "scan": "file_scan",
            "find": "file_scan",
            "volume": "volume",
            "prioritize": "task_priority",
            "plan": "planning",
        }

        for key, intent in intents.items():
            if key in text:
                return {"intent": intent, "text": text}

        # fallback to unknown
        return {"intent": "unknown", "text": text}

