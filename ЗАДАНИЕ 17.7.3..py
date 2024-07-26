money=int(input("Введите сумму вклада:"))
percent={'ТКБ':5.6, 'СКБ':5.9, 'ВТБ':4.28,'СБЕР':4.0}
dipposit=[]
dipposit.append(int(percent['ТКБ']*money/100))
dipposit.append(int(percent['СКБ']*money/100))
dipposit.append(int(percent['ВТБ']*money/100))
dipposit.append(int(percent['СБЕР']*money/100))
print(dipposit)
print('Выгодный вклад:',int (max (dipposit)))
