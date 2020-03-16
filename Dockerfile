FROM python:3.7-slim-buster

WORKDIR /app

# Copy Pipfile and Pipfile.lock to working directory i.e. /app
COPY ./Pipfile* /app/

# Create .venv in current folder
ENV PIPENV_VENV_IN_PROJECT=true

# Install dependencies w/ PipEnv
RUN python3 -m pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --pre && \
    pipenv graph

COPY ./web_app.py /app/

RUN ls -latr && ls -latr `pipenv --venv`/lib


# Run python prgram
CMD ["python", "./web_app.py"]