# Key-Value Database ([Redis](https://redis.io/))

## Configure application environment

* ([Install Docker](https://docs.docker.com/engine/installation/) for your OS.)

* (Install python3.)

* Install redis client for python with `sudo python3 -m pip install redis`

* Start redis container with `docker run --name some-redis -d redis`.
    * (Or `docker start some-redis` if already in local repository )

* Use `docker inspect some-redis | grep IPAddress` to get the IP from the container.

* Change the var HOST in the RedisConstants.py file to the IP of the container.

## Usage

 - Saving:   `python3 MainApp.py --save` to save `plz.data` or `--save <filename>`
 - Reading:  `python3 MainApp.py [--zip, --state, --city] --select ['zip', 'state', 'city']`
 - Deleting: `python3 MainApp.py --clear` to delete all from database
        
## Key-value structure

        KEY          -            VALUE

`<id>:<state>:<city># - loc [list] pop <value>`

`<id>:<state>:<city>#loc - [list]`

`<id>:<state>:<city>#pop - <value>`

