#!/bin/bash

uv run --env-file=.env.local uvicorn backend.app.main:app  --host 0.0.0.0 --port 8000 --reload