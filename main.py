# Importing Necessary modules
import pickle, uvicorn, inspect
from typing import Dict, Type
from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory = "")

filename = 'models/finalized_model.sav'
clf = pickle.load(open(filename, 'rb'))

# Labels the output results
output = ['setosa', 'versicolor', 'virginica']

def as_form(cls: Type[BaseModel]):
    new_params = [
        inspect.Parameter(
            field.alias,
            inspect.Parameter.POSITIONAL_ONLY,
            default=(Form(field.default) if not field.required else Form(...)),
            annotation=field.outer_type_,
        )
        for field in cls.__fields__.values()
    ]

    async def _as_form(**data):
        return cls(**data)

    sig = inspect.signature(_as_form)
    sig = sig.replace(parameters=new_params)
    _as_form.__signature__ = sig
    setattr(cls, "as_form", _as_form)
    return cls

@as_form
class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}

@app.get('/input', response_class = HTMLResponse)
def input(request: Request):
    return templates.TemplateResponse('form.html', context = {'request': request, 'result': ''})

@app.post('/input', response_class = HTMLResponse, response_model = request_body)
def input(request: Request, data: request_body = Depends(request_body.as_form)):
    test_data = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    class_idx = clf.predict(test_data)[0]
    return templates.TemplateResponse('form.html', context = {'request': request, 'result': output[class_idx]})

if __name__ == '__main__':
    uvicorn.run("main:app", reload = True)