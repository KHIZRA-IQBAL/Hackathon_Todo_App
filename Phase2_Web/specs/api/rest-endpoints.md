# REST API Endpoints

## 1. Base URL
- **Development:** `http://localhost:8000`
- **Production:** `https://api.yourdomain.com`

## 2. Authentication
All protected endpoints require an `Authorization` header with a Bearer token.
- **Format:** `Authorization: Bearer <your_jwt_token>`

---

## 3. API Endpoints

### Authentication

#### 1. User Signup
- **Method:** `POST`
- **Path:** `/api/auth/signup`
- **Description:** Registers a new user.
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "strongpassword123!"
  }
  ```
- **Success Response (201 Created):**
  ```json
  {
    "message": "User created successfully"
  }
  ```
- **Error Responses:**
  - `400 Bad Request`: Invalid email format or password does not meet requirements.
  - `409 Conflict`: An account with this email already exists.

#### 2. User Login
- **Method:** `POST`
- **Path:** `/api/auth/login`
- **Description:** Authenticates a user and returns a JWT.
- **Request Body:**
  ```json
  {
    "username": "user@example.com", // Note: FastAPI's OAuth2PasswordRequestForm uses 'username'
    "password": "strongpassword123!"
  }
  ```
- **Success Response (200 OK):**
  ```json
  {
    "access_token": "your_jwt_token",
    "token_type": "bearer"
  }
  ```
- **Error Responses:**
  - `401 Unauthorized`: Invalid credentials.

### Tasks

#### 3. Create Task
- **Method:** `POST`
- **Path:** `/api/tasks/`
- **Description:** Creates a new task for the authenticated user.
- **Request Body:**
  ```json
  {
    "content": "My new task"
  }
  ```
- **Success Response (201 Created):**
  ```json
  {
    "id": 1,
    "content": "My new task",
    "is_completed": false,
    "created_at": "2023-10-27T10:00:00Z",
    "owner_id": "user-uuid"
  }
  ```
- **Error Responses:**
  - `400 Bad Request`: Content is missing or invalid.
  - `401 Unauthorized`: User is not authenticated.

#### 4. Get Tasks
- **Method:** `GET`
- **Path:** `/api/tasks/`
- **Description:** Retrieves all tasks for the authenticated user.
- **Success Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "content": "My first task",
      "is_completed": true,
      "created_at": "2023-10-27T10:00:00Z",
      "owner_id": "user-uuid"
    },
    {
      "id": 2,
      "content": "My second task",
      "is_completed": false,
      "created_at": "2023-10-27T11:00:00Z",
      "owner_id": "user-uuid"
    }
  ]
  ```
- **Error Responses:**
  - `401 Unauthorized`: User is not authenticated.

#### 5. Update Task
- **Method:** `PUT`
- **Path:** `/api/tasks/{task_id}`
- **Description:** Updates a specific task's content or completion status.
- **Path Parameters:**
  - `task_id` (integer): The ID of the task to update.
- **Request Body:**
  ```json
  {
    "content": "Updated task content",
    "is_completed": true
  }
  ```
- **Success Response (200 OK):**
  ```json
  {
    "id": 1,
    "content": "Updated task content",
    "is_completed": true,
    "created_at": "2023-10-27T10:00:00Z",
    "owner_id": "user-uuid"
  }
  ```
- **Error Responses:**
  - `401 Unauthorized`: User is not authenticated.
  - `403 Forbidden`: User does not own this task.
  - `404 Not Found`: Task with the given ID does not exist.

#### 6. Delete Task
- **Method:** `DELETE`
- **Path:** `/api/tasks/{task_id}`
- **Description:** Deletes a specific task.
- **Path Parameters:**
  - `task_id` (integer): The ID of the task to delete.
- **Success Response (200 OK):**
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```
- **Error Responses:**
  - `401 Unauthorized`: User is not authenticated.
  - `403 Forbidden`: User does not own this task.
  - `404 Not Found`: Task with the given ID does not exist.

---

## 4. CORS Configuration
CORS will be configured in the FastAPI backend to allow requests only from the production frontend domain and `http://localhost:3000` during development.

## 5. Rate Limiting
Rate limiting should be applied to authentication endpoints (`/api/auth/signup`, `/api/auth/login`) to prevent brute-force attacks. For example, 10 requests per minute per IP address.