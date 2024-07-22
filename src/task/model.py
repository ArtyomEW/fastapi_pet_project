from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional


class Model(DeclarativeBase):
    pass


class TaskORM(Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


