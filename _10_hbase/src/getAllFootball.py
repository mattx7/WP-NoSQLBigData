from _10_hbase.src.data_access.Constants import Constants

for key, data in Constants.TABLE.scan(filter="SingleColumnValueFilter('family', 'city', =, 'regexstring:^HAMBURG$')"):
    print(str(key) + " -> " + str(data))
print("\n")

for key, data in Constants.TABLE.scan(filter="FamilyFilter(=, 'binary:Fussball')"):
    print(str(key) + " -> " + str(data))
