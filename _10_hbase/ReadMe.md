## Wide-Column database ([HBase](https://hbase.apache.org/))

## Configure application environment

* ([Install Docker](https://docs.docker.com/engine/installation/) for your OS.)

* (Install python3.)
    * (with dev package `sudo apt-get install python3-dev`)

* Install hbase client for python with `sudo python3 -m pip install happybase`

* Start hbase container with `docker run --name some-hbase -d nerdammer/hbase`.
    * (Or `docker start some-hbase` if already in local repository )

* Get container id with `docker ps`

* Start Thrift with `docker exec -d some-hbase hbase thrift start`

* Use `docker inspect some-hbase | grep IPAddress` to get the IP from the container.

* Change the var HOST in the HBaseConstants.py file to the IP of the container.

## Usage

 - Saving:   `python3 MainApp.py --save` to save `plz.data` or `--save <filename>`
 - Reading:  `python3 MainApp.py [--zip, --state, --city] --select ['zip', 'state', 'city']`
 - Deleting: `python3 MainApp.py --clear` to delete all from database

## Troubleshooting

* `docker attach some-hbase` to get into the container. 
    * (`docker exec -i -t some-hbase /bin/bash` for multiple shell instances.)


## Informations

* HbaseUI is under http://localhost:16010/

## Hadoop
Runs in Standalone HBase/Pseudo-Distibuted mode