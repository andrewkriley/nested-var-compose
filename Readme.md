# Nested Environment Variables with Docker Compose Files

Provides a way to set nested environment variables at a global, local and container scope. It will expose variables to both the container and the docker-compose file.

This project has the following structure

```bash
.env # a global environment variables file that sets environment variables that will be available to all containers and docker-compose files.
docker-compose.yaml # a main docker compose file that uses the include: function to lauch 2 other containers. 
container_1 # a directory hosting files for a container that pulls the global, local and container variables
container_2 # a second directory hosting files for a container that pulls the global, local and container variables.
```

Each 'container_N' directory has the following structure
```bash
.env # a local (to the container) environment variables file that sets environment variables that will be available to all containers and docker-compose files.
app.py # a flask application that launches a webserver and displays the global, local and container specific variables
docker-compose.yaml # a docker-compose.yaml file used to launch the image
Dockerfile # the Dockerfile that constructs the container image used by the docker-compose.yaml file
requirements.txt # a requirements file used by the Dockerfile to install package dependancies 
```

