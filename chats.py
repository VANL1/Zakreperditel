def write_ids(new_d):
    with open('chats_ids.txt') as f:
        d = []
        for i in f:
            d.append(int(i[:-1]))
    f.close()
    f = open('chats_ids.txt', 'a')
    if not new_d in d:
        d.append(new_d)

    with open('chats_ids.txt', 'wb'):
        pass

    for i in range(len(d)):
        f.write(str(d[i]) + '\n')

    f.close()

    with open('chats_ids.txt') as f:
        data = []
        for i in f:
            data.append(int(i[:-1]))

