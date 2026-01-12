#!/bin/bash
export PYTHONPATH=/app/Phase2_Web:$PYTHONPATH
cd /app/Phase2_Web/backend
uvicorn main:app --host 0.0.0.0 --port $PORT