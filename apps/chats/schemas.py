"""
title: не пустой, длина 1..200

пробелы по краям должны триммиться (опционально, но приветствуется)

text: не пустой, длина 1..5000
"""
from typing import Annotated

from pydantic import BaseModel, StringConstraints


class ChatCreateSchema(BaseModel):
    title: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=200)
    ]


class MessageCreateSchema(BaseModel):
    text: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=5000)
    ]
