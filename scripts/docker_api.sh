#!/bin/bash
cp docker/api_package/Dockerfile .
docker build --build-arg PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL -t ml_api:latest .

