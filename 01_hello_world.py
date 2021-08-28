"""
A simple app, serving some data on /foo
"""

from _util import app


@app.get("/foo")
async def foo():
    return {"foo": 100}


"""
unvicorn 01_hello_world:foo --reload
swagger @ localhost:8000/docs
redocs @ localhost:8000/redocs
(.venv)  si@ubuntu  ~/workspaces/introduction-to-fastapi   main ±✚  curl localhost:8000/foo
{"foo":100}
"""
