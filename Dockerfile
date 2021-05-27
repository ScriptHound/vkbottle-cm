FROM python:3.8

WORKDIR /vkbottle-cm

RUN python -m venv venv
RUN python -m pip install poetry

COPY pyproject.toml poetry.lock ./
COPY . /vkbottle-cm

RUN chmod +x bot-entrypoint.sh

ENTRYPOINT [ "./bot-entrypoint.sh" ]
