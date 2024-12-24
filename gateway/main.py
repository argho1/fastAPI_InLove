import os
import sys
import logging


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log", level=logging.INFO)

root_path = os.environ.get("ROOT_PATH", "")
if root_path is None:
    sys.exit("\033[91m ROOT_PATH is not set \003[0m")

app = FastAPI(
    title="InLove API",
    description="Backend API for InLove Website",
    version="1.0.0"
)

init_telemetry(app)


