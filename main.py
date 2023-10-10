# main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Video
from database import engine

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.post("/upload/")
async def upload_video(file: UploadFile, title: str, description: str):
    with SessionLocal() as db:
        db_video = Video(title=title, description=description, file_path=file.filename)
        db.add(db_video)
        db.commit()

    with open(f"videos/{file.filename}", "wb") as f:
        f.write(file.file.read())

    return {"message": "Video uploaded successfully"}

@app.get("/videos/")
async def list_videos():
    with SessionLocal() as db:
        videos = db.query(Video).all()
    return videos
