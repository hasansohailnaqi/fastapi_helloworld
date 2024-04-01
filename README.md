# helloworld with fast api
poetry new fastapi_helloworld
 `cd 'fastapi_helloworld'`
 select your project with vs code
 open file file name 'pyproject.toml'
 
 ```
[tool.poetry]
name = "fastapi-helloworld"
version = "0.1.0"
description = ""
authors = ["Hasan Sohail  <hasansohail793@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

 create main.py location fastapi_helloworld\main.py
 install new package in poetry project
  `poetry add fastapi "uvicorn[standard]"`

```
[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.110.0"
uvicorn = {extras = ["standard"], version = "^0.29.0"}

```

poetry run uvicorn fastapi_helloworld.main:app --reload
`http://127.0.0.1:8000`
`http://127.0.0.1:8000/piaic`
`http://127.0.0.1:8000/doc`

write your own test
 `tests\test_main.py`
 ```
 from http import client
from fastapi.testclient import TestClient
from fastapi_helloworld.main import app

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello" : "world" }
def test_piaic():
    client = TestClient(app=app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"company" : "pakistan" } 

```
poetry run pytest -v

ctrl + shift + v to view doc