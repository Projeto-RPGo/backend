#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;36m'
NC='\033[0m'

VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    echo -e "${BLUE}[INFO] Virtual environment not found. Creating a new one...${NC}"
    python3 -m venv $VENV_DIR
fi

if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${BLUE}[INFO] Activating the virtual environment...${NC}"
    source $VENV_DIR/bin/activate
fi

if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${RED}[ERROR] Failed to activate the virtual environment.${NC}"
    return 1
fi

if [ -f .env ]; then
    echo -e "${BLUE}[INFO] Loading environment variables from .env file${NC}"
    export $(grep -v '^#' .env | xargs)
fi

if [ -f requirements.txt ]; then
    echo -e "${BLUE}[INFO] Installing dependencies from requirements.txt${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo -e "${RED}[ERROR] requirements.txt file not found.${NC}"
    return 1
fi

echo -e "${BLUE}[INFO] Running database migrations...${NC}"
python3 manage.py makemigrations
python3 manage.py migrate

echo -e "${GREEN}[SUCCESS] Configuration successful.${NC}"
