# commands/app_launcher.py 
import os

def launch(text):
    if "vlc" in text:
        os.system("vlc &")
        return "Launching VLC now, sir."
    return "I cannot launch that application, sir."
