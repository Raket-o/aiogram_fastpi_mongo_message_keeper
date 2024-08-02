#!/usr/bin/env bash

uvicorn app.main:app --host 192.168.55.5 --port 8000 --reload
