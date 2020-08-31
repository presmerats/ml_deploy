#!/bin/bash
docker run --name ml_api -d -p 8000:5000 --rm ml_api:latest