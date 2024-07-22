from database import create_table, delete_database
from task.router import router as router_task
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(application: FastAPI):
    await create_table()
    print('База создана')
    yield
    await delete_database()
    print('База удалена')


app = FastAPI(lifespan=lifespan)

app.include_router(router_task)

