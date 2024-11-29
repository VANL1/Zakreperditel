from tinkoff.invest import Client
import datetime

t_token = 't.amUvdX6qLClmNIFR6rP-aFA42BIJEbLTTQO87gGBYyig5QYXz_KZF5DnBIgad3j1FrbJ6B3FWuIMOhj-ZKzvzA'
a_id = '2181501776'

with Client(t_token) as client:
    r = client.operations.get_operations(
        account_id=a_id,
        from_=datetime.datetime(2023, 8, 7),
        to=datetime.datetime.now()
    )
    x = -3
    # print(r.operations[x].type)
    # print(r.operations[x].payment)
    # print('>>>>>>>>>>>')
    class_code = 'TQCB'
    r = client.instruments.shares()
    print(r)
