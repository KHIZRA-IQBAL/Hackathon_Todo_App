"""
User interface layer for the Hackathon Todo App.
Handles all user interaction and display formatting.
"""

from typing import List, Optional
from .todo_manager import TodoManager, Task


class TodoUI:
    """
    Console-based user interface for the todo application.
    Handles menu display, user input, and task formatting.
    """

    # UI-1: TodoUI Class Foundation
    def __init__(self, manager: TodoManager):
        """
        Initialize the UI with a TodoManager instance.

        Args:
            manager: The TodoManager instance to use for operations
        """
        self.manager = manager

    # UI-1: Main Application Loop
    def run(self) -> None:
        """
        Main application loop.
        Displays menu and handles user choices until exit.
        """
        print("\n" + "="*50)
        print("Welcome to Hackathon Todo Manager!")
        print("="*50)

        while True:
            try:
                self.display_menu()
                choice = self.get_menu_choice()

                if choice == 1:
                    self.handle_add_task()
                elif choice == 2:
                    self.handle_view_tasks()
                elif choice == 3:
                    self.handle_update_task()
                elif choice == 4:
                    self.handle_delete_task()
                elif choice == 5:
                    self.handle_toggle_complete()
                elif choice == 6:
                    print("\nGoodbye! Thanks for using Todo Manager.")
                    break

                input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                print("\n\nGoodbye! Thanks for using Todo Manager.")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
                input("\nPress Enter to continue...")

    # UI-2: Menu Display
    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\n" + "="*50)
        print("=== Todo Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete/Incomplete")
        print("6. Exit")

    # UI-2: Get Menu Choice
    def get_menu_choice(self) -> int:
        """
        Get and validate menu choice from user.

        Returns:
            Valid menu choice (1-6)
        """
        while True:
            try:
                choice_str = input("Enter choice: ").strip()
                choice = int(choice_str)

                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Error: Please enter a number between 1 and 6.")

            except ValueError:
                print("Error: Please enter a valid number.")
            except EOFError:
                print("\nError: No input received. Please enter a choice.")

    # UI-3: Display Tasks
    def display_tasks(self, tasks: List[Task]) -> None:
        """
        Display a list of tasks in a formatted table.

        Args:
            tasks: List of tasks to display
        """
        if not tasks:
            print("\nNo tasks yet. Add your first task to get started!")
            return

        print(f"\n{'='*80}")
        print(f"{'ID':<5} {'Status':<10} {'Title':<30} {'Description':<35}")
        print(f"{'='*80}")

        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            title = task.title[:27] + "..." if len(task.title) > 30 else task.title
            desc = task.description[:32] + "..." if len(task.description) > 35 else task.description

            print(f"{task.id:<5} {status:<10} {title:<30} {desc:<35}")

        print(f"{'='*80}")
        print(f"Total tasks: {len(tasks)}")

    # UI-4: Get Input Helper
    def get_input(self, prompt: str, allow_empty: bool = False) -> str:
        """
        Get input from user with validation.

        Args:
            prompt: The prompt to display
            allow_empty: Whether to allow empty input

        Returns:
            The validated user input (stripped of whitespace)
        """
        while True:
            try:
                user_input = input(prompt).strip()

                if not allow_empty and not user_input:
                    print("Error: This field cannot be empty. Please try again.")
                    continue

                return user_input

            except EOFError:
                print("\nError: No input received. Please try again.")
                if allow_empty:
                    return ""

    # UI-4: Get Task ID Helper
    def get_task_id(self) -> Optional[int]:
        """
        Get a task ID from the user.

        Returns:
            The task ID as integer, or None if input is invalid
        """
        try:
            task_id_str = input("Enter task ID: ").strip()
            task_id = int(task_id_str)
            return task_id
        except ValueError:
            print("Error: Please enter a valid number for task ID.")
            return None
        except EOFError:
            print("\nError: No input received.")
            return None

    # UI-4: Confirm Action Helper
    def confirm_action(self, prompt: str) -> bool:
        """
        Ask user to confirm an action.

        Args:
            prompt: The confirmation prompt

        Returns:
            True if user confirms, False otherwise
        """
        while True:
            try:
                response = input(f"{prompt} (y/n): ").strip().lower()

                if response in ['y', 'yes']:
                    return True
                elif response in ['n', 'no']:
                    return False
                else:
                    print("Error: Please enter 'y' for yes or 'n' for no.")

            except EOFError:
                print("\nError: No input received.")
                return False

    # UI-5: Handle Add Task
    def handle_add_task(self) -> None:
        """Handle the 'Add Task' menu option."""
        print("\n" + "-"*50)
        print("ADD NEW TASK")
        print("-"*50)

        try:
            # Get title (required)
            title = self.get_input("Enter task title: ", allow_empty=False)

            # Get description (optional)
            print("Enter task description (press Enter to skip):")
            description = input("> ").strip()

            # Add task
            task_id = self.manager.add_task(title, description)
            print(f"\nSuccess! Task added with ID: {task_id}")

        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nError: Failed to add task. {e}")

    # UI-5: Handle View Tasks
    def handle_view_tasks(self) -> None:
        """Handle the 'View All Tasks' menu option."""
        print("\n" + "-"*50)
        print("ALL TASKS")
        print("-"*50)

        try:
            tasks = self.manager.get_all_tasks()
            self.display_tasks(tasks)
        except Exception as e:
            print(f"\nError: Failed to retrieve tasks. {e}")

    # UI-5: Handle Update Task
    def handle_update_task(self) -> None:
        """Handle the 'Update Task' menu option."""
        print("\n" + "-"*50)
        print("UPDATE TASK")
        print("-"*50)

        try:
            # Get task ID
            task_id = self.get_task_id()
            if task_id is None:
                return

            # Check if task exists
            task = self.manager.get_task(task_id)
            if task is None:
                print(f"\nError: Task with ID {task_id} not found.")
                return

            # Show current task
            print(f"\nCurrent task details:")
            print(f"  Title: {task.title}")
            print(f"  Description: {task.description}")

            # Get new values
            print("\nEnter new values (press Enter to keep current value):")

            new_title_input = input(f"New title [{task.title}]: ").strip()
            new_title = new_title_input if new_title_input else None

            new_desc_input = input(f"New description [{task.description}]: ").strip()
            new_desc = new_desc_input if new_desc_input else None

            # Check if anything to update
            if new_title is None and new_desc is None:
                print("\nNo changes made.")
                return

            # Update task
            success = self.manager.update_task(task_id, new_title, new_desc)

            if success:
                print(f"\nSuccess! Task {task_id} updated.")
            else:
                print(f"\nError: Failed to update task {task_id}.")

        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nError: Failed to update task. {e}")

    # UI-5: Handle Delete Task
    def handle_delete_task(self) -> None:
        """Handle the 'Delete Task' menu option."""
        print("\n" + "-"*50)
        print("DELETE TASK")
        print("-"*50)

        try:
            # Get task ID
            task_id = self.get_task_id()
            if task_id is None:
                return

            # Check if task exists
            task = self.manager.get_task(task_id)
            if task is None:
                print(f"\nError: Task with ID {task_id} not found.")
                return

            # Show task details
            print(f"\nTask to delete:")
            print(f"  ID: {task.id}")
            print(f"  Title: {task.title}")
            print(f"  Description: {task.description}")
            print(f"  Completed: {'Yes' if task.completed else 'No'}")

            # Confirm deletion
            if self.confirm_action("\nAre you sure you want to delete this task?"):
                success = self.manager.delete_task(task_id)

                if success:
                    print(f"\nSuccess! Task {task_id} deleted.")
                else:
                    print(f"\nError: Failed to delete task {task_id}.")
            else:
                print("\nDeletion cancelled.")

        except Exception as e:
            print(f"\nError: Failed to delete task. {e}")

    # UI-5: Handle Toggle Complete
    def handle_toggle_complete(self) -> None:
        """Handle the 'Mark Complete/Incomplete' menu option."""
        print("\n" + "-"*50)
        print("TOGGLE TASK COMPLETION")
        print("-"*50)

        try:
            # Get task ID
            task_id = self.get_task_id()
            if task_id is None:
                return

            # Check if task exists and show current status
            task = self.manager.get_task(task_id)
            if task is None:
                print(f"\nError: Task with ID {task_id} not found.")
                return

            current_status = "completed" if task.completed else "incomplete"
            print(f"\nTask: {task.title}")
            print(f"Current status: {current_status}")

            # Toggle completion
            success = self.manager.toggle_complete(task_id)

            if success:
                # Get updated task to show new status
                task = self.manager.get_task(task_id)
                new_status = "completed" if task.completed else "incomplete"
                print(f"\nSuccess! Task {task_id} marked as {new_status}.")
            else:
                print(f"\nError: Failed to toggle task {task_id}.")

        except Exception as e:
            print(f"\nError: Failed to toggle task completion. {e}")
