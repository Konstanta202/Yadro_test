# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import create_tables, drop_tables
from app.api.routers.users import router as user_router
from app.core.init_data import init_database
import logging
from app.models import User # noqa


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start app")
    await init_database()

    yield
    await drop_tables()
    logger.info("Shutting down application...")


app = FastAPI(
    title="Random People Database",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api")


@app.get("/")
async def root():
    return {"Message": "Backend work"}
