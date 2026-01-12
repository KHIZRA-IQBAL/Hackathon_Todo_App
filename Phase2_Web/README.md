# Phase 2 - Todo Hackathon Application

This repository contains the monorepo for the Phase 2 Todo Hackathon application.

## Overview

This project is a multi-user web-based todo application. It features a frontend built with Next.js and a backend built with FastAPI.

- **`frontend/`**: Contains the Next.js application.
- **`backend/`**: Contains the FastAPI application.
- **`specs/`**: Contains the project specifications and documentation.

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python (v3.9+)

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set up your environment variables by creating a `.env` file.
4.  Run the backend server:
    ```bash
    uvicorn backend.main:app --reload
    ```
    The backend will be running at `http://localhost:8000`.

### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the required Node.js packages:
    ```bash
    npm install
    ```
3.  Run the frontend development server:
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:3000`.

## Usage

- Open your browser and go to `http://localhost:3000`.
- You will be redirected to the sign-in page.
- You can sign up for a new account or log in with an existing one.
- Once logged in, you will be taken to your dashboard where you can manage your tasks.
