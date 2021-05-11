FROM python:3.8

WORKDIR /vkbottle-cm

RUN python -m venv venv
RUN python -m pip install poetry

COPY pyproject.toml poetry.lock ./
COPY . .

RUN . venv/bin/activate && poetry install

RUN chmod +x bot-entrypoint.sh

ENTRYPOINT [ "./bot-entrypoint.sh" ]
