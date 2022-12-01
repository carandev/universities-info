from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.university import university
from routes.career import career

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(university)
app.include_router(career)
