from typing import Annotated
from fastapi import APIRouter, Depends
from .repository import TaskRepository
from .schema import STask, STaskAdd, STaskID

router = APIRouter(prefix='/task', tags=['/task'])


@router.post('')
async def add_task(add_task: Annotated[STaskAdd, Depends()]) -> STaskID:
    result = await TaskRepository.add_one(add_task)
    return {'status': 200, 'task_id': result}


@router.get('')
async def read_task() -> list[STask]:
    result = await TaskRepository.read_all()
    return result

