import os
from dotenv import load_dotenv

__version__ = "v0.1.0"

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)
