from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from utils.config import Config

engine = create_async_engine(url=Config.DATABASE_URL, echo=True)

async def main():
    id = input("id: ")
    name = input("name: ")



