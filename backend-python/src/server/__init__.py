from pathlib import Path

from .main import create_app

app_dist = Path(__file__).parents[2] / "frontend" / "dist"
app = create_app(app_dist)
