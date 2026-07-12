from fastapi import FastAPI
from routes import api_router
from core.config import settings
from core.exceptions import register_exception_handlers

app = FastAPI(title=settings.app_name, debug=settings.debug)

register_exception_handlers(app)
app.include_router(api_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Now I am a Python Developer."}
