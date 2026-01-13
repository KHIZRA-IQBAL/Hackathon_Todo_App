"""
Main entry point for the Hackathon Todo App.
"""

from .todo_manager import TodoManager
from .ui import TodoUI


def main():
    """Main application entry point."""
    # INT-1: Initialize components and run application
    manager = TodoManager()
    ui = TodoUI(manager)
    ui.run()


if __name__ == "__main__":
    main()
