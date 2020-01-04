ab = { 'Swan' : 'swan@gmail.com',
       'Alex': 'alex@gmail.com',
       'Larry': 'larry@mail.ru',
       'Spammer': 'spam@mail.ru'
}
print("Email Swan'a: ", ab['Swan'])

del ab['Spammer']
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name,address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido: ", ab['Guido'])
    help(dict)