from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import DB_USER, DB_PASS, DB_NAME, DB_PORT, DB_HOST
from task.model import Model

engine = create_async_engine(
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_database():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)




