# UI Components

## 1. TaskList Component (`components/TaskList.tsx`)
- **Props:**
  - `tasks: Task[]`: An array of task objects to display.
- **State:**
  - Manages the list of tasks passed via props.
- **Behavior:**
  - Renders a `TaskItem` component for each task in the `tasks` array.
  - Displays a message like "No tasks yet!" if the `tasks` array is empty.

## 2. TaskItem Component (`components/TaskItem.tsx`)
- **Props:**
  - `task: Task`: The individual task object to display.
  - `onUpdate: (id, updates) => void`: Callback to handle task updates.
  - `onDelete: (id) => void`: Callback to handle task deletion.
- **State:**
  - `isEditing: boolean`: Toggles between view and edit mode for the task content.
- **Actions:**
  - **Checkbox:** Toggles the `is_completed` status of the task and calls `onUpdate`.
  - **Edit Button:** Sets `isEditing` to `true`, displaying an input field with the current task content.
  - **Save Button (in edit mode):** Calls `onUpdate` with the new content and sets `isEditing` to `false`.
  - **Delete Button:** Calls `onDelete` with the task's ID.

## 3. AddTaskForm Component (`components/AddTaskForm.tsx`)
- **Fields:**
  - A single text input for the task content.
  - A submit button.
- **State:**
  - `content: string`: Manages the value of the text input.
- **Validation:**
  - The input field cannot be empty.
  - The submit button is disabled if the input is empty.
- **Behavior:**
  - On submit, it calls a function (passed via props) to create the new task via an API call.
  - Clears the input field after successful submission.

## 4. Header Component (`components/Header.tsx`)
- **Props:**
  - `isLoggedIn: boolean`: Determines which set of UI elements to display.
- **Navigation:**
  - If `isLoggedIn` is `false`, it shows "Login" and "Signup" links.
  - If `isLoggedIn` is `true`, it shows the user's email and a "Logout" button.
- **Logout Behavior:**
  - The "Logout" button triggers a function to clear the authentication token from storage and redirect the user to the login page.

## 5. Component Interaction Diagram

```
+-----------------+
|   Dashboard     | (Page)
| +-------------+ |
| |   Header    | |
| +-------------+ |
|                 |
| +-------------+ |
| | AddTaskForm | | -----------+
| +-------------+ |            | (creates new task)
|                 |            |
| +-------------+ | <----------+ (updates task list)
| |  TaskList   | |
| | +---------+ | |
| | | TaskItem| | | --(edit/delete)--> (API Call)
| | +---------+ | |
| | +---------+ | |
| | | TaskItem| | |
| | +---------+ | |
| +-------------+ |
+-----------------+
```