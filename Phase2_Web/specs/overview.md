# Project: Todo Application Phase 2

## 1. Purpose
A multi-user web application that allows users to manage their tasks in a secure and isolated environment.

## 2. Tech Stack
- **Frontend:** Next.js 16+
- **Backend:** FastAPI, SQLModel
- **Database:** Neon PostgreSQL
- **Authentication:** Better Auth
- **Styling:** Tailwind CSS

## 3. Core Features
- **User Authentication:** Secure user registration, login, and session management.
- **Task CRUD Operations:** Users can create, read, update, and delete their own tasks.
- **User Isolation:** Each user can only access their own tasks. Data is not shared between users.

## 4. Architecture
The application follows a monorepo structure with a clear separation between the frontend and backend services.
- **`frontend/`**: A Next.js application responsible for the user interface and user experience.
- **`backend/`**: A FastAPI application that serves a RESTful API for all application logic.
- **`specs/`**: Project documentation and specifications.