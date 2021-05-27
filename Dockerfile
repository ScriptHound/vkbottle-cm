FROM python:3.8

WORKDIR /vkbottle-cm

COPY pyproject.toml poetry.lock ./
COPY . /vkbottle-cm

RUN chmod +x bot-entrypoint.sh

ENTRYPOINT [ "./bot-entrypoint.sh" ]
