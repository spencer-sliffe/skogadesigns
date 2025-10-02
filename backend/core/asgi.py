import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

# Load backend/.env if present
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_SETTINGS_MODULE", "core.settings.local"),
)

application = get_asgi_application()
