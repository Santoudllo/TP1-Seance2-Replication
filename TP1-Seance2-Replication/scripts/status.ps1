Write-Host "=== Containers ==="
docker ps --filter "name=node-"

Write-Host "`n=== Health ==="
curl.exe -s http://localhost:8080/health
Write-Host ""
curl.exe -s http://localhost:8081/health
Write-Host ""
curl.exe -s http://localhost:8082/health
Write-Host ""
