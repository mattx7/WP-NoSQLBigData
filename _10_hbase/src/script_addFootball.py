import HBaseConstants as Constants
import HBaseSaver as Saver

try:
    Constants.CONNECTION.table('plz')
    Saver.delete_all()
except:
    pass

families = {'family': dict(),  # use defaults
            'Fussball': dict()}

Constants.CONNECTION.create_table(Constants.TABLE_NAME, families)
Saver.save_file('../../resources/plz.data')

# Value einfuegen
for key, data in Constants.TABLE.scan(filter="SingleColumnValueFilter('family', 'city', =, 'regexstring:^HAMBURG$')"):
    print("Adding family 'Fussball' to " + str(key) + "->" + str(data))
    Constants.TABLE.put(bytes(key), {b'Fussball:JaNein': b'ja'})
