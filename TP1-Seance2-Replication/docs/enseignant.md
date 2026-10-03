# Notes enseignant

## Positionnement

Ce mini-TP intervient au début de la séance 2, après l'introduction et la question :

> Pourquoi distribuer les données ?

Il sert à faire comprendre la réplication **avant** d'introduire Cassandra.

## Durée

Environ 1 heure :

- 5 min : rappel
- 10 min : démarrage
- 10 min : écriture
- 10 min : réplication
- 10 min : panne
- 10 min : questions et bilan
- 5 min : transition vers Cassandra

## Point pédagogique important

L'application est une **simulation pédagogique**.

Elle ne réalise pas une réplication automatique entre les conteneurs. Le schéma montre le principe de réplication et permet de travailler la notion de panne/résilience sans introduire immédiatement Cassandra.

La vraie réplication distribuée sera étudiée ensuite avec Cassandra.

## Transition

Après le TP :

1. SGBD distribué
2. Cassandra
3. Cluster / Node / Datacenter / Rack
4. Keyspace / Table / Partition / Row
5. CQL
6. Réplication
7. Partitionnement
8. Consistent Hashing
9. Hot Spots
