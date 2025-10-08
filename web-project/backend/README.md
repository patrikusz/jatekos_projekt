# Backend README

# Web Project Backend

This is the backend part of the web project, which provides user authentication functionalities. It is built using Node.js and Express.

## Features

- User registration
- User login
- JWT authentication

## Getting Started

### Prerequisites

- Node.js
- npm

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the backend directory:
   ```
   cd web-project/backend
   ```
3. Install the dependencies:
   ```
   npm install
   ```

### Running the Application

To start the backend server, run:
```
npm start
```

The server will run on `http://localhost:3000`.

### API Endpoints

- **POST /api/auth/register**: Register a new user
- **POST /api/auth/login**: Login an existing user

## Folder Structure

- `src/app.js`: Entry point of the application.
- `src/controllers/authController.js`: Contains authentication logic.
- `src/routes/authRoutes.js`: Defines the authentication routes.
- `src/models/user.js`: User model for database interactions.

## License

This project is licensed under the MIT License.