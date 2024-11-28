f = open('chats_ids.txt', 'a')

d = dict()
d = {-1002269645021: 'Пердёжное царство'}
new_d = {1036894021: 'Лс с ботом'}
d.update(new_d)
with open('chats_ids.txt', 'wb'):
    pass
f.write(str(d))
