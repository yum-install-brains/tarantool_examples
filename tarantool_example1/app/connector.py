#!/usr/bin/python


from tarantool import Connection
class tarantooldb():
    """Взаимодействие с tarantool"""
    def __init__(self, host, port, user=None, password=None, database=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def db_connect(self):
        return Connection(self.host, self.port)

    def db_select(self, idx, vals):
        conn = self.db_connect()
        return conn.select(self.database, vals, index = idx)

    def db_call(self, func, vals):
        conn = self.db_connect()
        return conn.call(func, (vals))


db = tarantooldb('localhost', 3301, database='meetups')
result = db.db_select('name', 'Tolya')
print(result)
print(db.db_call('get_date', result[0][3]))
