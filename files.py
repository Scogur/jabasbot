import os
#import asyncio
#import aiogram
# from aiogram import Bot
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session

from db_map import Base, MediaIds
from config import TOKEN, DB_FILENAME

engine = create_engine(f'sqlite:///{DB_FILENAME}')

def whatId(filename):
    with Session(engine) as session:
        fc = session.execute(select(MediaIds.file_id).where(MediaIds.file_name.like(f'{filename}%')))
        return fc.fetchone()[0]

#print((whatId('video2.mp4')))
