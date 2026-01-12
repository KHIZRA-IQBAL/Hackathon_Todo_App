# Feature: User Authentication

## 1. User Stories

- **Registration:** As a new user, I want to create an account using my email and a password so that I can use the application.
- **Login:** As an existing user, I want to log in with my email and password so that I can access my tasks.
- **Logout:** As a logged-in user, I want to log out so that my session is terminated and my account is secure.
- **Protected Routes:** As a logged-in user, I want to be the only one who can access my dashboard page. Unauthenticated users should be redirected to the login page.

## 2. Technical Architecture

### Registration Flow
1. User provides email and password.
2. Frontend sends a `POST` request to `/api/auth/signup`.
3. Backend validates that the email is not already in use.
4. Backend hashes the password using a strong algorithm (e.g., bcrypt).
5. Backend creates a new `User` record in the database.
6. Backend returns a `201 Created` response.

### Login Flow
1. User provides email and password.
2. Frontend sends a `POST` request to `/api/auth/login`.
3. Backend finds the user by email.
4. Backend verifies the provided password against the stored hash.
5. If credentials are valid, the backend generates a JWT containing the `user_id`.
6. Backend returns the JWT in the response.
7. Frontend stores the JWT for subsequent requests.

### API Request Flow with Authentication
1. Frontend makes a request to a protected endpoint (e.g., `GET /api/tasks/`).
2. The JWT is included in the `Authorization: Bearer <token>` header.
3. FastAPI dependency injection validates the token:
   - Is it expired?
   - Is the signature valid?
4. If valid, the user's ID is extracted from the token and attached to the request context.
5. The endpoint logic proceeds, using the user's ID to fetch the correct data.
6. If the token is invalid or missing, a `401 Unauthorized` error is returned.

## 3. JWT Token Structure
- **Header:** `{"alg": "HS256", "typ": "JWT"}`
- **Payload:**
  ```json
  {
    "sub": "user_id",
    "exp": <timestamp>,
    "iat": <timestamp>
  }
  ```
- **Signature:** Signed with a strong secret key stored securely on the backend.

## 4. Better Auth Configuration
*This section would be filled in with the specific configuration details for the `Better Auth` library if it were a real library. For this project, we assume a custom implementation following the principles above.*

## 5. Database Schema for Users
- `users` table:
  - `id`: Primary Key (e.g., UUID or auto-incrementing integer).
  - `email`: `VARCHAR(255)`, Unique, Not Null.
  - `hashed_password`: `VARCHAR(255)`, Not Null.
  - `created_at`: Timestamp.

## 6. API Security Patterns
- **HTTPS:** All communication must be over HTTPS in production.
- **Password Hashing:** Passwords are never stored in plain text.
- **Input Validation:** All user input is validated on the backend to prevent injection attacks.
- **CORS:** Configure Cross-Origin Resource Sharing on the backend to only allow requests from the known frontend domain.

## 7. Password Requirements
- Minimum 8 characters.
- Must contain a mix of uppercase letters, lowercase letters, numbers, and symbols (enforced on the frontend and backend).

## 8. Security Requirements
- **Secret Management:** The JWT secret key and database credentials must be stored securely as environment variables, not in code.
- **Dependency Security:** Regularly scan for vulnerabilities in third-party libraries.
- **Rate Limiting:** Implement rate limiting on authentication endpoints to prevent brute-force attacks.

## 9. Testing Scenarios
- Test that a new user can register successfully.
- Test that registration fails if the email is already in use.
- Test that a registered user can log in with correct credentials.
- Test that login fails with incorrect credentials.
- Test that an unauthenticated user receives a `401` error when accessing a protected route.
- Test that a logged-in user can access protected routes successfully.
- Test that an expired token is rejected.
