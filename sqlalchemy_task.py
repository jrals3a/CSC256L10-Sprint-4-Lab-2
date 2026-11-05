# app/models/sqlalchemy_task.py
from typing import Any

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class SQLAlchemyTask(Base):
    """SQLAlchemy ORM model for the tasks table.

    Maps to the 'tasks' table in SQLite.
    Each instance represents one row.

    This is separate from app/models/task.py (the domain model).
    FileTaskRepository uses Task (domain model).
    DatabaseTaskRepository uses SQLAlchemyTask (ORM model) internally
    but converts to/from dict for the ITaskRepository interface.
    """

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True, default="")
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def to_dict(self) -> dict[str, Any]:
        """Convert ORM model to dict for ITaskRepository interface."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description or "",
            "completed": self.completed,
        }
