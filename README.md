# App-Api

# Task Management API

This project is a simple Task Management API built with FastAPI. The API allows you to create, retrieve, update, and delete tasks. Each task has an `id`, `description`, and `status`.

## Features

- **Create Task**: Add a new task to the list.
- **Get All Tasks**: Retrieve the list of all tasks.
- **Update Task**: Update the status of a specific task.
- **Delete Task**: Remove a task by its ID.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install fastapi uvicorn
    ```

4. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### Get All Tasks
- **GET** `/tasks`
- Returns the list of all tasks.

### Create a New Task
- **POST** `/tasks`
- Creates a new task with the provided `id`, `description`, and `status`.

### Update a Task
- **PUT** `/tasks/{task_id}`
- Updates the status of a task with the given `task_id`.

### Delete a Task
- **DELETE** `/tasks/{task_id}`
- Deletes the task with the given `task_id`.

## Example Usage

To create a task, send a POST request to `/tasks` with the following JSON:

```json
{
    "id": 5,
    "description": "Read a book",
    "status": false
}
