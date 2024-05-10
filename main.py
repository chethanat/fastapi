from fastapi import FastAPI
from core.config import Settings

# object of class
app = FastAPI(title=Settings.PROJECT_TITLE , version=Settings.PROJECT_VERSION)


# decorator to call the api
@app.get('/')
def hello():
    return {"msg": "Hello FastAPI"}
