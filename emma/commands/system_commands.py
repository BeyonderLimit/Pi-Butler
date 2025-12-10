# commands/system_commands.py
from datetime import datetime
import os

def get_time():
    return "It is " + datetime.now().strftime("%I:%M %p") + ", sir."

def get_date():
    return "Today is " + datetime.now().strftime("%A, %B %d %Y") + ", sir."

def get_status():
    return "All systems are operational, sir."

def capabilities():
    return (
        "I can respond to voice commands, set reminders, "
        "perform calculations, scan files, launch applications, "
        "and help with planning tasks, sir."
    )

def set_volume(text):
    import re, os
    pct = re.findall(r"\d+", text)
    if pct:
        pct = pct[0]
        os.system(f"amixer set Master {pct}%")
        return f"Volume set to {pct} percent, sir."
    return "Unable to determine the desired volume, sir."

