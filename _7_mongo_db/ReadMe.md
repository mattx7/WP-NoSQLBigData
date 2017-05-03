# HowTo
 1. Install PyMongo [[Ref.]](https://docs.mongodb.com/ecosystem/drivers/python/)

    > sudo python -m pip install pymongo

 2. Start with: [[Ref.]](http://stackoverflow.com/questions/7744147/pymongo-keeps-refusing-the-connection-at-27017)

    > sudo service mongod start
        
 - MongoDB-Shell [[Ref.]](https://docs.mongodb.com/manual/mongo/#introduction)
 
    * Access with
        > mongo --shell
    * Display database you are using
        > db
    * Switch database
        > use \<database\>
    * Insert
        > use myNewDatabase 
        
        > db.myCollection.insertOne( { x: 1 } );
    * Find
        > db["3test"].find()
        > db.getCollection("3test").find()
       
 - Other useful commands:
 
    * sudo mongod --repair
    * sudo service mongodb status