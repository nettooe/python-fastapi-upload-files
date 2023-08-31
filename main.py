from typing import Annotated, Optional
from starlette.types import Message


import fastapi
import starlette
from fastapi import FastAPI, File, UploadFile, Form, Depends, Request
from starlette.datastructures import FormData


app = FastAPI()


@app.post("/files")
async def create_files(request: fastapi.Request):
    form = await request.form()

    dict_to_return: dict = {}

    # primeiro campo
    a_optional = form.get('a_optional')
    if a_optional is not None:
        dict_to_return["a_optional_size"] = a_optional.size

    # segundo campo
    b_optional = form.get('b_optional')
    if b_optional is not None:
        dict_to_return["b_optional_size"] = b_optional.size

    # terceiro campo, mas considerando como lista
    # atenção aqui, pois é 'getlist'
    list_repeat_optional = form.getlist('repeat_optional')

    if list_repeat_optional is not None:
        counter: int = 0
        for item in list_repeat_optional:
            if isinstance(item, starlette.datastructures.UploadFile):
                arquivo: UploadFile = item
                print(arquivo.size)
                dict_to_return[f"repeat_optional_{counter}_size"] = arquivo.size
                counter += 1

    return dict_to_return
