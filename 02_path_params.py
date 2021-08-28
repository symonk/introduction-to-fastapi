"""
Add path parameters to an endpoint
"""

from fastapi import FastAPI

app = FastAPI(title="path_params")


@app.get("/foo/{bar}")
def foo(bar: int):
    return {"foo": bar}

"""
(.venv)  si@ubuntu  ~/workspaces/introduction-to-fastapi   main ±✚  curl localhost:8000/foo/"100" 
{"foo":100}

Note the type hints here, automatically provide request parsing to the types!
"""