# Simple UV commands

# Install uv dependencies
uv install uvicorn 

# UV sync - synchronizes dependencies
uv sync

# Uvicorn server for fastapi application
uv run uvicorn src.app:app --reload
