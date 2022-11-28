from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.career import Career
from models.university import University
from config.database import db_engine, meta
university = APIRouter()


@university.get("/universities")
def get_universities():
    return "HOLA"


@university.get("/universities/{university_id}")
def get_university(university_id: int):
    return {"name": "University of California, Berkeley"}
