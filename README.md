# Django Todo Application with REST API

## Overview

This Django Todo application enables users to manage their tasks through a user-friendly web interface and interact with the task data via a RESTful API built with Django Rest Framework.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python (>=3.x)
- Django
- Django Rest Framework

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/todo-django.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd todo-django
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

Visit `http://localhost:8000` in your web browser to access the Todo application. Use the web interface to manage your tasks interactively.

## API Endpoints

### Task List

- **GET /api/get_task/**: Retrieve a list of all tasks.
- **POST /api/add_task/**: Create a new task.

### Task Detail

- **PUT /api/update/{task_name}/**: Update details of a specific task.
- **DELETE /api/delete_task/{task_name}/**: Delete a specific task.

## Features

- Add tasks through the web interface.
- Manage tasks via REST API.
- View a list of all tasks and details of individual tasks.
- Update and delete tasks interactively or through the API.

## Contributing

We welcome contributions! If you find a bug or have a feature request, please open an issue. Pull requests are also appreciated.

For major changes, please open an issue first to discuss what you would like to change.

