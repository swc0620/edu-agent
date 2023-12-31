""" module docstring """
import io
import os
from typing import Union
from time import time

import openai
from dotenv import load_dotenv
from fastapi import FastAPI, status, UploadFile, Form, File, HTTPException, Depends
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# from db import engine, SessionLocal
from ml import SummaryModel
import models

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
WHISPER_MODEL = "whisper-1"
summary_model = SummaryModel()

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
handler = Mangum(app)

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# def store_summary(db: SessionLocal, summary: str) -> models.Audio:
#     db_audio = models.Audio(summary=summary)
#     db.add(db_audio)
#     db.commit()
#     db.refresh(db_audio)

#     return db_audio


class NamedBytesIO(io.BytesIO):
    """A BytesIO subclass that has a name attribute"""

    def __init__(self, buffer, name=None):
        super().__init__(buffer)
        self.name = name


def read_audio_file(audio_file: UploadFile):
    """Read audio file"""
    print("Read Audio File")
    audio = audio_file.file.read()
    contents = NamedBytesIO(audio, name=audio_file.filename)
    return send_to_openai(contents)


def send_to_openai(audio):
    """Send audio to OpenAI"""
    print("Send audio to OpenAI")
    start_time = time()
    resp = openai.Audio.transcribe(
        file=audio,
        model=WHISPER_MODEL,
    )
    end_time = time()
    print(f"Audio Transribe Time: {end_time-start_time}s")
    
    print("Run Summary Model")
    summary_result = summary_model.run(resp.text)
    
    return summary_result


@app.get(
    '/',
    summary='Test root endpoint',
    description='Test root endpoint provided for automatic health checks.'
)
async def get_root():

    return {
        'info': 'edu-agent-api endpoint is healthy and running.'
    }

@app.get("/healthz")
def healthz():
    """Health check endpoint"""
    return Response(status_code=status.HTTP_200_OK)


@app.post("/audio")
def upload_audio(audio_file: UploadFile = File(...)):
    """Upload audio file endpoint"""
    if not audio_file or audio_file.filename.split('.')[-1] not in ["mp3", "mp4"]:
        raise HTTPException(status_code=400, detail="Invalid file format. Only mp3 and mp4 are supported.")

    # summary_text=await run_in_threadpool(read_audio_file, audio_file)
    summary_text=read_audio_file(audio_file)

    # db_audio = store_summary(db, summary_text)
    # print(db_audio)

    # return JSONResponse(status_code=status.HTTP_201_CREATED, content={ "id": db_audio.id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"summary_text": summary_text})


@app.get("/audio/{audio_id}")
async def polling_audio(audio_id: Union[str, int]):
    """Polling audio file endpoint"""
    return JSONResponse(status_code=status.HTTP_200_OK, content={"audio_id": audio_id})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
