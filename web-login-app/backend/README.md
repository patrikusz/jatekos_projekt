# Backend Documentation

## Overview
This is the backend component of the web-login-app project, which is built using Python and Flask. It handles user authentication and serves as the API for the frontend.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd web-login-app/backend
   ```

2. **Create a Virtual Environment**
   It is recommended to create a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the Flask application.
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your web browser and go to `http://127.0.0.1:5000` to access the login interface.

## Usage
- The backend provides endpoints for user login and authentication.
- Ensure that the frontend is properly configured to communicate with this backend.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.