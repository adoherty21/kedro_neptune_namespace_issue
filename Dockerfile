FROM python:3.9.15-slim AS production
# SWITCH TO BASE PYTHON
ARG PYTHON_VER="3.9.15"

# COPY EVERYTHING
COPY . .

RUN apt-get update
RUN apt-get install -y --no-install-recommends make build-essential

RUN pip install pip --upgrade
RUN pip --no-cache-dir install --upgrade awscli

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENV CODEARTIFACT_AUTH_TOKEN=""

CMD ["poetry", "run", "kedro", "run", "--pipeline=namespace_1"]
