# Using Nested Environment Variables with docker compose files

Provides a way to set nested environment variables at a global, local and container scope.

This project has the following structure

```bash
.env # an environment variables file that sets environme
docker-compose # a main docker compose file that uses the include: function to lauch 2 other containers. 
container_1 # a directory hosting files for a container that pulls the global, local and container variables
container_2 # a second directory hosting files for a container that pulls the global, local and container variables.
```

