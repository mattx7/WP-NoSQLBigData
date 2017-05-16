import happybase

connection = happybase.Connection('localhost', autoconnect=False)
connection.open()
# connection.delete_table('table')
families = {
    'family': dict(),  # use defaults
}
# connection.create_table('table', families)
table = connection.table('table')

table.put(b'row-key', {b'family:qual1': b'value1',
                       b'family:qual2': bytes(float(123))})

row = table.row(b'row-key')
print(row[b'family:qual1'])  # prints 'value1'

for key, data in table.rows([b'row-key-1', b'row-key-2']):
    print(key, data)  # prints row key and data for each row

for key, data in table.scan(row_prefix=b'row'):
    print(key, data)  # prints 'value1' and 'value2'

row = table.delete(b'row-key')
