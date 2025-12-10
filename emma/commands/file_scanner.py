# commands/file_scanner.py
import glob
import os

def scan(text):
    if "*.md" in text:
        files = glob.glob("**/*.md", recursive=True)
        return f"Found {len(files)} markdown files, sir."
    return "Specify a file pattern, sir."
