# thirdparty
import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.responses import RedirectResponse

# project
from routers.lantern_router import lantern_router

# Define a root router
root_router = APIRouter(prefix="/api/v1")

# Define a FastAPI application
app = FastAPI(title="Lantern API", version="0.0.1")

# ===========ROUTER REGISTRATION===========#

# 1. LANTERN
root_router.include_router(lantern_router)

# =====================================#


# Connect a root router to an application
app.include_router(root_router)


# Redirect root URL to /docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


# # define exception handlers
# app.add_exception_handler(CustomHTTPException)


def openapi_specs():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Lantern",
        version="0.0.1",
        description="Lantern Open-API Specification",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = openapi_specs

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = "127.0.0.1"
        port = 9999

    uvicorn.run(app, host=host, port=port)
