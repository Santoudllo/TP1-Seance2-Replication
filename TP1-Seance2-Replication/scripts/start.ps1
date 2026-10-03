if (-not (docker network inspect distributed-net 2>$null)) {
    docker network create --driver bridge distributed-net
}

docker compose up -d
docker ps
