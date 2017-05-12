from _10_hbase.src.data_access.Constants import Constants
from _10_hbase.src.data_access.Saver import Saver

HBSaver = Saver()

try:
    Constants.CONNECTION.table('plz')
    HBSaver.delete_all()
except:
    pass

families = {'family': dict(),  # use defaults
            'Fussball': dict()}

Constants.CONNECTION.create_table(Constants.TABLE_NAME, families)
HBSaver.save_file('../../resources/plz.data')

# Value einfuegen
for key, data in Constants.TABLE.scan(filter="SingleColumnValueFilter('family', 'city', =, 'regexstring:^HAMBURG$')"):
    print("Adding family 'Fussball' to " + str(key) + "->" + str(data))
    Constants.TABLE.put(bytes(key), {b'Fussball:JaNein': b'ja'})
