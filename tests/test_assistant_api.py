import os
import sys
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
os.environ.setdefault("GEMINI_API_KEY", "test-key")
os.environ.setdefault("GEMINI_MODEL", "gemini-pro")

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.api import assistant as assistant_api
from app.main import app
from fastapi.testclient import TestClient


class DummyAssistant:
    def chat(self, analysis, history, message):
        return SimpleNamespace(answer=f"reply:{message}")


def override_get_current_user():
    return SimpleNamespace(id=uuid4())


def override_get_db():
    return None


def override_get_project_assistant():
    return DummyAssistant()


def override_get_user_project(*args, **kwargs):
    return SimpleNamespace(id=uuid4())


def override_get_project_analysis(*args, **kwargs):
    return SimpleNamespace(
        summary="Test summary",
        detected_technologies="FastAPI, SQLAlchemy",
    )


app.dependency_overrides[assistant_api.get_current_user] = override_get_current_user
app.dependency_overrides[assistant_api.get_db] = override_get_db
app.dependency_overrides[assistant_api.get_project_assistant] = override_get_project_assistant
assistant_api.get_user_project = override_get_user_project
assistant_api.get_project_analysis = override_get_project_analysis

client = TestClient(app)


def test_assistant_endpoint_returns_reply():
    project_id = uuid4()

    response = client.post(
        f"/assistant/{project_id}",
        json={
            "message": "Hello",
            "history": {"messages": []},
        },
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "reply:Hello"
