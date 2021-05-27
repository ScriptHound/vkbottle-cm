#!/bin/sh

echo "Entering venv"
chmod a+rwx -R venv
python -m venv venv && . venv/bin/activate
echo;

echo "Installing vkbottle3"
python -m pip install -U https://github.com/timoniq/vkbottle/archive/master.zip
echo;

poetry install
python -m pip freeze

echo "Running migrations"
alembic upgrade head
echo;


echo "Running bot"
python main.py
echo;