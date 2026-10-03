#!/bin/bash
set -e

if ! docker network inspect distributed-net >/dev/null 2>&1; then
  docker network create --driver bridge distributed-net
fi

docker compose up -d
docker ps
