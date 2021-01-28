from db import SESSION
from fastapi.responses import JSONResponse, PlainTextResponse
from loguru import logger
from models import Fruit

DOC = {
    200: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": {"name": "apple", "count": 1}}},
    },
    400: {
        "description": "Object not exists or encounter DB connection issues",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


def get(name: str):
    try:
        fruit: Fruit = SESSION.query(Fruit).filter(Fruit.name == name).one()
        return JSONResponse(fruit.dumps(), 200)
    except Exception as error:
        SESSION.rollback()
        logger.error(error)
        return PlainTextResponse("Bad Request", 400)
