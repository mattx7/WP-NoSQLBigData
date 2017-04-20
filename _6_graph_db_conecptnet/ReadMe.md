Schreiben sie eine cypher-Anfrage, die für den Knoten mit der ID „/c/en/baseball“ alle direkt mit dem Kantenlabel „IsA“ verbundenen Knoten findet.
```
MATCH (baseball {id: "/c/en/baseball"})-[:IsA]->(teil) RETURN teil.id
```
