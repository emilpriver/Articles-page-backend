#!/bin/bash
set -e

echo "Stopping docker images..."
docker-compose -f docker-compose.master.yml down --rmi 'all'
echo "Pulling docker images..."
docker-compose -f docker-compose.master.yml pull
echo "Starting docker images..."
docker-compose -f docker-compose.master.yml up -d
