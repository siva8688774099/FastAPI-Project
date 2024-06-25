from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Users(Base):
    __tablename__:str = "users_login"

    __table_args__ = {"schema":"fastapi"}

    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    username:Mapped[str] = mapped_column(String(50))
    email:Mapped[str] = mapped_column(String(50))
    mobile = mapped_column(String(20))
    hashed_password:Mapped[str] = mapped_column(String)
    image : Mapped[str] = mapped_column(String)
