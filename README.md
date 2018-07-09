# RCRM

Installation (for Development)
------------------------------
We use Docker.

[Download Docker](https://www.docker.com/community-edition)

# Docker can't help for some devices. If the project does not work with Docker, Docker Toolbox will help you.

[Download Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/#step-2-install-docker-toolbox)

# How to Run?
To run the project (for the first time):
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
```

To run the project (after the first time):
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml start -d
```

To stop the project:
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml stop
```

To see logs:
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs -f --tail 50
```


# We have a default admin user.
email = admin@localhost

password = secret