from pydantic import BaseModel
from fastapi import HTTPException, APIRouter, Response, Depends,status,Form
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
# from session import SessionData, cookie, backend
from database import get_db
from models.models import Users
from fastapi.responses import RedirectResponse
from starlette.requests import Request

router = APIRouter(tags=["User Registraion"])

templates = Jinja2Templates(directory="templates")

bcrypt_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


@router.get("/register")
async def register(request: Request):

    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register_user(
    request: Request,
    response: Response,
    username: str = Form(),
    email: str = Form(),
    mobile: str = Form(),
    password: str = Form(),
    db:Session=Depends(get_db)
):
    request.session["session"] = str(uuid4())
    request.session["email"] = email
    print(request.session["session"])
    user = db.query(Users).filter(Users.email == email).first()
    if user is not None:
        return templates.TemplateResponse(
            "user_already_present.html", {"request": request}
        )
    print(username, email, mobile, password)
    create_user_model = Users(
        username=username,
        email=email,
        mobile=mobile,
        hashed_password=bcrypt_context.hash(password),
    )
    print(create_user_model.hashed_password)

    db.add(create_user_model)
    db.commit()
    return RedirectResponse('login',status_code=status.HTTP_302_FOUND)\
