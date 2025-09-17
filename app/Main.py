from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_page():
    return "This is home page"

@app.get("/health")
def app_health():
    return 'App is up and running D from qa'

@app.get("/project-name")
def get_app_name():
    return "Bsic-Python-App Main from dev"
