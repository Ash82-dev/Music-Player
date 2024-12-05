import hashlib
import json
import os

# Get the directory where the database.py script is located
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
USER_FILE = os.path.join(BASE_DIR, "user_db.txt")


def hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def get_user_list() -> dict:
    """Reads and returns the user database from the file."""
    if not os.path.exists(USER_FILE):
        return {}  # Return an empty dict if the file doesn't exist yet

    with open(USER_FILE, "r") as file:
        return json.load(file)


def add_user(username: str, password: str) -> str:
    """Adds a new user to the database."""
    user_db = get_user_list()
    if username in user_db:
        return "Username already exists."

    # Hash the password before storing
    user_db[username] = hash_password(password)

    # Save the updated user_db back to the file
    with open(USER_FILE, "w") as file:
        json.dump(user_db, file)
    return "User added successfully."
