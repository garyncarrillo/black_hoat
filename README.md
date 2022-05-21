# user CRUD In Fastapi

This project was designed to complete technical testing requirements.

## Installation

[uvicorn](https://www.uvicorn.org/) is required to start the project

```bash
$ pip install uvicorn
```

## Start de project
The main.py file contains the commands required to start the project
```bash
python3 main.py
```
But you can also start the project using the uvicorn command to the user.py file directly
```bash
uvicorn.run("users:app", host = "127.0.0.1", port = 8000, reload = True)
```
## Enter to the FASTAPI Docs
[Docs](http://127.0.0.1:8000/docs)

## Testing
you have to install pytest first to be able to use the test file
```bash
$ pip install pytest
```
after install pytest, you can test the file using the following command on test_user.py
```bash
$ pytest test_user.py
```
