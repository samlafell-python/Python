num = input('type any number: ')

addition = 0

if int(num) < 0:
    print('make it positive, fam')
elif int(num) == 0:
    print('cant be 0')
elif int(num) > 0:
    for i in range(1,int(num)+1):
        addition = addition+i
    print('Adding ' + str(int(num)) + ' by ever number below it = ' + str(addition))
