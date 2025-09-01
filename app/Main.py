from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home_page():
    name = os.getenv("NAME")
    age = 28
    return f"This is home page ${name}"


@app.get("/health")
def app_health():
    return 'App is up and running fine! - sp1'

@app.get("/project-name")
def get_app_name():
    return "App Bsic-Python-App using FastAPI"


