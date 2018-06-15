# Download / Update docker-machine (MacOSX / Linux)
curl -L https://github.com/docker/machine/releases/download/v0.2.0/docker-machine_darwin-amd64 > /usr/local/bin/docker-machine
chmod +x /usr/local/bin/docker-machine

# will delete all stopped containers.
docker container prune

# will banish all dangling images to beyond the wall. Add -a to get rid of all unused images (ones with no containers running them).
docker image prune

# will dispatch volumes to their eternal resting place at /dev/null.
docker volume prune

# does the same for networks.
docker network prune

# Pruning is a lot more fun when you can see the impact it has on disk space.
docker system df

# Download / Update docker client (MacOSX)
curl -L https://get.docker.com/builds/Darwin/x86_64/docker-latest > /usr/local/bin/docker

# Another version
curl -L https://get.docker.com/builds/Darwin/x86_64/docker-1.5.0 > /usr/local/bin/docker

# Create a machine with docker-machine on virtualbox (MaxOsX)
docker-machine create --driver virtualbox dev

# Set ENV variables to work on specific machine
eval "$(docker-machine env dev)"

# Remove all untagged images
docker rmi $(docker images | grep "^<none>" | awk "{print $3}")

# Remove all stopped containers.
docker rm $(docker ps -a -q)
