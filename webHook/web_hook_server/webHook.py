from fastapi import FastAPI
from schemas.user_schema import user_schema
import requests


app = FastAPI()

@app.post("/webhook")
def newUser(user: user_schema):
    response = requests.post("https://webhook.site/5d7f9e23-14e8-448b-9beb-516304c0bcc9", data=json.dumps(payload), headers={'Content-Type' : 'application/json'})