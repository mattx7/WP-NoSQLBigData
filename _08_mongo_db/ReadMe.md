Install MongoDB

Start MongoDB
sudo service mongod start

MongoDB-Shell Access with
mongo --shell

Display database you are using
db

Switch database
use <database> 
in this example: use fussball

Insert
db.fussball.insert({name: 'HSV', gruendung: new Date(1887, 09, 29), farben: ['weiss', 'rot'], Tabellenplatz: 17, nike: 'n'});
db.fussball.insert({name: 'Dortmund', gruendung: new Date(1909, 12, 19), farben: ['gelb', 'schwarz'], Tabellenplatz: 16, nike: 'n'});
db.fussball.insert({name: 'Schalke', gruendung: new Date(1904, 5, 4), farben: ['blau'], Tabellenplatz: 15, nike: 'n'});
db.fussball.insert({name: 'Paderborn', gruendung: new Date(1907, 8, 14), farben:['blau', 'weiss', ], Tabellenplatz:14, nike:'n', });
db.fussball.insert({name: 'Hertha', gruendung: new Date(1892, 7, 25), farben: ['blau', 'weiss'], Tabellenplatz: 13, nike: 'j'});
db.fussball.insert({name: 'Augsburg', gruendung: new Date(1907, 8, 8), farben: ['rot', 'weiss'], Tabellenplatz: 12,  nike: 'j'});
db.fussball.insert({name: 'Pauli', gruendung: new Date(1910, 5, 15), farben: ['braun', 'weiss'], Tabellenplatz: 11, nike: 'n'});
db.fussball.insert({name: 'Gladbach', gruendung: new Date(1900, 8,1), farben: ['schwarz', 'weiss', 'gruen'], Tabellenplatz: 10, nike: 'n'});
db.fussball.insert({name: 'Frankfurt', gruendung: new Date(1899, 3, 8), farben: ['rot', 'schwarz', 'weiss'], Tabellenplatz: 9, nike: 'j'});
db.fussball.insert({name: 'Leverkusen', gruendung: new Date(1904, 11, 20, 16, 15), farben: ['rot', 'schwarz'], Tabellenplatz: 8, nike: 'n'});
db.fussball.insert({name: 'Stuttgart', gruendung: new Date(1893, 9, 9 ), farben: ['rot', 'weiss'], Tabellenplatz: 7, nike: 'n'});
db.fussball.insert({name: 'Werder', gruendung: new Date(1899,2,4), farben: ['gruen','weiss'], Tabellenplatz: 6, nike: 'j'});

Findall
db["fussball"].find();

1 Find Augsburg
db["fussball"].find({"name": "Augsburg"})

2 Find niketeam with black color
db["fussball"].find({"farben" :"schwarz", "nike" :"j"})

3 Find niketeam where green and white
db["fussball"].find({"farben" :["gruen","weiss"],"nike": "j"})

4 Find niketeam where green or white
db["fussball"].find({"farben" : { $in: ["gruen","weiss"]}, "nike": "j"})

5 highest tabellenplatz
db.fussball.find().sort({"Tabellenplatz" :-1}).limit(1).pretty()

6 nicht abstiegsgefährdet (unter tabellenplatz 17)
db.fussball.find( { "Tabellenplatz" : { $lt: 17 } } );

c)
beliebiges bei dem die id nicht angezeigt wird
db.fussball.find({"name": "Augsburg"}, { _id: 0 })

d) Führen sie folgende Änderungsoperation aus:
db.fussball.update({name: 'Augsburg'}, {Tabellenplatz: 1})

Was beobachten sie als Ergebnis? 
Die Ausgabe: WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
Der Komplette Datensatz von Augsburg ist nur noch " {Tabellenplatz :1} Name etc ist weg.

Stellen sie den ursprünglichen Zustand von Augsburg (aus sinndeslebens.txt) wieder her.
db.fussball.update({Tabellenplatz: 1},{name: 'Augsburg', gruendung: new Date(1907, 8, 8), farben: ['rot', 'weiss'], Tabellenplatz: 12,  nike: 'j'})

e)
Führen sie folgende Änderungsoperationen aus:

1. Ändern sie den Tabellenplatz von Leverkusen auf 2
db.fussball.findOneAndUpdate({"name": "Leverkusen"},{$set: {"Tabellenplatz": "2"}})

2. Werder soll um einen Tabellenplatz nach vorne gebracht werden
db.fussball.findOneAndUpdate({"name": "Werder"},{$inc: {"Tabellenplatz": -1}})

3. Ergänzen sie für den HSV ein Attribut „abgestiegen“ mit einem sinnvollen Wert
db.fussball.findOneAndUpdate({"name": "HSV"},{$set: {"abgestiegen": "1"}})

4. Ergänzen sie für alle Vereine, deren Vereinsfarbe weiss enthält, ein Attribut „Waschtemperatur“ mit dem Wert 90.
db.fussball.updateMany({"farben": "weiss"},{$set: {"Waschtemperatur": "90 Grad"}})
