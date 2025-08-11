from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def app_health():
    return 'App is up and running'

@app.get("/project-name")
def get_app_name():
    return "Bsic-Python-App"