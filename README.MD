# Instagram API

This project is a simple **FastAPI**-based API that provides access to Instagram profile and reel information using the **instaloader** library.

## Features
- Retrieve Instagram profile details (username, full name, followers, followees, post count, biography, account status).
- Fetch Instagram reel information (link, username, publish date, likes, views, caption, hashtags, tagged users).
- Comprehensive error handling with appropriate HTTP responses.

## Prerequisites
To run this project, you need the following:
- **Python 3.8+**
- Python packages (listed in `requirements.txt`):
  - `fastapi`
  - `pydantic`
  - `instaloader`
  - `uvicorn` (for running the FastAPI server)
- Internet connection for Instagram API communication

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required packages using the provided `requirements.txt` file:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   Start the FastAPI server with the following command:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`. The `--reload` flag enables auto-reload for development.

## API Endpoints

### 1. Get Profile Information
- **Endpoint**: `POST /profile`
- **Description**: Retrieves details of an Instagram profile.
- **Request Body**:
  ```json
  {
    "username": "example_username"
  }
  ```
- **Response** (Success):
  ```json
  {
    "username": "example_username",
    "full_name": "Example Name",
    "followers": 1000,
    "followees": 500,
    "post_count": 50,
    "biography": "This is a bio",
    "profile_url": "https://www.instagram.com/example_username/",
    "status": "Public"
  }
  ```
- **Error Responses**:
  - `404`: Profile does not exist.
  - `403`: Profile is private, login required.
  - `500`: Server error with details.

### 2. Get Reel Information
- **Endpoint**: `POST /reel`
- **Description**: Retrieves details of an Instagram reel.
- **Request Body**:
  ```json
  {
    "link": "https://www.instagram.com/reel/ABC123/"
  }
  ```
- **Response** (Success):
  ```json
  {
    "link": "https://www.instagram.com/p/ABC123/",
    "username": "example_username",
    "date": "2023-10-27 14:30:00",
    "likes": 500,
    "views": 10000,
    "caption": "This is a reel caption",
    "hashtags": ["example", "reel"],
    "tagged_users": ["user1", "user2"]
  }
  ```
- **Error Responses**:
  - `404`: Reel does not exist.
  - `403`: Reel is private, login required.
  - `400`: Provided link is not a reel or video.
  - `500`: Server error with details.

## Usage
1. **Access the API**:
   After starting the server, you can access the API at `http://localhost:8000`. Use a tool like **Postman**, **cURL**, or any HTTP client to send requests.

2. **Interactive API Documentation**:
   FastAPI provides automatic Swagger UI documentation. Visit `http://localhost:8000/docs` to test the endpoints interactively.

3. **Example cURL Commands**:
   - Get profile info:
     ```bash
     curl -X POST "http://localhost:8000/profile" -H "Content-Type: application/json" -d '{"username": "example_username"}'
     ```
   - Get reel info:
     ```bash
     curl -X POST "http://localhost:8000/reel" -H "Content-Type: application/json" -d '{"link": "https://www.instagram.com/reel/ABC123/"}'
     ```

## Notes
- **Rate Limits**: Instagram may impose rate limits on requests. The `instaloader` configuration in the code includes `sleep=True` and `max_connection_attempts=3` to handle this gracefully.
- **Private Accounts**: Accessing private profiles or reels requires Instagram login credentials, which are not implemented in this code. Attempting to access private content will return a `403` error.
- **Error Handling**: The API includes robust error handling for common issues like non-existent profiles, private content, or invalid reel links.

## Troubleshooting
- **Module Not Found**: Ensure all dependencies are installed correctly using `pip install -r requirements.txt`.
- **Connection Issues**: Check your internet connection and ensure Instagram is accessible.
- **Rate Limit Errors**: If Instagram blocks requests, try reducing the frequency of requests or configure `instaloader` with login credentials for authenticated access.
