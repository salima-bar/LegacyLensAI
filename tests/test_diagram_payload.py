import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from app.api.analysis import build_diagram_payload


def test_build_diagram_payload_returns_reactflow_shape():
    diagram_data = {
        "nodes": [
            {
                "id": "user",
                "position": {"x": 0, "y": 0},
                "data": {"label": "User"},
            }
        ],
        "edges": [
            {"id": "e1", "source": "user", "target": "api"}
        ],
    }

    payload = build_diagram_payload(diagram_data)

    assert payload["nodes"][0]["id"] == "user"
    assert payload["nodes"][0]["position"] == {"x": 0, "y": 0}
    assert payload["edges"][0]["source"] == "user"
    assert payload["edges"][0]["target"] == "api"
