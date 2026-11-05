# app/models/task.py
from typing import Any


class Task:
    """Domain model representing a single task.

    Attributes:
        id: Unique task identifier (auto-assigned by TaskService)
        title: Task title — required, cannot be empty
        description: Optional task description
        completed: Whether the task is done — defaults to False
    """

    def __init__(
        self,
        id: int,
        title: str,
        description: str = "",
        completed: bool = False,
    ) -> None:
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.completed: bool = completed

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self) -> dict[str, Any]:
        """Serialize Task to a JSON-serializable dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
