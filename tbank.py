from tinkoff.invest import Client
import datetime

t_token = 't.amUvdX6qLClmNIFR6rP-aFA42BIJEbLTTQO87gGBYyig5QYXz_KZF5DnBIgad3j1FrbJ6B3FWuIMOhj-ZKzvzA'
a_id = '2181501776'


def money():
    with Client(t_token) as client:
        r = client.operations.get_portfolio(
            account_id=a_id
        )
        return str(r.total_amount_portfolio.units)
