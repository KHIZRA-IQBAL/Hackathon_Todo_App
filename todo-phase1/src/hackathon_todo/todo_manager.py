"""
Business logic layer for todo task management.
Handles all CRUD operations and task storage.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# CORE-2: Task Data Model
@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id: Unique identifier for the task
        title: Short title of the task (1-200 characters)
        description: Detailed description of the task (max 1000 characters)
        completed: Whether the task is completed or not
        created_at: Timestamp when the task was created
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)


class TodoManager:
    """
    Manages todo tasks with in-memory storage.
    Provides CRUD operations for tasks.

    Storage: Uses a list for in-memory task storage.
    All operations maintain data integrity and validate inputs.
    """

    # CORE-3: Initialize TodoManager Storage
    def __init__(self):
        """Initialize the TodoManager with empty task storage."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    # CRUD-1: Implement Add Task
    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task to the todo list.

        Validates inputs and creates a new task with a unique ID.

        Args:
            title: The title of the task (required, 1-200 characters)
            description: The description of the task (optional, max 1000 characters)

        Returns:
            The ID of the newly created task

        Raises:
            ValueError: If title is empty, too long, or description exceeds max length
        """
        # Validate title
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        title = title.strip()
        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")

        # Validate description
        description = description.strip()
        if len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")

        # Generate unique ID and create task
        task_id = self._next_id
        task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=False,
            created_at=datetime.now()
        )

        # Store task and increment ID counter
        self._tasks.append(task)
        self._next_id += 1

        return task_id

    # CRUD-2: Implement Get Tasks
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the todo list.

        Returns:
            List of all Task objects (empty list if no tasks exist)
        """
        return self._tasks.copy()

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    # CRUD-3: Implement Update Task
    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> bool:
        """
        Update an existing task's title and/or description.

        If a parameter is None, the corresponding field will not be updated.

        Args:
            task_id: The ID of the task to update
            title: The new title (optional, 1-200 characters if provided)
            description: The new description (optional, max 1000 characters if provided)

        Returns:
            True if task was updated successfully, False if task not found

        Raises:
            ValueError: If title is empty/too long or description exceeds max length
        """
        # Find the task
        task = self.get_task(task_id)
        if task is None:
            return False

        # Validate and update title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")

            title = title.strip()
            if len(title) > 200:
                raise ValueError("Title cannot exceed 200 characters")

            task.title = title

        # Validate and update description if provided
        if description is not None:
            description = description.strip()
            if len(description) > 1000:
                raise ValueError("Description cannot exceed 1000 characters")

            task.description = description

        return True

    # CRUD-4: Implement Delete Task
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the todo list.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted successfully, False if task not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                self._tasks.pop(i)
                return True
        return False

    # CRUD-5: Implement Toggle Complete
    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Changes the task's completed status from True to False or vice versa.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if task status was toggled successfully, False if task not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        task.completed = not task.completed
        return True
