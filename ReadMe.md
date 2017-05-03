# NoSQL & Big-Data

## Tasks

### [Task 4 (Key-Value-Database)](_4_key_value_db)

Program that can import a file and save it in redis.


### [Task 5 (Graph-Database)](_5_graph_db_moduls)

Little graph for HAW-moduls.

### [Task 6 (Graph-Database)](_6_graph_db_conecptnet)

import a graph and read the node with the id „/c/en/baseball“.

### [Task 7 (MongoDB)](_7_mongo_db)

Program that can import a file and save it in mongodb.

### [Task 8 (MongoDB)](_7_mongo_db)



## NoSQL-databases manual

### Redis installation

- Install Redis 
> sudo apt-get install redis-server 

- Check Installation
> redis-cli ping

- Install Python client for Redits 
> sudo pip install redis

Reference: https://wiki.ubuntuusers.de/Redis/

Framework: https://pypi.python.org/pypi/redis 

Dockerfile: https://runnable.com/docker/python/dockerize-your-python-application


### MongoDB installation (Community Edition)

Reference: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#reload-local-package-database

1. Import the public key used by the package management system.

> sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

2. Create a list file for MongoDB.

Ubuntu 12.04

> echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

Ubuntu 14.04

> echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

Ubuntu 16.04

> echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

3. Reload local package database.

> sudo apt-get update

4. Install the MongoDB packages.

> sudo apt-get install -y mongodb-org
