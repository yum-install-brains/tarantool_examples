Пример взаимодействия тарантула с Python3 приложением

Подготовка:

1. Запустим контейнер с tarantool 1.7
docker run \
  --name mytarantool \
  -d -p 3301:3301 \
  -v /data/dir/on/host:/var/lib/tarantool \
  tarantool/tarantool:1.7

2. Подключимся к консоли и создадим необходимые для примера модель и данные
docker exec -t -i mytarantool console
>s = box.schema.space.create('meetups');

>s:insert({1, 'Vadim', 'Graph DB', os.time{year=2017, month=11, day=20, hour=15}})
>s:insert({2, 'Tolya', 'tarantool', os.time{year=2017, month=11, day=27, hour=15}})

>s:create_index('name', {type = 'hash', parts = {2, 'string'}})

>function get_date_from_seconds (seconds) return os.date("%x", seconds) end

>os.exit()

3. Установим модуль tarantool
$ virtualenv tarantool
$ source tarantool/bin/activate
$ pip3 install tarantool

4. Запустим тестовое приложение (выведет одну строку из спейса, отфильтрованную по имени и переведет unix-time в дату)
$ python3 connector.py
