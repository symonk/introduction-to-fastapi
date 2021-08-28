"""
Build a simple app instance
"""

from fastapi import FastAPI


# As this is a tutorial; this is designed to be called on a per file basis with uvicorn each time, not reused.
app = FastAPI()