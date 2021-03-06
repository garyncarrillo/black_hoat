#!/usr/bin/env python3

import uvicorn
from users import app

if __name__ == '__main__':
    uvicorn.run("users:app", host = "127.0.0.1", port = 8000, reload = True)