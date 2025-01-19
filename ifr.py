# -*- coding: utf-8 -*-
s1 = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя "
s2 = 'ъэюхжбздьщлтшоигрмнпсеачквяуыфцйё '
s_input = 'тыквенные семечки'
res = ''

for i in s_input:
    first_index = s1.index(i)
    res += s2[first_index]
print(res)
