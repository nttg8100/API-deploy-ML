# Importing Necessary modules
from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

filename = 'models/finalized_model.sav'
clf = pickle.load(open(filename, 'rb'))


# Define class for return result
class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Labels the output results
output = ['setosa', 'versicolor', 'virginica']


# Defining path operation for root endpoint
# GET
@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}


# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to GeeksforGeeks!, {name}'}


# POST
@app.post('/predict')
def predict(data: request_body):
    test_data = [[
        data.sepal_length, data.sepal_width, data.petal_length,
        data.petal_width
    ]]
    class_idx = clf.predict(test_data)[0]
    return {'class': output[class_idx]}