from fastapi import APIRouter, status, Request, File, UploadFile,Depends
from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi.templating import Jinja2Templates
from models.models import Users
from database import get_db
import base64

router = APIRouter(tags=["Cascade Dropdoen"])

templates = Jinja2Templates(directory="templates")


@router.get("/cascade")
async def cascase(request:Request):
	
	return templates.TemplateResponse("cascade/cascade_dropdown.html", context={"request":request })