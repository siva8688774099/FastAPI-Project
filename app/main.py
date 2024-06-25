from fastapi import Depends, FastAPI

# from session import SessionData, cookie, backend, verifier
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

# from uuid import UUID, uuid4
from router import image_upload_route, user_login_route, user_regiration_route,cascase_route,table_api_route

origins = [
    "http://127.0.0.1:5500",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="secret-key")

app.include_router(user_login_route.router)
app.include_router(user_regiration_route.router)
app.include_router(image_upload_route.router)
app.include_router(cascase_route.router)
app.include_router(table_api_route.router)

@app.get("/whoami")
async def whoami(request: Request):
    return request.session["email"]
