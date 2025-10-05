# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# serve your built React app
app.mount("/", StaticFiles(directory="react_templates/react-app/dist", html=True), name="frontend")