my_dict = {'Андрей': 1994, 'Мария': 1995, 'Иван': 1997, 'Дарья': 2002, 'Михаил': 2003}
print('Словарь:', my_dict)
print('Год рождения Марии:', my_dict['Мария'])
print('Год рождения Василисы:', my_dict.get('Василиса', 'нет такого ключа'))
my_dict.update({'Славя': 1995, 'Ульяна': 2005})
removed_year = my_dict.pop('Ульяна')
print('Значение удалённого элемента \'Ульяна\':', removed_year)
print('Изменённый словарь:', my_dict)

print()
my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)
