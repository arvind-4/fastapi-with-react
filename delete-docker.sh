docker system df

docker rmi -f $(docker images -aq)
docker system prune -a --volumes
docker system prune -a
docker system prune --force
docker volume prune 
docker rmi $(docker images -a)
docker volume rm $(docker volume ls -q --filter dangling=true)

docker system df