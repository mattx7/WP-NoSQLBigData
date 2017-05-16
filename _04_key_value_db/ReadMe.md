# Key-Value Database with Redis

## How to run the application

* ([Install Docker](https://docs.docker.com/engine/installation/) for your OS.)

* (Install python.)

* Install redis client for python with `sudo pip install redis`

* Start redis container with `docker run --name some-redis -d redis`.

* Get the container-id with `docker ps`.

* Use `docker inspect <container-id>` to get the IP from the redis container.

* Change the var HOST in the RedisConstants.py file to the IP of the redis container.

## Usage
 - Saving:   Use `--save <filename>` to save a File from resource folder 
 - Reading:  Use `[--id, --state, --city] --select ['id', 'state', 'city']`
 - Deleting: Use `--clear` to delete all from database
        
## Key-value structure

        KEY          -            VALUE

`<id>:<state>:<city># - loc [list] pop <value>`

`<id>:<state>:<city>#loc - [list]`

`<id>:<state>:<city>#pop - <value>`

