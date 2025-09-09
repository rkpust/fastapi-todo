# FastAPI ToDo App

<div align="center">
  <img height="400" width="80%" src="https://github.com/rkpust/fastapi-todo/blob/master/API.jpg"/>
</div>

This project is a **ToDo Application** built with **FastAPI** to demonstrate the simplicity and power of FastAPI for creating RESTful APIs. It includes basic functionality for creating, reading, updating, and deleting tasks in a ToDo list.

## Features

* Create, Read, Update, and Delete (CRUD) tasks.
* User-friendly interactive API documentation with **Swagger UI**.
* Built with **FastAPI** for fast and efficient backend development.


## Prerequisites

Before you start, make sure you have the following installed:

* **Python 3.7+**
* **pip** (Python package manager)


## Installation

### Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies separately from your global Python environment.

```bash
python -m venv venv
```

### Activate Virtual Environment

* **For Windows**:

```bash
venv\Scripts\activate
```

* **For Mac/Linux**:

```bash
source venv/bin/activate
```

### Clone the Repository

Clone this project to your local machine using the following command:

```bash
git clone https://github.com/rkpust/fastapi-todo.git
```

### Install Required Dependencies

Install all the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Server

To run the FastAPI development server:

```bash
uvicorn main:api --reload
```

Alternatively, you can also use the following command to start the server:

```bash
fastapi dev main.py
```

#### Run with a specific port:

You can specify a custom port (e.g., port 9999):

```bash
fastapi dev main.py --port 9999
```

## API Documentation
Once the server is running, you can interact with the API, test the endpoints via **Swagger UI** and see the detailed API documentation via **ReDoc**.

* **Swagger UI**: Using `/docs` endpoints
* **ReDoc**: Using `/redoc` endpoints