#!/bin/bash

echo "=== Containers ==="
docker ps --filter "name=node-"

echo
echo "=== Health ==="
curl -s http://localhost:8080/health
echo
curl -s http://localhost:8081/health
echo
curl -s http://localhost:8082/health
echo
