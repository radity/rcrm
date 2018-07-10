# RCRM
RCRM (Radity CRM) is a modern, easy to use CRM system based on Python and Django.

We intend to keep RCRM simple yet effective and extendable meeting the demands of SMEs and Startups. RCRM will come with modules for different domains such as fintech, blockchain, asset management, sales, marketing and hr. RCRM can be used standalone or can be used to accelarate product development for tailored software solutions.

A detailed Roadmap will follow soon.


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
