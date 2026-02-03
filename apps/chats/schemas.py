"""
title: не пустой, длина 1..200

пробелы по краям должны триммиться (опционально, но приветствуется)

text: не пустой, длина 1..5000
"""
from pydantic import BaseModel, Field, field_validator


class ChatCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, strip_whitespace=True)

    @field_validator('title')
    def validate_title(cls, v):
        stripped = v.strip()
        if not stripped:
            raise ValueError("Название чата не может состоять из пробелов")
        return stripped


class MessageCreateSchema(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, strip_whitespace=True)

    @field_validator('text')
    def validate_text(cls, v):
        stripped = v.strip()
        if not stripped:
            raise ValueError("Сообщение не может быть пустым")
        return stripped
