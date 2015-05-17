# Download / Update docker-machine (MacOSX / Linux)
curl -L https://github.com/docker/machine/releases/download/v0.2.0/docker-machine_darwin-amd64 > /usr/local/bin/docker-machine
chmod +x /usr/local/bin/docker-machine

# Download / Update docker client (MacOSX)
curl -L https://get.docker.com/builds/Darwin/x86_64/docker-latest > /usr/local/bin/docker

# Another version
curl -L https://get.docker.com/builds/Darwin/x86_64/docker-1.5.0 > /usr/local/bin/docker

# Create a machine with docker-machine on virtualbox (MaxOsX)
docker-machine create --driver virtualbox dev

# Set ENV variables to work on specific machine
eval "$(docker-machine env dev)"
