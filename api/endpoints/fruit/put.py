from db import SESSION
from fastapi.responses import PlainTextResponse
from loguru import logger
from models import Fruit
# pylint: disable=E0611
from pydantic import BaseModel


class Payload(BaseModel):
    name: str
    count: int


DOC = {
    200: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": "OK"}},
    },
    400: {
        "description": "Object not exist or encounter DB connection issues",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


def put(payload: Payload):
    try:
        fruit: Fruit = SESSION.query(Fruit).filter(Fruit.name == payload.name).one()
        fruit.count = payload.count
        SESSION.commit()
        return PlainTextResponse("OK", 200)
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)
