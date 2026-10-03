#!/bin/bash

docker compose down

echo "Pour supprimer également le réseau :"
echo "docker network rm distributed-net"
