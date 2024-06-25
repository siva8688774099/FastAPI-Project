from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os

ENVIRONMENT = os.getenv("ENVIRONMENT","local")

class ProjectConfig(BaseSettings):
	model_config:SettingsConfigDict = SettingsConfigDict(env_file=f".env_{ENVIRONMENT}",extra="ignore")

class DBConfig(ProjectConfig):
	db_host: str = Field(..., alias="host")
	db_port: int = Field(..., alias="port")
	db_name: str = Field(..., alias="database")
	db_user: str = Field(..., alias="user")
	db_password: str = Field(..., alias="password")

db_creds = DBConfig() #type: ignore
