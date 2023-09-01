from sqlalchemy.orm import Session
import models
import schemas


def get_audio(db: Session, audio_id: int):
    return db.query(models.Audio).filter(models.Audio.id == audio_id).first()


def get_audios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Audio).offset(skip).limit(limit).all()


def create_audio(db: Session, audio: schemas.AudioCreate):
    db_audio = models.Audio(**audio.dict())
    db.add(db_audio)
    db.commit()
    db.refresh(db_audio)
    return db_audio
