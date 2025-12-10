# ui/api.py 
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.emma_brain import EmmaBrain
from core.speech_output import EmmaVoice
import uvicorn

emma = EmmaBrain()
voice = EmmaVoice()
app = FastAPI()

@app.post("/process")
async def process(data: dict):
    text = data["text"]
    response = emma.process(text)
    voice.speak(response)
    return {"response": response}

app.mount("/static", StaticFiles(directory="ui/static"), name="static")

@app.get("/")
async def root():
    return FileResponse("ui/index.html")

def start_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)
