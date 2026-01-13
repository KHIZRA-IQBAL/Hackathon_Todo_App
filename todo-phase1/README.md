# Hackathon Todo App - Phase I

A simple, in-memory console-based todo list application built in Python.

## Features

- **Add Task**: Create new tasks with title and description
- **View All Tasks**: Display all tasks with completion status
- **Update Task**: Modify task title or description
- **Delete Task**: Remove tasks (with confirmation)
- **Mark Complete/Incomplete**: Toggle task completion status
- **Simple Console UI**: Easy-to-use menu-driven interface

## Requirements

- Python 3.8 or higher
- No external dependencies (uses Python standard library only)

## Installation

### Option 1: Using uv (Recommended)

```bash
# From the phase1-console-app directory
uv pip install -e .
```

### Option 2: Using pip

```bash
# From the phase1-console-app directory
pip install -e .
```

## Running the Application

### Option 1: Using uv run (Recommended)

```bash
# From the phase1-console-app directory
uv run python -m hackathon_todo.main
```

### Option 2: Direct module execution

```bash
# After installation
python -m hackathon_todo.main
```

### Option 3: Using the todo command

```bash
# After installation
todo
```

## Usage

Once the application starts, you'll see the main menu:

```
=== Todo Manager ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit
Enter choice:
```

Simply enter the number (1-6) for the action you want to perform.

### Example Workflow

1. **Add a task**: Choose option 1, enter a title and description
2. **View tasks**: Choose option 2 to see all your tasks
3. **Mark complete**: Choose option 5, enter the task ID
4. **Update task**: Choose option 3 to modify a task
5. **Delete task**: Choose option 4 to remove a task (requires confirmation)
6. **Exit**: Choose option 6 to quit

## Task Display Format

Tasks are displayed in a table with the following columns:
- **ID**: Unique task identifier
- **Status**: `[ ]` for incomplete, `[X]` for completed
- **Title**: Task title (truncated if too long)
- **Description**: Task description (truncated if too long)

## Data Persistence

**Important**: This is Phase I with in-memory storage only. All tasks are lost when you exit the application. Data persistence will be added in Phase II.

## Validation

- **Title**: Required, 1-200 characters
- **Description**: Optional, maximum 1000 characters
- **Task ID**: Must be a valid number
- **Menu choices**: Must be 1-6

## Error Handling

The application handles errors gracefully:
- Invalid menu choices are rejected with clear messages
- Non-existent task IDs show helpful error messages
- Empty titles are rejected (title is required)
- All operations can be cancelled
- Keyboard interrupt (Ctrl+C) exits cleanly

## Project Structure

```
phase1-console-app/
├── src/
│   └── hackathon_todo/
│       ├── __init__.py          # Package initialization
│       ├── main.py              # Entry point
│       ├── todo_manager.py      # Business logic (CRUD operations)
│       └── ui.py                # User interface layer
├── speckit.constitution         # Project principles
├── speckit.specify              # Requirements specification
├── speckit.plan                 # Architecture plan
├── speckit.tasks                # Task breakdown
├── CLAUDE.md                    # Development instructions
├── pyproject.toml               # Project configuration
└── README.md                    # This file
```

## Development

This project follows Spec-Driven Development (SDD). All specifications are documented in the `speckit.*` files.

### Architecture

The application uses a three-layer architecture:
- **UI Layer** (`ui.py`): Handles all user interaction
- **Business Logic** (`todo_manager.py`): Manages tasks and operations
- **Data Layer**: In-memory list storage

### Running Tests

The application has been tested with:
- Unit tests for TodoManager CRUD operations
- Integration tests for UI and manager interaction
- Manual acceptance testing for all user stories

## Limitations (Phase I)

- No data persistence (memory only)
- No task priorities or categories
- No due dates or reminders
- No search or filter functionality
- Console interface only (no web UI)

These features are planned for future phases.

## License

Hackathon project - Phase I implementation.
