from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.config import settings


app = FastAPI(
    title="SDE Round API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

print("DATABASE URL:", settings.DATABASE_URL)


@app.get("/db-health")
def database_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "connected"
    }