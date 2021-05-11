#!/bin/sh
echo "Entering venv"
. venv/bin/activate
echo;

echo "Running migrations"
alembic upgrade head
echo;

echo "Installing vkbottle3"
python -m pip install -U https://github.com/timoniq/vkbottle/archive/master.zip
echo;

echo "Running bot"
python main.py
echo;