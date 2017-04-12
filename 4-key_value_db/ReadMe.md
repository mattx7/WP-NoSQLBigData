# Key-Value Database with Redis

## Installation

- Install Redis 
> sudo apt-get install redis-server 

- Check Installation
> redis-cli ping

- Install Python client for Redits 
> sudo pip install redis

redis-py: https://pypi.python.org/pypi/redis 

Dockerfile: https://runnable.com/docker/python/dockerize-your-python-application

## Key-Value structure

        KEY          -            VALUE

`<id>:<state>:<city># - loc [list] pop <value>`

`<id>:<state>:<city>#loc - [list]`

`<id>:<state>:<city>#pop - <value>`
