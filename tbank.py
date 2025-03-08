from tinkoff.invest import Client
import datetime

t_token = 't.xWrQYcUmMTn3_SUzwcbHyNpWa31htZDsVMzvmGM0Kbn9XB9DINbcZFr-B35lovHhtcFqvms6oY4iyQ6vZa22zg'
a_id = '2181501776'


def money():
    with Client(t_token) as client:
        r = client.operations.get_portfolio(
            account_id=a_id
        )
        return str(r.total_amount_portfolio.units)


def profit():
    with Client(t_token) as client:
        r = client.operations.get_portfolio(
            account_id=a_id
        )
        pr = 0
        for i in r.positions:
            pr += i.expected_yield.units
        return pr

