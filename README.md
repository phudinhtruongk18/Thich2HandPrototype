# [thich2hand.com](https://thich2hand.com)
# [dev.thich2hand.com](https://dev.thich2hand.com)


Place to buy, exchange, and sell old book

Project Purpose:
============================
test ci/cd, config port, security, docker, docker-compose in personal project

DEV
============================

Build dev:
```shell
docker-compose build
```
Run dev:
```shell
docker-compose run
```

DEPLOY
============================

Build deploy:
```shell
docker-compose -f docker-compose-deploy.yml build
```
Run deploy:
```shell
docker-compose -f docker-compose-deploy.yml up
```


# Pre-commit
```
pre-commit install
pre-commit run
```
