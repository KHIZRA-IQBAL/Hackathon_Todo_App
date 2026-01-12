# Feature: Task CRUD Operations

## 1. User Stories

- **Create:** As a logged-in user, I want to create a new task so that I can track what I need to do.
- **View:** As a logged-in user, I want to see a list of all my tasks so that I know what I have to do.
- **Update:** As a logged-in user, I want to edit the content of an existing task so that I can correct mistakes or update its details.
- **Delete:** As a logged-in user, I want to delete a task that is no longer needed so that my task list stays clean.
- **Mark Complete:** As a logged-in user, I want to mark a task as complete so that I can track my progress.

## 2. Acceptance Criteria

- **Create:**
  - A logged-in user can see a form to add a new task.
  - The task must have content.
  - When submitted, the new task appears in the user's task list.
  - An unauthenticated user cannot create a task.

- **View:**
  - A logged-in user sees only their own tasks.
  - Tasks are displayed clearly, showing content and completion status.
  - An unauthenticated user cannot see any tasks.

- **Update:**
  - A logged-in user can click an "edit" button on a task they own.
  - The task content becomes editable.
  - When saved, the task list updates with the new content.
  - A user cannot edit another user's task.

- **Delete:**
  - A logged-in user can click a "delete" button on a task they own.
  - A confirmation is requested before deletion.
  - Once confirmed, the task is removed from the task list.
  - A user cannot delete another user's task.

- **Mark Complete:**
  - A logged-in user can click a checkbox or button to toggle a task's completion status.
  - The UI reflects the new status (e.g., strikethrough text).
  - The change is persisted to the backend.

## 3. Technical Requirements

- **Data Model:**
  - `Task` model with fields: `id`, `content`, `is_completed`, `created_at`, `owner_id` (foreign key to `User`).
- **API Endpoints:**
  - `POST /api/tasks/`: Create a new task.
  - `GET /api/tasks/`: Get all tasks for the logged-in user.
  - `PUT /api/tasks/{task_id}`: Update a task's content or status.
  - `DELETE /api/tasks/{task_id}`: Delete a task.
- **Frontend Components:**
  - `TaskList`: Renders the list of tasks.
  - `TaskItem`: Represents a single task with controls for edit, delete, and completion.
  - `AddTaskForm`: Form for creating a new task.

## 4. Validation Rules
- `content`: Required, string, max length 255 characters.
- `is_completed`: Boolean.

## 5. Error Handling
- `400 Bad Request`: Invalid input data (e.g., empty content).
- `401 Unauthorized`: User is not authenticated.
- `403 Forbidden`: User tries to access or modify a task they do not own.
- `404 Not Found`: The specified task does not exist.
- `500 Internal Server Error`: Unexpected backend error.

## 6. UI/UX Requirements
- The task list should be clean and easy to read.
- Controls for actions (edit, delete) should be intuitive.
- Provide clear feedback to the user on success or failure of an action (e.g., toast notifications).
- Completed tasks should be visually distinct from incomplete ones.

## 7. Testing Scenarios
- **Unit Tests:**
  - Test validation rules for the Task model.
  - Test API service functions for correct request formatting.
- **Integration Tests:**
  - Test API endpoints for correct behavior (CRUD operations).
  - Test that a user can only interact with their own tasks.
- **End-to-End (E2E) Tests:**
  - Simulate a user logging in, creating a task, editing it, marking it complete, and deleting it.
  - Test that a user cannot see or modify another user's tasks by manipulating requests.