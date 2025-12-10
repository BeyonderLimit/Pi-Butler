# core/speech_output.py
import subprocess
import tempfile

class EmmaVoice:
    def speak(self, text):
        with tempfile.NamedTemporaryFile(delete=True) as f:
            cmd = ["piper", "--model", "emma.onnx", "--output", f.name]
            subprocess.run(cmd, input=text.encode("utf-8"))
            subprocess.run(["aplay", f.name])
