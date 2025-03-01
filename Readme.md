# Nested Environment Variables with Docker Compose Files

Provides a way to set nested environment variables at a global and local scope. It will expose variables to both the container and the docker-compose file.

![alt text](https://raw.githubusercontent.com/andrewkriley/nested-var-compose/refs/heads/v0.3/images/1and2.png)
![alt text](https://raw.githubusercontent.com/andrewkriley/nested-var-compose/refs/heads/v0.3/images/3and4.png)


The intent of this project is demonstrate how nested variables can be used and inspire you to use something similar in your own projects.

This project has the following structure

```bash
.env # a global environment variables file that sets environment variables that will be available to all containers and docker-compose files.
docker-compose.yaml # a main docker compose file that uses the include: function to lauch 2 other containers. 
container_1 # a directory hosting files for a container that pulls the global and local variables
container_2 # a second directory hosting files for a container that pulls the global and local variables.
container_3 # a second directory hosting files for a container that pulls the global and local variables.
container_4 # a second directory hosting files for a container that pulls the global and local variables.
```

Each 'container_N' directory has the following structure
```bash
.env # a local (to the container) environment variables file that sets environment variables that will be available to all containers and docker-compose files.
docker-compose.yaml # a docker-compose.yaml file used to launch the image
```

The docker-compose file uses a range of docker compose features including profiles and lots of variables

```yaml
services:
  server1:
## <--common
    profiles: [all, "${CONTNAME}"]
    restart: unless-stopped
    security_opt:
    - no-new-privileges:true
    environment:
      - GLOBALVAR1=${GLOBALVAR1}
      - GLOBALVAR2=${GLOBALVAR2}
      - LOCALVAR1=${LOCALVAR1}
      - LOCALVAR2=${LOCALVAR2}
      - CONTNAME=${CONTNAME}
## <--container specific
    container_name: ${CONTNAME}
    image: nested-var-compose
    ports:
      - '8101:8080'
    labels:
      - homepage.group=${GLOBALVAR1}
      - homepage.name=${LOCALVAR1}
      - homepage.icon=${LOCALVAR2}
      - homepage.href=${GLOBALVAR1}
      - homepage.description=${LOCALVAR2}
```

# Getting Started

Begin by building the images for each 'container_N'

```bash
cd images
docker build -t nested-var-compose .

```

Then launch the main docker-compose.yaml. We are using the docker compose 'profiles' to enable us to stop and start all, or some containers.

```bash
cd ..
docker compose --profile all up
```

It will then launch like this

```bash
docker compose --profile all up

[+] Running 5/5
 ✔ Network nested-var-compose_default  Created                                                                                                                                                                                                                                                            0.0s 
 ✔ Container server1                   Created                                                                                                                                                                                                                                                            0.1s 
 ✔ Container server4                   Created                                                                                                                                                                                                                                                            0.1s 
 ✔ Container server2                   Created                                                                                                                                                                                                                                                            0.0s 
 ✔ Container server3                   Created                                                                                                                                                                                                                                                            0.1s 
Attaching to server1, server2, server3, server4
server3  |  * Serving Flask app 'app.py'
server3  |  * Debug mode: off
server3  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server3  |  * Running on all addresses (0.0.0.0)
server3  |  * Running on http://127.0.0.1:8080
server3  |  * Running on http://192.168.240.2:8080
server3  | Press CTRL+C to quit
server4  |  * Serving Flask app 'app.py'
server4  |  * Debug mode: off
server2  |  * Serving Flask app 'app.py'
server2  |  * Debug mode: off
server1  |  * Serving Flask app 'app.py'
server1  |  * Debug mode: off
server4  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server4  |  * Running on all addresses (0.0.0.0)
server4  |  * Running on http://127.0.0.1:8080
server4  |  * Running on http://192.168.240.3:8080
server4  | Press CTRL+C to quit
server2  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server2  |  * Running on all addresses (0.0.0.0)
server2  |  * Running on http://127.0.0.1:8080
server2  |  * Running on http://192.168.240.4:8080
server2  | Press CTRL+C to quit
server1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server1  |  * Running on all addresses (0.0.0.0)
server1  |  * Running on http://127.0.0.1:8080
server1  |  * Running on http://192.168.240.5:8080
server1  | Press CTRL+C to quit
```
You can then launch the URLs to see the variables being pulled from the environment variables.

http://yourip:8101<br>
http://yourip:8102<br>
http://yourip:8103<br>
http://yourip:8104


Stoping all the containers
```bash
docker compose --profile all down

[+] Running 5/5
 ✔ Container server3                   Removed                                                                                                                                                                                                                                                           10.3s 
 ✔ Container server2                   Removed                                                                                                                                                                                                                                                           10.4s 
 ✔ Container server1                   Removed                                                                                                                                                                                                                                                           10.4s 
 ✔ Container server4                   Removed                                                                                                                                                                                                                                                           10.4s 
 ✔ Network nested-var-compose_default  Removed   
 ```

Starting a container at a time

```bash
docker compose --profile server1 up -d

[+] Running 2/2
 ✔ Network nested-var-compose_default  Created                                                                                                                                                                                                                                                 
 ✔ Container server1  Started                                                                                                                                                                                                                                                          
TESTandreril@docker-int:~/dev/nested-var-compose$ docker compose --profile server2 up -d
[+] Running 1/1
 ✔ Container server2  Started                                                                                                                                                                                                                                                                      
TESTandreril@docker-int:~/dev/nested-var-compose$ docker compose --profile server3 up -d
[+] Running 1/1
 ✔ Container server3  Started                                                                                                                                                                                                                                                                      
TESTandreril@docker-int:~/dev/nested-var-compose$ docker compose --profile server4 up -d
[+] Running 1/1
 ✔ Container server4  Started                                                                                                                                                                                                                                                                   
TESTandreril@docker-int:~/dev/nested-var-compose$ 