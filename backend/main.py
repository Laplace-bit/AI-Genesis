from fastapi import FastAPI
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

from routers import timeline, empowerment, inspiration, auth, comments

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(timeline.router, prefix="/api/v1", tags=["timeline"])
app.include_router(empowerment.router, prefix="/api/v1", tags=["empowerment"])
app.include_router(inspiration.router, prefix="/api/v1", tags=["inspiration"])
app.include_router(comments.router, prefix="/api/v1", tags=["comments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Genesis Backend"}
