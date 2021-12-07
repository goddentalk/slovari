x=dict()
x['Phone']='Телефон'
x['Book']='Книга'
x['Sometimes']='Иногда'
print('Введите слово')
a=input()
if a in x:
    print('Перевод вашего слова:',x[a])
else:
    print('Какой перевод вашего слова?')
    perevod=input()
    x[a]=perevod