# Document-oriented database ([MondoDB](https://www.mongodb.com/))

## Configure application environment

* ([Install Docker](https://docs.docker.com/engine/installation/) for your OS.)

* (Install python3.)

* Install mongo client for python with `sudo python3 -m pip install pymongo`

* Start mongo container with `docker run --name some-mongo -d mongo`.
    * (Or `docker start some-mongo` if already in local repository )

* Use `docker inspect some-mongo | grep IPAddress` to get the IP from the container.

* Change the var HOST in the MongoConstants.py file to the IP of the container.

## Usage

 - Saving:   `python3 MainApp.py --save` to save `plz.data` or `--save <filename>`
 - Reading:  `python3 MainApp.py [--zip, --state, --city] --select ['zip', 'state', 'city']`
 - Deleting: `python3 MainApp.py --clear` to delete all from database


## Troubleshooting

* `docker attach some-mongo` to get into the container. 
    * (`docker exec -i -t some-mongo /bin/bash` for multiple shell instances.)


* MongoDB-Shell [[Ref.]](https://docs.mongodb.com/manual/mongo/#introduction)
 
    * Access with `mongo --shell`
    * Display database you are using `db`
    * Switch database `use <database>`
    * Insert: 
        * `use myNewDatabase`
        * `db.myCollection.insertOne( { x: 1 } );`
    * Find:
        * `db["3test"].find()` 
        * `db.getCollection("3test").find()`
       
* Other useful commands:
    * `sudo mongod --repair`
    * `sudo service mongodb status`

        
 
