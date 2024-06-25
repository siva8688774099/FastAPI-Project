from fastapi import APIRouter, status, Request, Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from database import get_db
from models.models import Users


router = APIRouter(tags=["Table API"])

@router.get("/table")
async def table(request:Request, db:Session=Depends(get_db)):
	users = db.query(Users).with_entities(Users.username, Users.email, Users.mobile,Users.image).all()
	return [{"username":user.username, "email":user.email, "mobile":user.mobile,"image":user.image} for user in users]
