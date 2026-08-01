from app.api.analysis import router as analysis_router
from app.api.assistant import router as assistant_router
from app.api.auth import router as auth_router
from app.api.projects import router as projects_router
from app.api.users import router as users_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(projects_router)
app.include_router(analysis_router)
app.include_router(assistant_router)


@app.get("/")
def root():
    return {"message": "Welcome to LegacyLensAI API"}