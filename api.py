from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/out", StaticFiles(directory="out"), name="out")

