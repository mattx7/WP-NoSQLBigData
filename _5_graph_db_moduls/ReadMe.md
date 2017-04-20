# Modul-Graph with Neo4j
HELP FROM http://www.apcjones.com/arrows/#

## Neo4j installation

The Neo4j Debian repository can be used on Debian and Debian-based distributions like Ubuntu.

Documentation for the Neo4j 3.0 (and above) Debian package is available here.

To use the repository add it to the list of sources:

`wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt-get update`


## Insert Graph

1. Start Neo4j with:

    > neo4j start

2. Open the address `localhost:7474` in browser.
 
3. Insert following code in the Neo4j command line:

    CREATE (`BWL1` :Fach {title: 'BWL1'}) ,  
    (`PM1` :Fach {title: 'PM1'} ) ,
  (`GI` :Fach {title: 'GI'} ) ,
  (`MG` :Fach {title: 'MG'} ) ,
  (`RMP` :Fach {title: 'RMP'} ) ,
  (`LB` :Fach {title: 'LB'} ) ,
  (`DB` :Fach {title: 'DB'} ) ,
  (`AF` :Fach {title: 'AF'} ) ,
  (`SE1` :Fach {title: 'SE1'} ) ,
  (`BS` :Fach {title: 'BS'} ) ,
  (`BWL2` :Fach {title: 'BWL2'} ) ,
  (`PM2` :Fach {title: 'PM2'} ) ,
  (`GKA` :Fach {title: 'GKA'} ) ,
  (`AD` :Fach {title: 'AD'} ) ,
  (`GW1` :Fach {title: 'GW1'} ) ,
  (`IS` :Fach {title: 'IS'} ) ,
  (`SE2` :Fach {title: 'SE2'} ) ,
  (`RN` :Fach {title: 'RN'} ) ,
  (`NoSQL` :Fach {title: 'NoSQL'} ) ,
  (`GW2` :Fach {title: 'GW2'} ) ,
  (`MG`)-[:`RELATED_TO`]->(`LB`),
  (`MG`)-[:`RELATED_TO`]->(`AF`),
  (`MG`)-[:`RELATED_TO`]->(`DB`),
  (`BWL1`)-[:`RELATED_TO`]->(`BWL2`),
  (`MG`)-[:`RELATED_TO`]->(`GKA`),
  (`GI`)-[:`RELATED_TO`]->(`LB`),
  (`GI`)-[:`RELATED_TO`]->(`GKA`),
  (`GI`)-[:`RELATED_TO`]->(`RMP`),
  (`PM1`)-[:`RELATED_TO`]->(`PM2`),
  (`PM1`)-[:`RELATED_TO`]->(`DB`),
  (`PM1`)-[:`RELATED_TO`]->(`BS`),
  (`PM1`)-[:`RELATED_TO`]->(`AD`),
  (`GI`)-[:`RELATED_TO`]->(`AD`),
  (`PM1`)-[:`RELATED_TO`]->(`IS`),
  (`PM1`)-[:`RELATED_TO`]->(`SE2`),
  (`PM1`)-[:`RELATED_TO`]->(`RN`),
  (`PM1`)-[:`RELATED_TO`]->(`SE1`),
  (`RMP`)-[:`RELATED_TO`]->(`BS`),
  (`PM2`)-[:`RELATED_TO`]->(`IS`),
  (`PM2`)-[:`RELATED_TO`]->(`SE1`),
  (`PM2`)-[:`RELATED_TO`]->(`SE2`),
  (`PM2`)-[:`RELATED_TO`]->(`NoSQL`),
  (`DB`)-[:`RELATED_TO`]->(`BWL2`),
  (`DB`)-[:`RELATED_TO`]->(`SE1`),
  (`DB`)-[:`RELATED_TO`]->(`SE2`),
  (`DB`)-[:`RELATED_TO`]->(`IS`),
  (`DB`)-[:`RELATED_TO`]->(`NoSQL`),
  (`SE1`)-[:`RELATED_TO`]->(`SE2`),
  (`SE1`)-[:`RELATED_TO`]->(`IS`),
  (`BS`)-[:`RELATED_TO`]->(`RN`),
  (`AF`)-[:`RELATED_TO`]->(`IS`),
  (`AF`)-[:`RELATED_TO`]->(`GKA`),
  (`LB`)-[:`RELATED_TO`]->(`GKA`),
  (`GKA`)-[:`RELATED_TO`]->(`SE2`),
  (`GKA`)-[:`RELATED_TO`]->(`IS`),
  (`AD`)-[:`RELATED_TO`]->(`RN`)
  
  Alles ausgeben
  MATCH (n) RETURN (n)
  
  Was mit NoSQL Verbunden ist
  
  MATCH (NoSQL {title: 'NoSQL'})<-[:RELATED_TO]-(Fach) RETURN Fach.title
  
  Ausgabe: DB, PT
  
  Welche im Studium nicht wieder genutzt werden
  
 MATCH (Fach) WHERE NOT (Fach)-[]->() RETURN DISTINCT Fach
  
  Ausgabe: GW1, GW2, NoSQL, RN, IS, SE2, BWL2

Schreiben sie eine cypher-Anfrage, die für den Knoten mit der 
ID „/c/en/baseball“ alle direkt mit dem Kantenlabel „IsA“ verbundenen Knoten findet.

MATCH (n{ID:/c/en/baseball})<-[:IsA]-(x) RETURN n
