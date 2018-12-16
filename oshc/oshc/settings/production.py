# production settings
from .base import *


DEBUG = os.getenv("DEBUG", False)
