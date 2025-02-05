#!/usr/bin/env sh

python3 -m src.main #src/main.py
cd public && python3 -m http.server 8888