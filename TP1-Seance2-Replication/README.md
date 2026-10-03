# TP1 — Réplication | Séance 2

**Module :** Données distribuées — M2 Big Data & IA  
**Durée :** 1h maximum  
**Format :** binôme

## Objectif

Comprendre concrètement le principe de **réplication** avec trois conteneurs Docker.

> Ce TP est volontairement indépendant de Cassandra. Cassandra sera étudié ensuite dans le cours.

## Prérequis

- Docker Desktop
- Docker Compose
- Git
- Terminal (Git Bash ou PowerShell)

## 1. Cloner le repository

Après avoir forké le repository :

```bash
git clone https://gitlab.com/<votre-compte>/TP1-Seance2-Replication.git
cd TP1-Seance2-Replication
```

## 2. Créer le réseau Docker

```bash
docker network create --driver bridge distributed-net
```

Vérifier :

```bash
docker network ls
```

## 3. Démarrer les trois nœuds

```bash
docker compose up -d
```

Vérifier :

```bash
docker ps
```

Vous devez retrouver :

- `node-leader`
- `node-follower-1`
- `node-follower-2`

## 4. Vérifier les nœuds

```bash
curl http://localhost:8080/health
curl http://localhost:8081/health
curl http://localhost:8082/health
```

## 5. Suivre le TP

Toutes les étapes pédagogiques sont dans :

```text
TP1.md
```

## Nettoyage

À la fin :

```bash
docker compose down
```

Puis, si vous souhaitez supprimer le réseau :

```bash
docker network rm distributed-net
```
