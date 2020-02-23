#!/bin/bash
set -e

echo "Loggin in to Docker github"
sudo docker login docker.pkg.github.com
echo "Stopping docker images..."
sudo docker-compose -f docker-compose.master.yml down --rmi 'all'
echo "Pulling docker images..."
sudo docker-compose -f docker-compose.master.yml pull
echo "Starting docker images..."
sudo docker-compose -f docker-compose.master.yml up -d
