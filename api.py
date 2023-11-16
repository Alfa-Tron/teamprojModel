from fastapi import FastAPI
from main import translator
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'OK'}


@app.post('/translate/')
def translate(item: Item):
    return {'Translated text': translator(item.text)[0]['translation_text']}
