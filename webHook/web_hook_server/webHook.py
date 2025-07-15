from fastapi import FastAPI
from schemas.user_schema import user_schema
import requests


app = FastAPI()

@app.post("/webhook")
def newUser(user: user_schema):
    response = requests.post(user.url_user, data=json.dumps(user), headers={'Content-Type' : 'application/json'})