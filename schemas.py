from typing import Union

from pydantic import BaseModel


class AudioBase(BaseModel):
    summary: Union[str, None] = None


class AudioCreate(AudioBase):
    pass


class Audio(AudioBase):
    id: int

    class Config:
        orm_mode = True
