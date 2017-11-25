# in tarantool database console

s = box.schema.space.create('meetups');

s:insert({1, 'Vadim', 'Graph DB', os.time{year=2017, month=11, day=20, hour=15}})
s:insert({2, 'Tolya', 'tarantool', os.time{year=2017, month=11, day=27, hour=15}})

s:create_index('name', {type = 'hash', parts = {2, 'string'}})

function get_date_from_seconds (seconds) return os.date("%x", seconds) end
