from fastapi import APIRouter,status,Request,Form,Depends,Response
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,Response as Resp
from models.models import Users
from database import get_db

router = APIRouter(tags=["User Login"])

templates = Jinja2Templates(directory="templates")

bcrypt_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


@router.get("/",status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def template(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


@router.get("/login")
async def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})



@router.post("/login")
async def login_for_access_token(request: Request,email=Form(),
        password=Form(),db:Session = Depends(get_db)):
    """
    The login_for_access_token function is used to authenticate a user and return an access token.

    :param request:Request: Get the request body
    :param db:db_dependency
    email: Get the email from the request body
    :param password: Get the password from the request body
    :param : Get the data from the request body
    :return: A dictionary with the access_token and token_type keys
    :doc-author: Trelent
    """
    result = db.query(Users).where(Users.email == email).first()
    user = bcrypt_context.verify(password, result.__dict__["hashed_password"])
    print(user)
    if not user:
        return Resp(content="<h1 >UnAuthorized</h1>",status_code=status.HTTP_401_UNAUTHORIZED)  # noqa: E999

    if request.session.get("session") is None:
        request.session["email"] = email
        print(request.session["email"])
        context = result.__dict__
        print(f"context : {context.get('email')}")
        return templates.TemplateResponse("file_upload.html", {"request": request,})


    return templates.TemplateResponse("file_upload.html",{"request": request,})


# @router.route("/login_redirect", methods=["GET", "POST"])
# async def login_redirect(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})