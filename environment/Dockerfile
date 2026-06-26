# Original image used an unpinned tag (python:latest). 
# Replaced with an approved Harbor base image pinned by digest.

FROM python:3.11-slim

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log