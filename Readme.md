# Nested Environment Variables with Docker Compose Files

Provides a way to set nested environment variables at a global, local and container scope. It will expose variables to both the container and the docker-compose file.

The intent of this project is demonstrate how nested variables can be used and inspire you to use something similar in your own projects.

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

# Getting Started

Begin by building the images for each 'container_N'

```bash
cd container_1
docker build -t server1 .

cd container_2
docker build -t server2 .
```

Then launch the main docker-compose.yaml. We are using the docker compose 'profiles' to enable us to stop and start all, or some containers.

```bash
cd ..
docker compose --profile all up
```

It will then launch like this

```bash
docker-server:~/dev/nested-var-compose$ docker compose --profile all up
[+] Running 3/3
 ✔ Network nested-var-compose_default  Created                                                                                      0.0s 
 ✔ Container server1                   Created                                                                                      0.0s 
 ✔ Container server2                   Created                                                                                      0.0s 
Attaching to server1, server2
server1  |  * Tip: There are .env files present. Install python-dotenv to use them.
server2  |  * Tip: There are .env files present. Install python-dotenv to use them.
server1  |  * Serving Flask app 'app.py'
server1  |  * Debug mode: off
server2  |  * Serving Flask app 'app.py'
server2  |  * Debug mode: off
server2  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server2  |  * Running on all addresses (0.0.0.0)
server2  |  * Running on http://127.0.0.1:8080
server2  |  * Running on http://192.168.240.3:8080
server2  | Press CTRL+C to quit
server1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server1  |  * Running on all addresses (0.0.0.0)
server1  |  * Running on http://127.0.0.1:8080
server1  |  * Running on http://192.168.240.2:8080
server1  | Press CTRL+C to quit
```
