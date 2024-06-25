from fastapi import APIRouter, status, Request, File, UploadFile,Depends
from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi.templating import Jinja2Templates
from models.models import Users
from database import get_db
import base64

router = APIRouter(tags=["Image Upload"])

templates = Jinja2Templates(directory="templates")


@router.get("/upload", status_code=status.HTTP_200_OK)
async def template(request: Request):
	"""
	The template function is used to render the index.html template.

	:param request:Request: Get the request body
	:return: The index.html template
	:doc-author: Trelent
	"""
	return templates.TemplateResponse("file_upload.html", context={"request": request})

@router.post("/uploadfile", status_code=status.HTTP_200_OK)
async def upload_image(request: Request, file: UploadFile = File(...),db_conn:Session=Depends(get_db)):
	"""
	The upload_image function is used to upload an image file.

	:param request:Request: Get the request body
	:param file: UploadFile: Get the file from the request body
	:return: A dictionary with the file name and content type keys
	:doc-author: Trelent
	"""
	# db_conn.query(Users).filter(Users.email == request.session["email"]).update({"image": file.file.read()})
	filecontent = await file.read()
	query = update(Users).where(Users.email == request.session["email"]).values(image=base64.b64encode(filecontent).decode("utf-8"))

	db_conn.execute(query)
	db_conn.commit()

	user_details = db_conn.query(Users).filter(Users.email == request.session["email"]).first()

	context = user_details.__dict__
	return templates.TemplateResponse("dashboard.html", {"request": request, "request": context})