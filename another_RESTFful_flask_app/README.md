# RESTful Flask App / Server on port 5000

## Setup Python/Pip:
- Upgrade pip: ```python3 -m pip install --upgrade pip```
- Install VirtualEnv: ```python3 -m pip install --upgrade virtualenv```

## Setup virtual env
- ```python3 -m virtualenv .venv```
- Activate VEnv: ```./.venv/Scripts/activate```
- Install dependencies: ```python3 -m pip install -r requirements.txt```

## Run Flask server either way
1. Using Flask:
```
python3 -m flask --app hello_timestamp.py run
OR Debug mode: python3 -m flask --app hello_timestamp.py --debug run
```
2. As Python script:
```
export FLASK_DEBUG=1
python3 ./hello_timestamp.py
```

## Test using RESTClient VSCode extension
- Index (i.e. "/"):                             tests/landing.rest
- Simple (i.e. "/time"):                        tests/simple_timestamp__default.rest
- GET: Hello timestamp (/time/<username>):      tests/hello_timestamp__GET_200.rest
- POST: Hello timestamp (/time/<username>):     tests/hello_timestamp__POST_403.rest