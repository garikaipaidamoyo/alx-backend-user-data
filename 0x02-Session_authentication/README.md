# 0x02. Session Authentication

This project implements session-based authentication for a web application.

## Files

- `session_auth.py`: Contains the SessionAuth class for session-based authentication.

## Usage

To use the session authentication in your project, follow these steps:

1. Import the `SessionAuth` class from `session_auth.py`.
2. Create an instance of `SessionAuth`.
3. Set the authentication mechanism for your application using the created instance.

Example:

```python
from api.v1.auth.session_auth import SessionAuth

# Create an instance of SessionAuth
session_auth = SessionAuth()

# Set as the authentication mechanism for your application
app.auth = session_auth

Paidamoyo Garikai