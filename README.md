# flask-py-sandbox
Python Flask sandbox

Using PipEnv:
- Install pipenv : pip install pipenv
- Enable venv in current folder: export PIPENV_VENV_IN_PROJECT=true
- Launch pipenv where Pipfile exists : pipenv install

To run flask web-app:
- pipenv run python3 web_app.py
- OR Run: pipevn shell. Then inside pipenv shell, execute: python3 web_app.py
- OR Run: pipevn shell. Then inside pipenv shell, execute: chmod +x web_app.py. Then run python script as : ./web_app.py

Dockerized app:
## Option 1:
- To use pip and requirements.txt, use file : Dockerfile_for_pip
- docker build . --file Dockerfile_for_pip --tag flask-app-pip
- docker run -p 5000:5000 -t flask-app-pip
## Option 2:
- To use PipEnv, use file : Dockerfile_for_PipEnv
- docker build . --file Dockerfile_for_PipEnv --tag flask-app-pipenv
- docker run -p 5000:5000 -t flask-app-pipenv

----

Also refer branch: https://github.com/productiveAnalytics/flask-py-sandbox/tree/feature/another_RESTful_flask_app
