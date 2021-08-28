"""
Parse query parameters from a reqest
"""

from _util import app


@app.get("/foo/{bar}")
async def foo(bar: int = 0, baz: int = 0):
    # Anything not defined in the path is considered a query string parameter
    return {
        "path": bar,
        "query": baz
    }

"""
✘  (.venv)  si@ubuntu  ~/workspaces/introduction-to-fastapi   main ±✚  curl 'localhost:8000/foo/100?baz=10'
{"path":100,"query":10}
"""